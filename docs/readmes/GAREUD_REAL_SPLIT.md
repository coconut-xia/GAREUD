# GAREUD-Real: reported train/validation protocol and release train/validation/test protocol

The reported experiments use **311,339 training frames and 133,128 validation frames**. The release protocol below keeps training unchanged and divides that original validation pool into new validation and test partitions. The original protocol and recording assignments remain documented below so the reported results remain reproducible.

## Release protocol (2026-10-20)

| Partition | Recording IDs represented | Complete recordings | Additional segment | Frames | Share of all frames |
|---|---:|---:|---|---:|---:|
| Train | 55 | 54 | R_04 earlier, 11,680 frames | 311,339 | 70.05% |
| Validation (`val`) | 8 | 7 | R_04 later, 5,007 frames | 44,223 | 9.95% |
| Test | 20 | 20 | None | 88,905 | 20.00% |
| Total | 82 unique recordings | 81 | Two segments of one recording | 444,467 | 100.00% |

The selection is fixed using recording metadata and frame counts, without using model predictions or accuracy. It targets an approximate 70/10/20 frame ratio while keeping all 27 complete recordings in the old validation pool intact. Both new validation and test contain G2A and A2A viewpoints, indoor and outdoor conditions, varied illuminance, and the three UAV types that have separate recordings: DJI Matrice 350 RTK, DJI Mavic 4 Pro and DJI Avata 2. This is a metadata-based allocation, not a randomized split.

Validation contains the complete recordings **R_14, R_19, R_35, R_43, R_56, R_66 and R_72**, plus the existing later segment of **R_04**. Test contains all 20 remaining complete recordings from the original validation pool. Training membership and frame selection are unchanged.

R_04 is the only recording containing DJI Air 3. Keeping its later segment in validation places the shared-recording exception outside test. Consequently, the test partition contains three UAV types; Air 3 remains available for the separately identified temporal-segment validation analysis. The fixed original training partition already contains all 10–100 lux nighttime recordings, so this repartitioning of old validation does not supply a 10–100 lux nighttime test subset.

### Roles and relation to the reported results

For experiments using the new protocol, use validation for early stopping, checkpoint selection and development; reserve test scoring until these choices are fixed. The previously reported results use the **union of new validation and test**, namely the original 133,128-frame validation pool. Those frames were used for model selection in the original experiments, and the new test designation does not make them an untouched test set for the existing checkpoints. No reported accuracy has been recomputed or relabelled by publishing this allocation.

### Machine-readable membership

- [`split.json`](../../splits/gareud_real/split.json): complete assignments, counts, metadata, protocol roles and R_04 rank ranges.
- [`membership.csv`](../../splits/gareud_real/membership.csv): the same 83 partition entries for 82 unique recording IDs; `reported_experiment_partition` recovers the original train/validation assignment.
- [`test.txt`](../../splits/gareud_real/test.txt): the 20 complete test recording folders, one per line.

R_04 must be selected by its **chronological frame ranks**, not copied as a whole folder into both sets. Ranks are one-based and inclusive in synchronized RGB acquisition order: **1–11,680 for train; 11,681–16,687 for validation**. These ranks are not literal filenames or original camera frame-counter values. Paired event inputs and labels follow the corresponding RGB membership. Recording-level illuminance fields in the manifest should not be interpreted as separate measured ranges for the R_04 segments.

These files define memberships; they do not move dataset files on a local drive or modify the Google Drive releases.

### New validation membership

| Recording | Frames assigned | Allocation | Viewpoint | UAV type |
|---|---:|---|---|---|
| `GAREUD_R_000004` | 5,007 | later contiguous segment | G2A | DJI Air 3 |
| `GAREUD_R_000014` | 8,549 | complete recording | G2A | DJI Matrice 350 RTK |
| `GAREUD_R_000019` | 8,728 | complete recording | G2A | DJI Avata 2 |
| `GAREUD_R_000035` | 10,097 | complete recording | A2A | DJI Avata 2 |
| `GAREUD_R_000043` | 4,558 | complete recording | A2A | DJI Avata 2 |
| `GAREUD_R_000056` | 866 | complete recording | G2A | DJI Avata 2 |
| `GAREUD_R_000066` | 3,665 | complete recording | A2A | DJI Mavic 4 Pro |
| `GAREUD_R_000072` | 2,753 | complete recording | A2A | DJI Avata 2 |

### New test membership

| Recording | Frames assigned | Allocation | Viewpoint | UAV type |
|---|---:|---|---|---|
| `GAREUD_R_000002` | 14,398 | complete recording | G2A | DJI Avata 2 |
| `GAREUD_R_000005` | 4,017 | complete recording | G2A | DJI Avata 2 |
| `GAREUD_R_000007` | 1,752 | complete recording | G2A | DJI Avata 2 |
| `GAREUD_R_000012` | 4,396 | complete recording | G2A | DJI Matrice 350 RTK |
| `GAREUD_R_000020` | 5,341 | complete recording | G2A | DJI Matrice 350 RTK |
| `GAREUD_R_000022` | 10,684 | complete recording | G2A | DJI Matrice 350 RTK |
| `GAREUD_R_000029` | 926 | complete recording | A2A | DJI Avata 2 |
| `GAREUD_R_000030` | 2,488 | complete recording | A2A | DJI Avata 2 |
| `GAREUD_R_000033` | 443 | complete recording | A2A | DJI Avata 2 |
| `GAREUD_R_000034` | 746 | complete recording | A2A | DJI Avata 2 |
| `GAREUD_R_000036` | 1,429 | complete recording | A2A | DJI Avata 2 |
| `GAREUD_R_000042` | 8,797 | complete recording | A2A | DJI Avata 2 |
| `GAREUD_R_000045` | 11,361 | complete recording | A2A | DJI Avata 2 |
| `GAREUD_R_000057` | 1,575 | complete recording | G2A | DJI Avata 2 |
| `GAREUD_R_000060` | 4,382 | complete recording | A2A | DJI Avata 2 |
| `GAREUD_R_000064` | 2,076 | complete recording | A2A | DJI Mavic 4 Pro |
| `GAREUD_R_000070` | 1,867 | complete recording | A2A | DJI Avata 2 |
| `GAREUD_R_000073` | 6,183 | complete recording | A2A | DJI Avata 2 |
| `GAREUD_R_000079` | 4,968 | complete recording | A2A | DJI Mavic 4 Pro |
| `GAREUD_R_000080` | 1,076 | complete recording | A2A | DJI Mavic 4 Pro |

## Frame-count coverage

| Viewpoint | Train | New validation | New test |
|---|---:|---:|---:|
| G2A | 153,654 | 23,150 | 42,163 |
| A2A | 157,685 | 21,073 | 46,742 |

| UAV type | Train | New validation | New test |
|---|---:|---:|---:|
| DJI Air 3 | 11,680 | 5,007 | 0 |
| DJI Avata 2 | 212,377 | 27,002 | 60,364 |
| DJI Matrice 350 RTK | 39,481 | 8,549 | 20,421 |
| DJI Mavic 4 Pro | 47,801 | 3,665 | 8,120 |

## Protocol used for the reported experiments

This document describes the existing partition used for the GAREUD-Real detection experiments. Of the 82 separately acquired continuous recordings, 81 are assigned in their entirety to either training or validation. The sole exception is R_04, which is divided chronologically into an earlier training segment and a later validation segment. RGB frames and their paired event data follow the same assignment.

### Summary

| Partition | Recording IDs represented | Frames assigned to this partition | Share of frames |
|---|---:|---:|---:|
| Train | 55 | 311,339 | 70.0% |
| Validation (`val`) | 28 | 133,128 | 30.0% |
| Total (unique recordings) | 82 | 444,467 | 100.0% |

Training contains 54 complete recordings plus the earlier R_04 segment; validation contains 27 complete recordings plus the later R_04 segment. R_04 appears in both lists, so the partition-level ID counts overlap by one. The dataset contains 82 unique recordings.

### Allocation Procedure

Recording assignment considers acquisition viewpoint, UAV type, scene conditions, measured illuminance range, and sequence duration. Complete recordings are kept intact for all sequences except R_04. The split uses recording and temporal-segment assignment; acquisition date and location are not additional disjointness criteria.

### R_04: chronological segment exception

| Identifier | Value |
|---|---|
| Paper sequence ID | `R_04` |
| Released folder | `GAREUD_R_000004` |
| Server file prefix | `1.4_7_todo` |
| UAV type | DJI Air 3 |

| Partition | Frames assigned | Share of R_04 | Temporal allocation |
|---|---:|---:|---|
| Train | 11,680 | 70.0% | Earlier contiguous segment |
| Validation (`val`) | 5,007 | 30.0% | Later contiguous segment |
| Total | 16,687 | 100.0% | One acquired recording |

R_04 is the only recording containing DJI Air 3. Its earlier segment was acquired with falling snow. The later segment was acquired after snowfall stopped, under lower illuminance, and includes high-speed UAV motion towards and away from the sensing system, changing target depth. The chronological division follows these changes in acquisition conditions and retains DJI Air 3 examples in both partitions. Frames are assigned as two contiguous segments rather than randomly interleaved.

The partition counts reflect the server-side split check reported by the dataset maintainer. The temporal allocation and acquisition-condition descriptions are provided by the maintainer. Counts in the membership tables below refer to frames assigned to the named partition; the complete R_04 recording still contains 16,687 frames.

### Training Membership

| Sequence folder | Frames assigned to training | Allocation |
|---|---:|---|
| `GAREUD_R_000001` | 9,285 | Complete recording |
| `GAREUD_R_000003` | 25,603 | Complete recording |
| `GAREUD_R_000004` | 11,680 | Earlier contiguous segment |
| `GAREUD_R_000006` | 432 | Complete recording |
| `GAREUD_R_000008` | 6,957 | Complete recording |
| `GAREUD_R_000009` | 17,295 | Complete recording |
| `GAREUD_R_000010` | 2,582 | Complete recording |
| `GAREUD_R_000011` | 5,856 | Complete recording |
| `GAREUD_R_000013` | 4,498 | Complete recording |
| `GAREUD_R_000015` | 9,942 | Complete recording |
| `GAREUD_R_000016` | 1,176 | Complete recording |
| `GAREUD_R_000017` | 5,990 | Complete recording |
| `GAREUD_R_000018` | 3,921 | Complete recording |
| `GAREUD_R_000021` | 9,250 | Complete recording |
| `GAREUD_R_000023` | 10,439 | Complete recording |
| `GAREUD_R_000024` | 7,268 | Complete recording |
| `GAREUD_R_000025` | 1,509 | Complete recording |
| `GAREUD_R_000026` | 7,945 | Complete recording |
| `GAREUD_R_000027` | 9,742 | Complete recording |
| `GAREUD_R_000028` | 2,119 | Complete recording |
| `GAREUD_R_000031` | 838 | Complete recording |
| `GAREUD_R_000032` | 2,685 | Complete recording |
| `GAREUD_R_000037` | 10,162 | Complete recording |
| `GAREUD_R_000038` | 412 | Complete recording |
| `GAREUD_R_000039` | 6,707 | Complete recording |
| `GAREUD_R_000040` | 4,278 | Complete recording |
| `GAREUD_R_000041` | 8,964 | Complete recording |
| `GAREUD_R_000044` | 3,987 | Complete recording |
| `GAREUD_R_000046` | 6,170 | Complete recording |
| `GAREUD_R_000047` | 4,349 | Complete recording |
| `GAREUD_R_000048` | 9,911 | Complete recording |
| `GAREUD_R_000049` | 7,742 | Complete recording |
| `GAREUD_R_000050` | 1,127 | Complete recording |
| `GAREUD_R_000051` | 5,792 | Complete recording |
| `GAREUD_R_000052` | 7,646 | Complete recording |
| `GAREUD_R_000053` | 7,529 | Complete recording |
| `GAREUD_R_000054` | 1,022 | Complete recording |
| `GAREUD_R_000055` | 1,262 | Complete recording |
| `GAREUD_R_000058` | 1,475 | Complete recording |
| `GAREUD_R_000059` | 4,441 | Complete recording |
| `GAREUD_R_000061` | 5,312 | Complete recording |
| `GAREUD_R_000062` | 4,386 | Complete recording |
| `GAREUD_R_000063` | 1,886 | Complete recording |
| `GAREUD_R_000065` | 2,771 | Complete recording |
| `GAREUD_R_000067` | 1,863 | Complete recording |
| `GAREUD_R_000068` | 4,937 | Complete recording |
| `GAREUD_R_000069` | 7,544 | Complete recording |
| `GAREUD_R_000071` | 7,600 | Complete recording |
| `GAREUD_R_000074` | 2,852 | Complete recording |
| `GAREUD_R_000075` | 8,505 | Complete recording |
| `GAREUD_R_000076` | 2,433 | Complete recording |
| `GAREUD_R_000077` | 3,025 | Complete recording |
| `GAREUD_R_000078` | 4,225 | Complete recording |
| `GAREUD_R_000081` | 3,436 | Complete recording |
| `GAREUD_R_000082` | 576 | Complete recording |

### Validation Membership

| Sequence folder | Frames assigned to validation | Allocation |
|---|---:|---|
| `GAREUD_R_000002` | 14,398 | Complete recording |
| `GAREUD_R_000004` | 5,007 | Later contiguous segment |
| `GAREUD_R_000005` | 4,017 | Complete recording |
| `GAREUD_R_000007` | 1,752 | Complete recording |
| `GAREUD_R_000012` | 4,396 | Complete recording |
| `GAREUD_R_000014` | 8,549 | Complete recording |
| `GAREUD_R_000019` | 8,728 | Complete recording |
| `GAREUD_R_000020` | 5,341 | Complete recording |
| `GAREUD_R_000022` | 10,684 | Complete recording |
| `GAREUD_R_000029` | 926 | Complete recording |
| `GAREUD_R_000030` | 2,488 | Complete recording |
| `GAREUD_R_000033` | 443 | Complete recording |
| `GAREUD_R_000034` | 746 | Complete recording |
| `GAREUD_R_000035` | 10,097 | Complete recording |
| `GAREUD_R_000036` | 1,429 | Complete recording |
| `GAREUD_R_000042` | 8,797 | Complete recording |
| `GAREUD_R_000043` | 4,558 | Complete recording |
| `GAREUD_R_000045` | 11,361 | Complete recording |
| `GAREUD_R_000056` | 866 | Complete recording |
| `GAREUD_R_000057` | 1,575 | Complete recording |
| `GAREUD_R_000060` | 4,382 | Complete recording |
| `GAREUD_R_000064` | 2,076 | Complete recording |
| `GAREUD_R_000066` | 3,665 | Complete recording |
| `GAREUD_R_000070` | 1,867 | Complete recording |
| `GAREUD_R_000072` | 2,753 | Complete recording |
| `GAREUD_R_000073` | 6,183 | Complete recording |
| `GAREUD_R_000079` | 4,968 | Complete recording |
| `GAREUD_R_000080` | 1,076 | Complete recording |

### Interpretation of the reported metrics

All compared models use the same fixed GAREUD-Real partition. Validation is used for per-epoch evaluation, checkpoint selection, early stopping, and reporting the selected checkpoint's detection metrics. The reported 0.902 mAP50 is a validation result. Evaluation covers complete recordings allocated to validation and the later R_04 segment; DJI Air 3 is therefore evaluated across temporal segments of the same recording. At 30 FPS, neighboring frames are correlated, and the frame count is not a count of independent observations.

The processed real-world dataset layout is documented in the root [README](../../README.md).

