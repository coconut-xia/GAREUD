# GAREUD-Sim: Train / Validation / Test Split

Split version: **2026-09-22**. Scope: **original local `data_<id>` sequence names**.

## Definition

Training contains **63 sequences**: the 62 folders in the original directory listing plus **`data_40`**, which the dataset maintainer explicitly assigned to training. Only the original test pool is repartitioned, with an approximate **validation:test = 2:1** ratio by **sequence count**. Each sequence, including all modalities, annotations, and metadata, belongs to exactly one split.

| Split | Sequences | Share of the 88 assigned local sequences |
|---|---:|---:|
| Train | 63 | 71.59% |
| Validation (`val`) | 17 | 19.32% |
| Test | 8 | 9.09% |
| Total | 88 | 100.00% |

The original test pool has 25 sequences. Because 25 is not divisible by 3, the nearest integer allocation is **17 validation / 8 test**, not an exact 2:1 ratio. Frame counts were not supplied; no frame-count ratio is asserted. Adding `data_40` to training does not change the validation/test assignment.

## Sequence Lists

### Train (63)

`data_1` through `data_30`, **`data_40`**, `data_55` through `data_84`, `data_100`, and `data_103`.

Full list: [`train.txt`](../../splits/gareud_sim/train.txt).

### Validation (17)

```text
data_32
data_33
data_36
data_37
data_41
data_42
data_43
data_44
data_45
data_46
data_47
data_48
data_49
data_50
data_51
data_53
data_54
```

Full list: [`val.txt`](../../splits/gareud_sim/val.txt).

### Test (8)

```text
data_31
data_34
data_35
data_38
data_39
data_52
data_101
data_102
```

Full list: [`test.txt`](../../splits/gareud_sim/test.txt).

## Reproducibility

The assignment is generated once from the numerically sorted original test IDs, shuffled using Python's `random.Random(42)`. The first 17 shuffled IDs go to validation and the remaining 8 to test. Published lists are sorted numerically for readability and are the fixed assignment for this split version. Do not reshuffle for individual model runs.

```python
import random

original_test = list(range(31, 40)) + list(range(41, 55)) + [101, 102]
shuffled = sorted(original_test)
random.Random(42).shuffle(shuffled)
n_val = round(2 * len(shuffled) / 3)
val = sorted(shuffled[:n_val])
test = sorted(shuffled[n_val:])
```

[`split.json`](../../splits/gareud_sim/split.json) records the original pool, seed, counts, complete assignments, and limitations. The three text files contain one sequence folder name per line; they are not frame-level YOLO image-path lists.

No scene/trajectory/illumination grouping metadata was supplied for this reassignment. Sequence IDs are disjoint, but scene-level stratification and trajectory-level independence have not been established from the directory listing alone. For new experiments, use `val` for model selection and keep `test` for final evaluation; changing manifests does not retroactively change the split used for earlier reported results.

## Local Migration

The helper operates on the original local layout:

```text
sim_data/
|-- train/     # 63 data_* sequence folders, including data_40
|-- test/      # initially 25 data_* sequence folders
`-- val/       # created when applying the split; may be absent initially
```

**Before running the helper, ensure `train/data_40/` exists and contains the actual sequence data.** Its source location was not supplied, so the helper does not attempt to find or relocate it. It only moves the 17 assigned validation sequences between `test/` and `val/`.

From the repository root, using Python 3.9 or later (standard library only):

```powershell
# Preview only: does not create folders or move data.
python .\tools\split_gareud_sim.py --root "E:\dataset\sim_data"

# Apply: move the 17 validation sequences from test/ to val/.
python .\tools\split_gareud_sim.py --root "E:\dataset\sim_data" --apply

# Preview a return to the 63-train / 25-test layout.
python .\tools\split_gareud_sim.py --root "E:\dataset\sim_data" --undo

# Apply that return, moving only assigned validation sequences back to test/.
python .\tools\split_gareud_sim.py --root "E:\dataset\sim_data" --undo --apply
```

Before moving anything, the script checks the full 63-sequence training inventory and the 25-sequence held-out inventory. Missing sequences, duplicate locations, unexpected sequence directories, file/directory collisions, and linked sequence directories are rejected. It never overwrites a destination or changes sequence contents. It uses directory renames rather than a copy-and-delete fallback, so all split directories must be on the same filesystem.

A repeated run skips sequences already in the correct location. A partially completed run can be resumed after the reported problem is fixed, or reversed with `--undo --apply`. The helper does not remove an empty `val/` directory after undo. Do not modify the dataset concurrently while running the helper.

Expected final inventories: **train=63, val=17, test=8**. Updating this repository does not move data on a local drive or reorganize the Google Drive release.

## Released Names Are Not Remapped

The existing released structure described in [GAREUD_SIM.md](GAREUD_SIM.md) uses `GAREUD_S_000001` through `GAREUD_S_000087`. These manifests instead assign **88 original local `data_<id>` folders**, including IDs above 87 and numbering gaps. A verified original-to-release mapping is not available in the repository. Do not assume `data_41` corresponds to `GAREUD_S_000041`, or apply these lists by numeric suffix to the renamed release. The local inventory correction does not establish that the released archive contains an additional sequence.
