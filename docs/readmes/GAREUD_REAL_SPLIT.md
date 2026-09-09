# GAREUD-Real Train/Test Split

This file records the sequence-level train/test split for the real-world GAREUD release. All entries use the released sequence-folder names.

## Summary

| Split | Sequences | Images | Share |
|---|---:|---:|---:|
| Train | 54 | 299,659 | 67.4% |
| Test | 28 | 144,808 | 32.6% |
| Total | 82 | 444,467 | 100.0% |

## Training Sequences

| Sequence folder | Images | Sequence folder | Images | Sequence folder | Images |
|---|---:|---|---:|---|---:|
| `GAREUD_R_000001` | 9,285 | `GAREUD_R_000028` | 2,119 | `GAREUD_R_000055` | 1,262 |
| `GAREUD_R_000003` | 25,603 | `GAREUD_R_000031` | 838 | `GAREUD_R_000058` | 1,475 |
| `GAREUD_R_000006` | 432 | `GAREUD_R_000032` | 2,685 | `GAREUD_R_000059` | 4,441 |
| `GAREUD_R_000008` | 6,957 | `GAREUD_R_000037` | 10,162 | `GAREUD_R_000061` | 5,312 |
| `GAREUD_R_000009` | 17,295 | `GAREUD_R_000038` | 412 | `GAREUD_R_000062` | 4,386 |
| `GAREUD_R_000010` | 2,582 | `GAREUD_R_000039` | 6,707 | `GAREUD_R_000063` | 1,886 |
| `GAREUD_R_000011` | 5,856 | `GAREUD_R_000040` | 4,278 | `GAREUD_R_000065` | 2,771 |
| `GAREUD_R_000013` | 4,498 | `GAREUD_R_000041` | 8,964 | `GAREUD_R_000067` | 1,863 |
| `GAREUD_R_000015` | 9,942 | `GAREUD_R_000044` | 3,987 | `GAREUD_R_000068` | 4,937 |
| `GAREUD_R_000016` | 1,176 | `GAREUD_R_000046` | 6,170 | `GAREUD_R_000069` | 7,544 |
| `GAREUD_R_000017` | 5,990 | `GAREUD_R_000047` | 4,349 | `GAREUD_R_000071` | 7,600 |
| `GAREUD_R_000018` | 3,921 | `GAREUD_R_000048` | 9,911 | `GAREUD_R_000074` | 2,852 |
| `GAREUD_R_000021` | 9,250 | `GAREUD_R_000049` | 7,742 | `GAREUD_R_000075` | 8,505 |
| `GAREUD_R_000023` | 10,439 | `GAREUD_R_000050` | 1,127 | `GAREUD_R_000076` | 2,433 |
| `GAREUD_R_000024` | 7,268 | `GAREUD_R_000051` | 5,792 | `GAREUD_R_000077` | 3,025 |
| `GAREUD_R_000025` | 1,509 | `GAREUD_R_000052` | 7,646 | `GAREUD_R_000078` | 4,225 |
| `GAREUD_R_000026` | 7,945 | `GAREUD_R_000053` | 7,529 | `GAREUD_R_000081` | 3,436 |
| `GAREUD_R_000027` | 9,742 | `GAREUD_R_000054` | 1,022 | `GAREUD_R_000082` | 576 |

## Val Sequences

| Sequence folder | Images | Sequence folder | Images |
|---|---:|---|---:|
| `GAREUD_R_000002` | 14,398 | `GAREUD_R_000036` | 1,429 |
| `GAREUD_R_000004` | 16,687 | `GAREUD_R_000042` | 8,797 |
| `GAREUD_R_000005` | 4,017 | `GAREUD_R_000043` | 4,558 |
| `GAREUD_R_000007` | 1,752 | `GAREUD_R_000045` | 11,361 |
| `GAREUD_R_000012` | 4,396 | `GAREUD_R_000056` | 866 |
| `GAREUD_R_000014` | 8,549 | `GAREUD_R_000057` | 1,575 |
| `GAREUD_R_000019` | 8,728 | `GAREUD_R_000060` | 4,382 |
| `GAREUD_R_000020` | 5,341 | `GAREUD_R_000064` | 2,076 |
| `GAREUD_R_000022` | 10,684 | `GAREUD_R_000066` | 3,665 |
| `GAREUD_R_000029` | 926 | `GAREUD_R_000070` | 1,867 |
| `GAREUD_R_000030` | 2,488 | `GAREUD_R_000072` | 2,753 |
| `GAREUD_R_000033` | 443 | `GAREUD_R_000073` | 6,183 |
| `GAREUD_R_000034` | 746 | `GAREUD_R_000079` | 4,968 |
| `GAREUD_R_000035` | 10,097 | `GAREUD_R_000080` | 1,076 |

## Notes

- Each sequence folder is assigned entirely to one split.
- `GAREUD_R_000004` is split 5:5 for train/validation because it is the only sequence containing DJI Air 3 data.
- Image counts are recorded per released sequence folder.
- The processed real-world dataset layout is documented in the root README.
