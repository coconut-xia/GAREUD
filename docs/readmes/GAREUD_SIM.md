# GAREUD-Sim

This document describes the **GAREUD-Sim** subset. GAREUD-Sim is a synthetic RGB-Event UAV dataset generated for controlled evaluation of RGB-Event UAV detection. It provides RGB frames, event-frame representations, event streams, labels, and distance metadata.

## Download

| Version | Link |
|---|---|
| GAREUD-Sim | [Google Drive](https://drive.google.com/drive/folders/1ZP1Kh1y9-mLzez1ypwR6dnOkoOyz2dBe?usp=drive_link) |

## Folder Layout

The released folder contains one directory per simulated sequence. Zip archives may also be present in local storage, but the usable dataset structure is the extracted sequence folders:

```text
GAREUD_S/
|-- GAREUD_S_000001/
|   |-- images/
|   |   |-- 000001.png
|   |   |-- 000002.png
|   |   `-- ...
|   |-- event_frames/
|   |   |-- 000001.png
|   |   |-- 000002.png
|   |   `-- ...
|   |-- events.h5
|   |-- labels.txt
|   `-- distances.txt
|-- GAREUD_S_000002/
|   `-- ...
|-- ...
`-- GAREUD_S_000087/
    `-- ...
```

Folder names use zero-padded sequence IDs:

```text
GAREUD_S_000001, GAREUD_S_000002, ..., GAREUD_S_000087
```

## Train / Validation / Test Split

The local split dated **2026-09-22** contains **63 training sequences**, including **`data_40`** as clarified by the dataset maintainer, and divides the original **25 test sequences** into **17 validation sequences** and **8 test sequences**. The requested validation:test ratio is approximately **2:1**, measured by sequence count. Whole sequences remain intact.

See [GAREUD_SIM_SPLIT.md](GAREUD_SIM_SPLIT.md) for the complete sequence lists, reproducible assignment rule, and local migration commands. Machine-readable lists are in [`splits/gareud_sim/`](../../splits/gareud_sim/).

**Naming scope:** these manifests assign 88 original local `data_<id>` folders. The existing `GAREUD_S_xxxxxx` release layout above is unchanged. A verified mapping between the two naming schemes is not available in this repository; do not infer one from the numeric suffixes or treat the local count as a verified count of the released archive.

## Sequence-Level Files

Each `GAREUD_S_xxxxxx/` folder contains:

| Path | Description |
|---|---|
| `images/` | Synthetic RGB frames. File names are frame IDs such as `000001.png`. |
| `event_frames/` | Frame-like event representations paired with RGB frames. |
| `events.h5` | Synthetic event stream. |
| `labels.txt` | Bounding-box annotations for each RGB frame. |
| `distances.txt` | Per-frame distance and relative-position metadata. |

## `images/`

The `images/` directory stores synthetic RGB frames:

```text
images/
  000001.png
  000002.png
  000003.png
  ...
```

The file stem is the frame ID and is shared by `event_frames/`, `labels.txt`, and `distances.txt`.

## `event_frames/`

The `event_frames/` directory stores frame-like event representations:

```text
event_frames/
  000001.png
  000002.png
  000003.png
  ...
```

Each event-frame image is paired with the RGB image with the same frame ID.

## `events.h5`

The synthetic event stream is stored in `events.h5`.

Observed h5 layout:

```text
events.h5
  events/
    p
    t
    x
    y
  ms_to_idx
  t_offset
```

Fields:

| Path | Description |
|---|---|
| `events/x` | Event x coordinate |
| `events/y` | Event y coordinate |
| `events/p` | Event polarity |
| `events/t` | Event timestamp |
| `ms_to_idx` | Millisecond-to-event-index lookup table |
| `t_offset` | Timestamp offset |

## `labels.txt`

The label file uses one annotation per line:

```text
frame_id class_id x_center y_center width height
```

Example:

```text
000001 0 0.494531 0.491667 0.012500 0.008333
```

Bounding boxes use YOLO-normalized coordinates.

## `distances.txt`

The distance file stores per-frame range and relative-position metadata.

Example:

```text
000001  Distance: 8.033m  RelPos: X=-0.10 Y=0.03 Z=0.05
000002  Distance: 8.039m  RelPos: X=-0.13 Y=0.04 Z=0.05
```

Fields:

| Field | Description |
|---|---|
| Frame ID | Frame identifier matching `images/` and `event_frames/` |
| `Distance` | Distance between observer and target UAV, in meters |
| `RelPos` | Relative target position in the simulated coordinate frame |

## Notes

GAREUD-Sim is intended for controlled evaluation, robustness analysis, and comparison with the real-world subset. The real-world subset should be used when evaluating natural sensing artifacts such as illumination changes, background clutter, platform motion, and real sensor noise.
