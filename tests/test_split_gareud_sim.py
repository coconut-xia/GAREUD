"""Run from the repository root: python -m unittest discover -s tests -v."""
import contextlib
import copy
import importlib.util
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("split_gareud_sim", REPO / "tools/split_gareud_sim.py")
helper = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(helper)


class SplitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = helper.load_manifest(REPO / "splits/gareud_sim/split.json")
        for split, ids in (("train", self.data["splits"]["train"]), ("test", self.data["original_test"])):
            for name in ids:
                path = self.root / split / name
                (path / "images").mkdir(parents=True)
                (path / "images/000001.png").write_bytes(b"placeholder:" + name.encode())
                (path / "events.h5").write_bytes(b"events:" + name.encode())

    def run_helper(self, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            return helper.execute(self.root, self.data, **kwargs)

    def test_manifest_and_text_lists(self):
        for key, ids in self.data["splits"].items():
            self.assertEqual(ids, (REPO / f"splits/gareud_sim/{key}.txt").read_text().splitlines())
        all_ids = sum(self.data["splits"].values(), [])
        self.assertEqual(len(set(all_ids)), 88)
        self.assertIn("data_40", self.data["splits"]["train"])
        self.assertNotIn("data_40", self.data["original_test"])

    def test_dry_run_has_no_side_effects(self):
        self.assertEqual(self.run_helper(), 17)
        self.assertFalse((self.root / "val").exists())
        self.assertEqual(len(list((self.root / "test").iterdir())), 25)

    def test_apply_preserves_payloads_and_training(self):
        self.assertEqual(self.run_helper(apply=True), 17)
        for split, ids in self.data["splits"].items():
            self.assertEqual(helper.inventory(self.root / split), set(ids))
            for name in ids:
                self.assertEqual((self.root / split / name / "images/000001.png").read_bytes(), b"placeholder:" + name.encode())
                self.assertEqual((self.root / split / name / "events.h5").read_bytes(), b"events:" + name.encode())

    def test_repeated_apply_is_no_op(self):
        self.run_helper(apply=True)
        self.assertEqual(self.run_helper(apply=True), 0)

    def test_undo_and_repeated_undo(self):
        self.run_helper(apply=True)
        self.assertEqual(self.run_helper(undo=True), 17)
        self.assertEqual(len(helper.inventory(self.root / "val")), 17)
        self.assertEqual(self.run_helper(apply=True, undo=True), 17)
        self.assertEqual(helper.inventory(self.root / "test"), set(self.data["original_test"]))
        self.assertEqual(self.run_helper(apply=True, undo=True), 0)

    def test_partial_completion_resumes(self):
        (self.root / "val").mkdir()
        name = self.data["splits"]["val"][0]
        (self.root / "test" / name).rename(self.root / "val" / name)
        self.assertEqual(self.run_helper(apply=True), 16)

    def test_missing_sequence_rejected_before_move(self):
        shutil.rmtree(self.root / "test" / self.data["splits"]["val"][-1])
        with self.assertRaisesRegex(ValueError, "Held-out inventory mismatch"):
            self.run_helper(apply=True)
        self.assertFalse((self.root / "val").exists())

    def test_duplicate_rejected_before_move(self):
        (self.root / "val" / self.data["splits"]["val"][0]).mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "both val and test"):
            self.run_helper(apply=True)
        self.assertEqual(len(helper.inventory(self.root / "test")), 25)

    def test_data_40_cannot_also_be_in_test(self):
        (self.root / "test/data_40").mkdir()
        with self.assertRaisesRegex(ValueError, "unexpected=.*data_40"):
            self.run_helper(apply=True)
        self.assertFalse((self.root / "val").exists())

    def test_missing_training_data_40_rejected(self):
        shutil.rmtree(self.root / "train/data_40")
        with self.assertRaisesRegex(ValueError, "Training inventory mismatch.*data_40"):
            self.run_helper(apply=True)
        self.assertFalse((self.root / "val").exists())

    def test_destination_file_collision(self):
        (self.root / "val").mkdir()
        (self.root / "val" / self.data["splits"]["val"][0]).write_text("existing")
        with self.assertRaisesRegex(ValueError, "file or link"):
            self.run_helper(apply=True)
        self.assertEqual(len(helper.inventory(self.root / "test")), 25)

    def test_training_mismatch(self):
        (self.root / "train/data_1").rename(self.root / "train/data_999")
        with self.assertRaisesRegex(ValueError, "Training inventory mismatch"):
            self.run_helper(apply=True)
        self.assertFalse((self.root / "val").exists())

    def test_path_traversal_in_manifest_rejected(self):
        bad = copy.deepcopy(self.data)
        bad["splits"]["val"][0] = "../elsewhere"
        path = self.root / "bad.json"
        path.write_text(json.dumps(bad))
        with self.assertRaisesRegex(ValueError, "Invalid original sequence ID"):
            helper.load_manifest(path)

    def test_fixed_test_cannot_be_in_val(self):
        (self.root / "val").mkdir()
        name = self.data["splits"]["test"][0]
        (self.root / "test" / name).rename(self.root / "val" / name)
        with self.assertRaisesRegex(ValueError, "Fixed test sequences"):
            self.run_helper(apply=True)

    def test_rename_failure_can_be_resumed(self):
        original = Path.rename
        calls = 0
        def fail_second(src, dst):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise PermissionError("simulated locked directory")
            return original(src, dst)
        with mock.patch.object(Path, "rename", fail_second):
            with self.assertRaisesRegex(ValueError, "Stopped after 1/17"):
                self.run_helper(apply=True)
        self.assertEqual(self.run_helper(apply=True), 16)

    def test_symbolic_split_directory_rejected(self):
        target = self.root / "elsewhere"
        target.mkdir()
        try:
            (self.root / "val").symlink_to(target, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("Creating symlinks is not permitted in this environment")
        with self.assertRaisesRegex(ValueError, "not a file/link"):
            self.run_helper(apply=True)

    def test_missing_root_cli_fails(self):
        with contextlib.redirect_stderr(io.StringIO()):
            code = helper.main(["--root", str(self.root / "missing")])
        self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
