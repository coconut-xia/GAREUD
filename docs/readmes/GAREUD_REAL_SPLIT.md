# GAREUD-Real Train/Validation Split

This document describes the existing partition used for the GAREUD-Real detection experiments. Of the 82 separately acquired continuous recordings, 81 are assigned in their entirety to either training or validation. The sole exception is R_04, which is divided chronologically into an earlier training segment and a later validation segment. RGB frames and their paired event data follow the same assignment.

## Summary

| Partition | Recording IDs represented | Frames assigned to this partition | Share of frames |
|---|---:|---:|---:|
| Train | 55 | 311,339 | 70.0% |
| Validation (`val`) | 28 | 133,128 | 30.0% |
| Total (unique recordings) | 82 | 444,467 | 100.0% |

Training contains 54 complete recordings plus the earlier R_04 segment; validation contains 27 complete recordings plus the later R_04 segment. R_04 appears in both lists, so the partition-level ID counts overlap by one. The dataset contains 82 unique recordings.

## Allocation Procedure

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

## Training Membership

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

## Validation Membership

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

## Evaluation Scope

All compared models use the same fixed GAREUD-Real partition. Validation is used for per-epoch evaluation, checkpoint selection, early stopping, and reporting the selected checkpoint's detection metrics. The reported 0.902 mAP50 is a validation result. Evaluation covers complete recordings allocated to validation and the later R_04 segment; DJI Air 3 is therefore evaluated across temporal segments of the same recording. At 30 FPS, neighboring frames are correlated, and the frame count is not a count of independent observations.

The processed real-world dataset layout is documented in the root [README](../../README.md).
