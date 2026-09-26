# GAREUD: Ground-Aerial RGB-Event UAV Dataset

GAREUD is a large-scale RGB-Event UAV detection benchmark for multimodal perception under ground-to-air and air-to-air viewpoints. It provides real-world and synthetic sequences with paired RGB data, event data, annotations, and sequence metadata for UAV detection.

The dataset is built for challenging UAV scenarios where targets are small, fast-moving, and affected by illumination changes, motion blur, background clutter, platform motion, and viewpoint variation. GAREUD supports both ready-to-use RGB-DVS model training and lower-level research on RGB-Event alignment, event representation, and temporal slicing.

![GAREUD overview](assets/gareud_overview.png)

## Project Highlights

- **RGB-Event UAV benchmark:** paired RGB and event data for UAV detection.
- **Real and synthetic subsets:** real recordings for natural sensing conditions and synthetic data for dataset expansion and controlled analysis.
- **Multiple viewpoints:** ground-to-air and air-to-air scenarios.
- **Flexible event data:** processed DVS frames are provided for frame-based use, while h5 event streams support custom temporal slicing.

## Paper Context

GAREUD accompanies the paper **Full-Stack UAV Detection Pipeline from Precise RGB-Event Sensing to Efficient Edge Processing**. The paper studies RGB-Event sensing, dataset construction, multimodal detection, and edge deployment for UAV perception.

This repository currently focuses on dataset release and documentation.

## Download

The dataset releases are available through the following Google Drive folders:

| Version | Description | Link | Documentation |
|---|---|---|---|
| GAREUD-Real-Processed | processed RGB frames, DVS frames, DVS h5 files, labels, and sequence metadata | [Google Drive](https://drive.google.com/drive/folders/1sUcSeesOSm_48kB8NwUI_fUbOhFUaUQ1?usp=drive_link) | This page |
| GAREUD-Real-Raw | Original RGB and event-camera recordings with calibration, parameters, and labels | [Google Drive](https://drive.google.com/drive/folders/1WSdUVY31Msf_oUpoDQa9QQLj8btxbZYy?usp=drive_link) | [README](docs/readmes/UNPROCESSED_RAW_DATA.md) |
| GAREUD-Sim | Synthetic RGB frames, event-frame representations, event streams, labels, and distance metadata | [Google Drive](https://drive.google.com/drive/folders/1ZP1Kh1y9-mLzez1ypwR6dnOkoOyz2dBe?usp=drive_link) | [README](docs/readmes/GAREUD_SIM.md) |

## Dataset Overview

| Subset | Domain | Viewpoints | Resolution | Duration | UAV types | Illumination |
|---|---:|---:|---:|---:|---:|---:|
| GAREUD-Real | Real-world | G2A and A2A | 1280 x 720 raw, 1024 x 576 refined ROI | 4.1 h | 4 | 10-160,000 lux |
| GAREUD-Sim | Synthetic | A2A | 1280 x 720 | 14 min | 2 | Controlled lighting |

The real-world subset is designed for natural sensing conditions, including background clutter, platform motion, vehicle interference, illumination changes, and small UAV targets. The synthetic subset complements the real data with controlled environments and lighting settings for robustness and sensitivity analysis.

The sequence-level train/test split for `GAREUD-Real` is documented in [GAREUD_REAL_SPLIT.md](docs/readmes/GAREUD_REAL_SPLIT.md).

## Refined Real-World Release

This README describes the refined real-world RGB-DVS release. It is derived from the original recordings:

- RGB frames are stereo-rectified, manually shifted, and cropped to a common ROI.
- Event-camera coordinates are stereo-rectified and cropped to the same ROI.
- Event timestamps, polarities, and external trigger timestamps are preserved.
- DVS frame images are provided for quick frame-pair browsing and image-based experiments.
- Each sequence stores one continuous processed DVS h5 file, not one h5 file per RGB frame.

## Dataset Layout

The following layout describes the **Synchronized processed data** release. The unprocessed raw data folder keeps the original recordings, raw h5 files, calibration files, parameters, and labels, while the synchronized processed release uses the refined structure below. Its dataset root contains one folder per recording sequence:

```text
GAREUD_R/
|-- README.md
|-- GAREUD_R_000001/
|   |-- rgb_todo/
|   |   |-- 1415.670021592.jpg
|   |   |-- 1415.703367568.jpg
|   |   |-- 1415.736713136.jpg
|   |   `-- ...
|   |-- dvs_frame/
|   |   |-- 001_1415.670021592.jpg
|   |   |-- 002_1415.703367568.jpg
|   |   |-- 003_1415.736713136.jpg
|   |   `-- ...
|   |-- dvs_h5/
|   |   `-- 20260104_144809.h5
|   |-- labels.txt
|   `-- sequence_info.txt
|-- GAREUD_R_000002/
|   `-- ...
|-- ...
|-- GAREUD_R_000082/
|   `-- ...
|-- process_summary.json
|-- all_process_reports.json
|-- process_gareud_todo.py
|-- gareud_dataset_slicer.py
|-- run_gareud_slicer_gui.bat
`-- dvs_frame_copy_check.csv
```

Folder names use zero-padded sequence IDs:

```text
GAREUD_R_000001, GAREUD_R_000002, ..., GAREUD_R_000082
```

In the paper table, `R_01` corresponds to `GAREUD_R_000001`, `R_02` corresponds to `GAREUD_R_000002`, and so on.

### Image-plane speed ranges

The [per-sequence image-plane speed table](docs/readmes/GAREUD_REAL_IMAGE_PLANE_SPEED.md) reports **pixel-speed intervals (minimum–maximum, pixels/s)** for all 82 real-world sequences, with three decimal places. Speeds are computed from adjacent annotated bounding-box centers at **30 fps** in the **1024 × 576** image coordinate system. Missing-box pairs are excluded; actual zero displacements and extreme values are retained. These measurements include camera motion and annotation variation and are distinct from physical flight speed in m/s.

The analysis contains **379,392 valid adjacent-frame speeds** with an overall range of **0.000–3433.866 pixels/s**. The [CSV](docs/metadata/gareud_real_image_plane_speed_ranges.csv) records per-sequence ranges, sample counts, and extreme-frame filenames. The [paper LaTeX table](docs/metadata/sequence_metadata_with_image_plane_speed.tex) places each image-plane speed interval immediately after its physical flight speed in the scenario-label text.

## Sequence-Level Files

Each `GAREUD_R_xxxxxx/` folder contains the following files and directories.

Required sequence contents:

| Path | Description |
|---|---|
| `rgb_todo/` | Rectified, shifted, and ROI-cropped RGB frames |
| `dvs_frame/` | Pre-rendered DVS frame images aligned with RGB frame order |
| `dvs_h5/` | One continuous rectified and ROI-cropped event-stream h5 file |
| `labels.txt` | Sequence-level object annotations |
| `sequence_info.txt` | Human-readable sequence metadata |

Repository/helper files at the dataset root include the processing script, slicing tool, processing summaries, and the DVS-frame copy check table. They are included to document and reproduce the dataset construction workflow, but the main released data are the sequence folders.

### `rgb_todo/`

Processed RGB frames.

```text
rgb_todo/
  1415.670021592.jpg
  1415.703367568.jpg
  ...
```

Properties:

| Item | Description |
|---|---|
| File name | `<timestamp>.jpg` |
| Timestamp unit | seconds.nanoseconds-style string inherited from RGB acquisition |
| Image size | ROI size from `params.json`, typically `1024 x 576` |
| Color format | Standard JPEG image, read by OpenCV as BGR |

RGB processing steps:

1. Stereo rectification using the RGB camera homography.
2. Manual RGB translation using `offset_x` and `offset_y`.
3. ROI crop using `crop_x`, `crop_y`, `crop_w`, and `crop_h`.

The file stem is used as the RGB frame ID. For example:

```text
rgb_todo/1415.670021592.jpg
```

has frame stem:

```text
1415.670021592
```

### `dvs_h5/`

Processed event-camera data for the whole sequence.

Each sequence contains one h5 file:

```text
dvs_h5/
  20260104_144809.h5
```

The h5 file contains all original `CD/events` after coordinate rectification and ROI cropping. It is a continuous event stream. It is not split into per-frame h5 files.

Important points:

- All raw `CD/events` are processed.
- Events outside the ROI after rectification are discarded.
- Event timestamps `t` are preserved.
- Event polarities `p` are preserved.
- `EXT_TRIGGER/events` is copied unchanged from the raw h5.
- Trigger pairs are not used to filter the event stream; they are provided for synchronization.

### `dvs_frame/`

Pre-rendered DVS frame images aligned with the RGB frame order.

```text
dvs_frame/
  001_1415.670021592.jpg
  002_1415.703367568.jpg
  003_1415.736713136.jpg
  ...
```

Properties:

| Item | Description |
|---|---|
| File name | `<frame_index>_<timestamp>.jpg` |
| `frame_index` | 1-based RGB frame index, zero-padded in the filename |
| `timestamp` | RGB frame stem corresponding to the paired RGB image |
| Image size | Same ROI size as the processed RGB images, typically `1024 x 576` |
| Purpose | Quick visual inspection, RGB-DVS pair browsing, and image-based baseline experiments |

For example:

```text
rgb_todo/1415.670021592.jpg
dvs_frame/001_1415.670021592.jpg
```

refer to the same RGB frame timestamp. The `dvs_frame/` images are generated visualizations of event slices. They are convenient for browsing, annotation checks, and frame-based model input. For exact event timestamps, polarities, trigger information, or custom temporal windows, use the continuous h5 file in `dvs_h5/`.

### `labels.txt`

Sequence-level object annotations.

Typical object annotation line:

```text
<timestamp> <class_id> <x_center> <y_center> <width> <height>
```

Example:

```text
1415.670021592 3 0.518131 0.381939 0.025136 0.026980
```

Fields:

| Field | Description |
|---|---|
| `timestamp` | RGB frame stem |
| `class_id` | Object class index |
| `x_center` | YOLO-normalized bounding-box center x |
| `y_center` | YOLO-normalized bounding-box center y |
| `width` | YOLO-normalized bounding-box width |
| `height` | YOLO-normalized bounding-box height |

Coordinates are normalized relative to the processed RGB image size in `rgb_todo/`.

Some lines may contain only a timestamp. Such lines indicate RGB frames without object annotations.

Class-name lines may also appear in the file:

```text
classes DJI M350RTK
classes DJI Mavic 4 Pro
classes DJI Air3
classes DJI Avata2
```

### `sequence_info.txt`

Metadata file recording sequence-level labels and acquisition conditions.

Example:

```text
viewpoint: G2A
frame_count: 9285
target UAV: DJI Avata 2
flight_speed: flight speed 5-16 m/s
illumination: 5,000-15,000 lux
scene_conditions: Vehicle interference; cloudy afternoon; hovering.
```

Fields:

| Field | Description |
|---|---|
| `viewpoint` | Acquisition viewpoint category, e.g. `G2A` or `A2A` |
| `frame_count` | Number of processed RGB frames |
| `target UAV` | UAV model in the sequence |
| `flight_speed` | Approximate flight speed range |
| `illumination` | Measured or estimated illumination range |
| `scene_conditions` | Background, weather, interference, and motion notes |

### Optional Build Metadata: `params.json`

Per-sequence alignment and ROI parameters used during dataset construction. These parameters may be distributed with the construction scripts or processing reports. They describe how the released RGB images and event coordinates were produced.

Example:

```json
{
  "offset_x": 2,
  "offset_y": -4,
  "crop_x": 184,
  "crop_y": 142,
  "crop_w": 1024,
  "crop_h": 576
}
```

Fields:

| Field | Description |
|---|---|
| `offset_x` | Horizontal shift applied to rectified RGB before cropping |
| `offset_y` | Vertical shift applied to rectified RGB before cropping |
| `crop_x` | ROI top-left x coordinate in the rectified common canvas |
| `crop_y` | ROI top-left y coordinate in the rectified common canvas |
| `crop_w` | ROI width |
| `crop_h` | ROI height |

The event stream is not shifted by `offset_x` or `offset_y`. Event coordinates are rectified using the event-camera homography and then cropped by the ROI.

### Optional Build Metadata: `calibration_info.txt`

Stereo calibration and alignment record for the sequence. This file is used during construction and may be included with build metadata.

It contains:

- RGB camera intrinsic matrix `K1`
- event-camera intrinsic matrix `K2`
- event-camera rectification rotation `R2`
- translation vector `t2`
- manual RGB alignment offsets
- ROI origin and size

### Build Report: `process_report.json` / `all_process_reports.json`

Processing summary generated during dataset construction. Per-sequence reports may appear as `process_report.json`; the dataset root can also contain an aggregated `all_process_reports.json` and `process_summary.json`.

Typical fields:

| Field | Description |
|---|---|
| `sequence` | Sequence folder name |
| `raw_h5` | Source raw h5 path used during processing |
| `output` | Output sequence folder |
| `frames_total` | Number of source RGB frames |
| `frames_requested` | Number of RGB frames processed |
| `written_rgb` | Number of RGB frames written during this run |
| `dvs_events_written` | Number of processed events retained in the output h5 |
| `rgb_output` | RGB output subdirectory |
| `dvs_output` | DVS h5 output path relative to the sequence folder |
| `elapsed_s` | Processing time in seconds |

## H5 File Format

This section describes the content of each file in `dvs_h5/`.

### H5 Group Structure

Example:

```text
20260104_144809.h5
  CD/
    events
  EXT_TRIGGER/
    events
  RGB/
    frame_stems
```

### Root Attributes

The output h5 preserves original Prophesee metadata where possible. Geometry-related attributes are updated to the processed ROI size.

Example attributes from one sequence:

```text
format: EVT3;height=576;width=1024
geometry: 1024x576
sensor_name: IMX636
sensor_generation: 4.2
generation: 4.2
serial_number: 00050890
date: 2026-01-04 14:48:09
event_window: all_cd_events_rectified_roi_cropped
rgb_frame_count: 9285
```

Common attributes:

| Attribute | Description |
|---|---|
| `format` | Event data format and processed geometry, e.g. `EVT3;height=576;width=1024` |
| `geometry` | Processed event plane size, e.g. `1024x576` |
| `sensor_name` | Event sensor name, e.g. `IMX636` |
| `sensor_generation` / `generation` | Sensor generation |
| `serial_number` | Event-camera serial number |
| `date` | Original recording date |
| `camera_integrator_name` | Camera integrator metadata |
| `integrator_name` | Integrator metadata |
| `plugin_integrator_name` | Plugin integrator metadata |
| `system_ID` | System identifier from the original h5 |
| `version` | Original h5 version metadata |
| `event_window` | Processing note. Current value: `all_cd_events_rectified_roi_cropped` |
| `rgb_frame_count` | Number of processed RGB frames in `rgb_todo/` |
| `source_h5` | Source h5 path used during processing |

### `CD/events`

Main event stream after rectification and ROI cropping.

HDF5 path:

```text
CD/events
```

Compound dtype:

```text
{
  names:   ["x", "y", "p", "t"],
  formats: ["<u2", "<u2", "<i2", "<i8"],
  offsets: [0, 2, 4, 8],
  itemsize: 16
}
```

Field definitions:

| Field | dtype | Unit | Description |
|---|---:|---|---|
| `x` | unsigned 16-bit integer | pixel | Rectified and ROI-cropped event x coordinate |
| `y` | unsigned 16-bit integer | pixel | Rectified and ROI-cropped event y coordinate |
| `p` | signed 16-bit integer | binary | Event polarity, `0` or `1` |
| `t` | signed 64-bit integer | microseconds | Event timestamp |

Coordinate convention:

- `x` is in `[0, width)`.
- `y` is in `[0, height)`.
- `width` and `height` are given by the h5 `geometry` attribute.
- For `geometry = 1024x576`, valid coordinates are `0 <= x < 1024` and `0 <= y < 576`.

Processing convention:

- Raw event coordinates are transformed by the event-camera rectification homography.
- The ROI origin is subtracted from the transformed coordinates.
- Events outside the ROI are discarded.
- `p` and `t` are not modified.
- The event stream remains time-ordered.

### `EXT_TRIGGER/events`

External trigger stream.

HDF5 path:

```text
EXT_TRIGGER/events
```

Compound dtype:

```text
{
  names:   ["p", "t", "id"],
  formats: ["<i2", "<i8", "<i2"],
  offsets: [0, 8, 16],
  itemsize: 24
}
```

Field definitions:

| Field | dtype | Unit | Description |
|---|---:|---|---|
| `p` | signed 16-bit integer | binary | Trigger level |
| `t` | signed 64-bit integer | microseconds | Trigger timestamp |
| `id` | signed 16-bit integer | channel | Trigger channel ID |

Trigger polarity convention:

| Trigger `p` | Meaning |
|---:|---|
| `0` | RGB exposure start |
| `1` | RGB exposure end |

A valid RGB exposure is represented by a `0 -> 1` pair. Some recordings may contain a leading useless `p=1` trigger before the first valid `p=0`. This leading trigger is retained because the trigger stream is copied unchanged.

Important: `CD/events` is not filtered by trigger pairs. Users can use `EXT_TRIGGER/events` to slice events around RGB frames according to their own temporal-window definition.

### `RGB/frame_stems`

Processed RGB frame stems stored as UTF-8 strings.

HDF5 path:

```text
RGB/frame_stems
```

Example values:

```text
1415.670021592
1415.703367568
1415.736713136
...
```

Each stem maps to:

```text
rgb_todo/<frame_stem>.jpg
```

The order of `RGB/frame_stems` follows the sorted RGB frame order.

The same order is used by `dvs_frame/`. In the released folder, the DVS frame image corresponding to `RGB/frame_stems[i]` has a filename beginning with `i + 1`, for example `001_...jpg`, `002_...jpg`, and so on.

## Synchronization

The dataset provides three time-related signals:

1. RGB frame file stems, e.g. `1415.670021592`
2. Event timestamps in `CD/events/t`
3. DVS frame image filenames, e.g. `001_1415.670021592.jpg`
4. Trigger timestamps in `EXT_TRIGGER/events/t`

All event and trigger timestamps are in microseconds. RGB file stems are the RGB capture timestamps and are synchronized to the same acquisition system.

For frame-level event slicing:

1. Sort RGB frames by file stem.
2. Read `EXT_TRIGGER/events`.
3. Ignore any leading `p=1` without a preceding `p=0`.
4. Pair each valid `p=0` with the following `p=1`.
5. The first valid `0 -> 1` pair corresponds to the first RGB frame.

Depending on the task, users may choose different event windows, for example:

- exposure-only window: `[p0_i, p1_i]`
- frame-interval window: `[p0_i, p0_{i+1})`
- symmetric window around an RGB timestamp

The released h5 keeps the continuous corrected event stream so that users can choose the temporal slicing strategy.

For ordinary frame-pair browsing, use `rgb_todo/<timestamp>.jpg` together with `dvs_frame/<frame_index>_<timestamp>.jpg`. For temporal research or re-slicing, use `dvs_h5/*.h5` and the trigger stream.

## Reading Example

```python
from pathlib import Path

import cv2
import h5py

seq = Path("GAREUD_R/GAREUD_R_000001")

# Read RGB frame
rgb_path = seq / "rgb_todo" / "1415.670021592.jpg"
rgb = cv2.imread(str(rgb_path))
print("RGB shape:", rgb.shape)

# Read matching DVS frame image
dvs_frame_path = seq / "dvs_frame" / "001_1415.670021592.jpg"
dvs_frame = cv2.imread(str(dvs_frame_path))
print("DVS frame shape:", dvs_frame.shape)

# Read DVS h5
h5_path = next((seq / "dvs_h5").glob("*.h5"))
with h5py.File(h5_path, "r") as f:
    print("Attributes:")
    for key, value in f.attrs.items():
        print(key, value)

    events = f["CD/events"]
    triggers = f["EXT_TRIGGER/events"]
    frame_stems = [
        s.decode("utf-8") if isinstance(s, bytes) else str(s)
        for s in f["RGB/frame_stems"][:]
    ]

    print("Event dtype:", events.dtype)
    print("Event count:", events.shape[0])
    print("Trigger dtype:", triggers.dtype)
    print("Trigger count:", triggers.shape[0])
    print("First RGB stems:", frame_stems[:5])

    # Load a small event slice
    ev = events[:1000]
    x = ev["x"]
    y = ev["y"]
    p = ev["p"]
    t = ev["t"]
```

## Example: Slice Events by RGB Exposure Trigger

```python
import h5py
import numpy as np

def exposure_pairs(trigger_events):
    ordered = trigger_events[np.argsort(trigger_events["t"])]
    pairs = []
    start = None
    for item in ordered:
        if int(item["p"]) == 0:
            start = int(item["t"])
        elif int(item["p"]) == 1 and start is not None:
            pairs.append((start, int(item["t"])))
            start = None
    return pairs

with h5py.File("GAREUD_R/GAREUD_R_000001/dvs_h5/20260104_144809.h5", "r") as f:
    events = f["CD/events"]
    triggers = f["EXT_TRIGGER/events"][:]
    pairs = exposure_pairs(triggers)

    # Events during the first RGB exposure.
    t0, t1 = pairs[0]
    t = events["t"][:]
    left = np.searchsorted(t, t0, side="left")
    right = np.searchsorted(t, t1, side="right")
    first_exposure_events = events[left:right]
```

## Suggested Citation

If you use GAREUD, please cite the accompanying dataset paper:

```bibtex
@article{xia2026gareud,
  title   = {Full-Stack UAV Detection Pipeline from Precise RGB-Event Sensing to Efficient Edge Processing},
  author  = {Xia, Haoji and Liu, Siying and Jin, Jiaqi and Wang, Sihan and Huang, Tong and Han, Xujie and Wang, Zikai and Zhong, Yuxing and Zheng, Hanle and Cheng, Chen and Guo, Hao and Deng, Lei},
  journal = {To appear},
  year    = {2026}
}
```
