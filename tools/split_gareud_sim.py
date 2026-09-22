#!/usr/bin/env python3
"""Preview/apply the fixed GAREUD-Sim sequence split; never modify train contents."""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
from pathlib import Path

DEFAULT_MANIFEST = Path(__file__).resolve().parents[1] / "splits/gareud_sim/split.json"


def numeric_key(name: str) -> int:
    if not isinstance(name, str) or not re.fullmatch(r"data_[1-9][0-9]*", name):
        raise ValueError(f"Invalid original sequence ID: {name!r}")
    return int(name.split("_")[1])


def load_manifest(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if data.get("dataset") != "GAREUD-Sim" or data.get("sequence_namespace") != "data_<integer>":
        raise ValueError("Expected a GAREUD-Sim manifest in the original data_<id> namespace.")
    splits = data.get("splits", {})
    if set(splits) != {"train", "val", "test"}:
        raise ValueError("Manifest must contain train, val, and test splits.")
    for key, ids in list(splits.items()) + [("original_test", data.get("original_test", []))]:
        if not isinstance(ids, list) or not ids:
            raise ValueError(f"Missing or empty ID list: {key}")
        for name in ids:
            numeric_key(name)
        if len(ids) != len(set(ids)):
            raise ValueError(f"Duplicate IDs in manifest list: {key}")
    train, val, test = (set(splits[key]) for key in ("train", "val", "test"))
    if train & val or train & test or val & test:
        raise ValueError("Manifest splits overlap.")
    if val | test != set(data["original_test"]):
        raise ValueError("Validation and test must exactly partition the original test pool.")
    expected_train = {f"data_{i}" for i in list(range(1, 31)) + [40] + list(range(55, 85)) + [100, 103]}
    expected_pool = {f"data_{i}" for i in list(range(31, 40)) + list(range(41, 55)) + [101, 102]}
    if train != expected_train or val | test != expected_pool:
        raise ValueError("Manifest does not match the corrected 63-train / 25-test inventory (data_40 belongs to train).")
    counts = {key: len(ids) for key, ids in splits.items()}
    if counts != {"train": 63, "val": 17, "test": 8} or data.get("counts") != counts:
        raise ValueError("Expected split counts: train=63, val=17, test=8.")
    if data.get("seed") != 42:
        raise ValueError("This split version requires seed 42.")
    shuffled = sorted(data["original_test"], key=numeric_key)
    random.Random(42).shuffle(shuffled)
    if val != set(shuffled[:17]) or test != set(shuffled[17:]):
        raise ValueError("Manifest assignments do not match the fixed seed-42 split.")
    return data


def is_link(path: Path) -> bool:
    # FILE_ATTRIBUTE_REPARSE_POINT also catches Windows junctions on Python 3.9/3.10.
    return path.is_symlink() or bool(getattr(path.lstat(), "st_file_attributes", 0) & 0x400)


def inventory(path: Path, optional: bool = False) -> set[str]:
    if not path.exists() and not path.is_symlink():
        if optional:
            return set()
        raise ValueError(f"Missing required directory: {path}")
    if is_link(path) or not path.is_dir():
        raise ValueError(f"Expected an ordinary directory, not a file/link: {path}")
    names = set()
    for child in path.iterdir():
        if child.is_symlink() or child.is_dir() or child.name.startswith("data_"):
            if is_link(child) or not child.is_dir():
                raise ValueError(f"Sequence path is a file or link: {child}")
            numeric_key(child.name)
            names.add(child.name)
    return names


def build_plan(root: Path, data: dict, undo: bool = False) -> list[tuple[Path, Path]]:
    splits = data["splits"]
    actual = {key: inventory(root / key, optional=(key == "val")) for key in ("train", "val", "test")}
    train = set(splits["train"])
    if actual["train"] != train:
        missing = sorted(train - actual["train"], key=numeric_key)
        extra = sorted(actual["train"] - train, key=numeric_key)
        raise ValueError(f"Training inventory mismatch. Missing={missing}; unexpected={extra}")
    duplicate = actual["val"] & actual["test"]
    if duplicate:
        raise ValueError(f"Sequences exist in both val and test: {sorted(duplicate, key=numeric_key)}")
    pool = set(data["original_test"])
    found = actual["val"] | actual["test"]
    if found != pool:
        missing = sorted(pool - found, key=numeric_key)
        extra = sorted(found - pool, key=numeric_key)
        raise ValueError(f"Held-out inventory mismatch. Missing={missing}; unexpected={extra}")
    wrong_test = set(splits["test"]) - actual["test"]
    if wrong_test:
        raise ValueError(f"Fixed test sequences must remain under test/: {sorted(wrong_test, key=numeric_key)}")
    source, destination = ("val", "test") if undo else ("test", "val")
    moves = []
    for name in sorted(splits["val"], key=numeric_key):
        if name in actual[source]:
            src, dst = root / source / name, root / destination / name
            if dst.exists() or dst.is_symlink():
                raise ValueError(f"Destination already exists; refusing to overwrite: {dst}")
            moves.append((src, dst))
    return moves


def execute(root: Path, data: dict, apply: bool = False, undo: bool = False) -> int:
    # Validate ALL directories before making even the first move.
    moves = build_plan(root, data, undo=undo)
    mode = "APPLY" if apply else "DRY RUN"
    target = "train=63, val=0, test=25" if undo else "train=63, val=17, test=8"
    print(f"{mode}: {len(moves)} sequence(s) to move. Target: {target}")
    for src, dst in moves:
        print(f"  {src} -> {dst}")
    if not apply:
        print("No files changed. Add --apply to perform these moves.")
        return len(moves)
    moved = 0
    try:
        for src, dst in moves:
            dst.parent.mkdir(exist_ok=True)
            if is_link(dst.parent):
                raise ValueError(f"Destination parent became a link: {dst.parent}")
            if dst.exists() or dst.is_symlink():
                raise ValueError(f"Destination exists; refusing to overwrite: {dst}")
            if is_link(src) or not src.is_dir():
                raise ValueError(f"Source is no longer an ordinary directory: {src}")
            # No copy/delete fallback and no overwrite operation. Cross-device moves fail.
            src.rename(dst)
            moved += 1
    except (OSError, ValueError) as exc:
        raise ValueError(
            f"Stopped after {moved}/{len(moves)} moves: {exc}. "
            "No automatic rollback was attempted. Fix the problem, then rerun; "
            "use --undo --apply to return validation sequences to the original test pool."
        ) from exc
    if build_plan(root, data, undo=undo):
        raise ValueError("Post-migration verification failed; rerun a preview to inspect the inventory.")
    print(f"Verified: {target}. Training folders and sequence contents were not modified.")
    return moved


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="Local sim_data root containing train/ (including data_40) and test/.")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help="Path to the published split.json.")
    parser.add_argument("--apply", action="store_true", help="Perform moves; default is preview only.")
    parser.add_argument("--undo", action="store_true", help="Return only validation IDs to the original test pool.")
    args = parser.parse_args(argv)
    try:
        data = load_manifest(args.manifest)
        execute(args.root.expanduser().resolve(strict=True), data, apply=args.apply, undo=args.undo)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
