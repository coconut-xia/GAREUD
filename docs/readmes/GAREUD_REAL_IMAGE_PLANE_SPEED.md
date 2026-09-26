# GAREUD-Real: image-plane speed ranges

This table reports **pixel-speed intervals (minimum–maximum, pixels/s)** for each of the 82 real-world sequences. These are image-plane speeds of the annotated UAV bounding-box center, not physical flight speeds in m/s. All speed values are displayed to **three decimal places**.

## Definition and calculation

For adjacent RGB frames with normalized bounding-box centers `(cx_previous, cy_previous)` and `(cx_current, cy_current)`, use the fixed **1024 × 576** image coordinate system and **30 fps**:

```text
dt = 1/30 s = 33.333333... ms
dx = 1024 * (cx_current - cx_previous)
dy =  576 * (cy_current - cy_previous)
image_plane_speed = sqrt(dx*dx + dy*dy) / dt  # pixels/s
```

The interval is the minimum and maximum over valid consecutive-frame speeds within one sequence. It is not a confidence interval, a percentile interval, or a conversion of physical flight speed. Extrema were computed before rounding.

RGB filenames are ordered by their numeric timestamps. The calculation uses the fixed `1/30 s` interval, not the filename timestamp difference. Each valid pair contains exactly one box in each frame and the same class ID. The labels contain no track IDs, so continuity of this single target is assumed. A pair with a missing box is excluded; gaps are not bridged and missing values are not treated as zero. True zero center displacements are retained. No smoothing, outlier removal, or camera-motion compensation was applied.

Across **444,467 RGB frames**, the analysis covers **444,385 consecutive-frame pairs**: **379,392 valid speeds** and **64,993 excluded pairs due to missing boxes**. There are **118 zero-speed pairs** in **44 sequences**. The overall range is **0.000–3433.866 pixels/s**. Camera motion and annotation variation contribute to these image-plane measurements; zero image-plane speed does not establish zero physical UAV velocity.

## Files

- [CSV with all ranges and extreme-frame filenames](../metadata/gareud_real_image_plane_speed_ranges.csv)
- [Paper LaTeX table](../metadata/sequence_metadata_with_image_plane_speed.tex): adds `image-plane speed ... pixels/s` immediately after `physical flight speed ... m/s` in every scenario-label cell. The supplied physical-speed metadata are preserved.
- [Provenance and verification](../metadata/image_plane_speed_provenance.json)
- [LaTeX update script](../../tools/update_sequence_speed_latex.py), using only the Python standard library.

The LaTeX fragment retains the paper's existing six-column `longtable` layout. It uses the existing `C`/`L` column types and `TableHead`/`TableStripe` color definitions; it requires the paper preamble (`longtable`, `array`, `booktabs`, and table-color support). No standalone LaTeX engine was available for compilation in the editing environment; all 82 row mappings, RGB counts, ranges, and preserved cell contents were checked programmatically.

To apply the same additions to the supplied original table:

```bash
python tools/update_sequence_speed_latex.py --input original_sequence_table.tex --output updated_sequence_table.tex
```

## Per-sequence pixel-speed intervals

`R_01` corresponds to `GAREUD_R_000001`, and likewise for all other rows. Counts refer to valid adjacent-frame pairs, not RGB frame totals. The CSV includes both zero-speed counts and the first frame pair attaining each extreme.

| Paper ID | Sequence | Image-plane speed range (pixels/s) | Valid pairs | Zero-speed pairs |
|---|---|---:|---:|---:|
| R_01 | GAREUD_R_000001 | 0.000–954.143 | 8640 | 4 |
| R_02 | GAREUD_R_000002 | 0.000–807.269 | 13937 | 8 |
| R_03 | GAREUD_R_000003 | 0.000–892.830 | 23924 | 4 |
| R_04 | GAREUD_R_000004 | 0.000–1342.212 | 15967 | 29 |
| R_05 | GAREUD_R_000005 | 2.943–625.111 | 3879 | 0 |
| R_06 | GAREUD_R_000006 | 0.000–491.403 | 303 | 1 |
| R_07 | GAREUD_R_000007 | 0.000–515.210 | 1556 | 1 |
| R_08 | GAREUD_R_000008 | 0.000–1059.566 | 6753 | 2 |
| R_09 | GAREUD_R_000009 | 0.000–992.094 | 16873 | 7 |
| R_10 | GAREUD_R_000010 | 4.018–1423.813 | 2451 | 0 |
| R_11 | GAREUD_R_000011 | 0.000–991.049 | 5853 | 1 |
| R_12 | GAREUD_R_000012 | 3.644–1109.783 | 4395 | 0 |
| R_13 | GAREUD_R_000013 | 0.000–2329.969 | 4408 | 1 |
| R_14 | GAREUD_R_000014 | 0.000–1011.857 | 8334 | 1 |
| R_15 | GAREUD_R_000015 | 0.000–840.663 | 8814 | 1 |
| R_16 | GAREUD_R_000016 | 3.002–267.754 | 1116 | 0 |
| R_17 | GAREUD_R_000017 | 0.000–445.343 | 5656 | 1 |
| R_18 | GAREUD_R_000018 | 0.000–829.274 | 3677 | 1 |
| R_19 | GAREUD_R_000019 | 0.000–1219.210 | 8233 | 2 |
| R_20 | GAREUD_R_000020 | 0.035–369.169 | 5340 | 0 |
| R_21 | GAREUD_R_000021 | 0.277–681.703 | 9104 | 0 |
| R_22 | GAREUD_R_000022 | 0.000–547.006 | 10373 | 1 |
| R_23 | GAREUD_R_000023 | 0.000–1103.844 | 10166 | 2 |
| R_24 | GAREUD_R_000024 | 0.000–894.228 | 6906 | 1 |
| R_25 | GAREUD_R_000025 | 0.000–499.887 | 1234 | 4 |
| R_26 | GAREUD_R_000026 | 1.182–1072.975 | 6710 | 0 |
| R_27 | GAREUD_R_000027 | 0.000–809.640 | 9286 | 1 |
| R_28 | GAREUD_R_000028 | 4.971–979.739 | 1649 | 0 |
| R_29 | GAREUD_R_000029 | 18.073–1154.448 | 285 | 0 |
| R_30 | GAREUD_R_000030 | 5.061–1098.189 | 2328 | 0 |
| R_31 | GAREUD_R_000031 | 2.001–986.010 | 792 | 0 |
| R_32 | GAREUD_R_000032 | 3.146–1130.525 | 2121 | 0 |
| R_33 | GAREUD_R_000033 | 17.205–1026.926 | 57 | 0 |
| R_34 | GAREUD_R_000034 | 7.066–642.905 | 247 | 0 |
| R_35 | GAREUD_R_000035 | 2.304–925.441 | 8534 | 0 |
| R_36 | GAREUD_R_000036 | 6.861–776.540 | 1163 | 0 |
| R_37 | GAREUD_R_000037 | 3.441–1026.780 | 8815 | 0 |
| R_38 | GAREUD_R_000038 | 59.929–725.846 | 178 | 0 |
| R_39 | GAREUD_R_000039 | 4.372–1242.395 | 4965 | 0 |
| R_40 | GAREUD_R_000040 | 3.976–1237.278 | 2736 | 0 |
| R_41 | GAREUD_R_000041 | 0.000–1211.276 | 6511 | 4 |
| R_42 | GAREUD_R_000042 | 0.000–1008.366 | 7566 | 1 |
| R_43 | GAREUD_R_000043 | 0.000–1493.691 | 2134 | 1 |
| R_44 | GAREUD_R_000044 | 0.000–1273.152 | 2244 | 1 |
| R_45 | GAREUD_R_000045 | 0.000–1021.980 | 7330 | 1 |
| R_46 | GAREUD_R_000046 | 3.076–1599.414 | 4210 | 0 |
| R_47 | GAREUD_R_000047 | 0.000–1588.732 | 2167 | 4 |
| R_48 | GAREUD_R_000048 | 4.128–1036.557 | 8254 | 0 |
| R_49 | GAREUD_R_000049 | 5.468–1187.076 | 5580 | 0 |
| R_50 | GAREUD_R_000050 | 3.256–869.120 | 916 | 0 |
| R_51 | GAREUD_R_000051 | 5.067–1095.090 | 5010 | 0 |
| R_52 | GAREUD_R_000052 | 0.000–1284.201 | 6477 | 2 |
| R_53 | GAREUD_R_000053 | 0.000–1264.657 | 6307 | 4 |
| R_54 | GAREUD_R_000054 | 8.778–1229.763 | 898 | 0 |
| R_55 | GAREUD_R_000055 | 2.345–1064.263 | 1152 | 0 |
| R_56 | GAREUD_R_000056 | 0.000–548.170 | 849 | 1 |
| R_57 | GAREUD_R_000057 | 1.651–2008.297 | 1388 | 0 |
| R_58 | GAREUD_R_000058 | 4.437–779.392 | 1363 | 0 |
| R_59 | GAREUD_R_000059 | 3.024–927.154 | 3669 | 0 |
| R_60 | GAREUD_R_000060 | 0.000–864.955 | 3956 | 2 |
| R_61 | GAREUD_R_000061 | 0.000–1410.797 | 4665 | 2 |
| R_62 | GAREUD_R_000062 | 0.000–1903.331 | 3310 | 1 |
| R_63 | GAREUD_R_000063 | 0.000–699.878 | 1885 | 1 |
| R_64 | GAREUD_R_000064 | 0.000–1152.330 | 1187 | 2 |
| R_65 | GAREUD_R_000065 | 0.000–1501.563 | 2479 | 4 |
| R_66 | GAREUD_R_000066 | 0.000–1164.587 | 3463 | 1 |
| R_67 | GAREUD_R_000067 | 12.338–2274.353 | 1194 | 0 |
| R_68 | GAREUD_R_000068 | 0.000–766.315 | 4402 | 3 |
| R_69 | GAREUD_R_000069 | 0.000–1056.021 | 5767 | 3 |
| R_70 | GAREUD_R_000070 | 0.000–1604.933 | 1605 | 1 |
| R_71 | GAREUD_R_000071 | 4.234–1596.547 | 4685 | 0 |
| R_72 | GAREUD_R_000072 | 0.000–1047.775 | 2158 | 1 |
| R_73 | GAREUD_R_000073 | 9.646–1644.998 | 3594 | 0 |
| R_74 | GAREUD_R_000074 | 0.000–850.677 | 1886 | 1 |
| R_75 | GAREUD_R_000075 | 0.000–3433.866 | 6763 | 2 |
| R_76 | GAREUD_R_000076 | 7.066–1409.206 | 1742 | 0 |
| R_77 | GAREUD_R_000077 | 0.000–991.336 | 2764 | 1 |
| R_78 | GAREUD_R_000078 | 7.033–1477.095 | 3219 | 0 |
| R_79 | GAREUD_R_000079 | 0.000–1458.373 | 3733 | 1 |
| R_80 | GAREUD_R_000080 | 14.479–1294.267 | 896 | 0 |
| R_81 | GAREUD_R_000081 | 9.222–2171.326 | 1851 | 0 |
| R_82 | GAREUD_R_000082 | 13.168–1335.029 | 405 | 0 |
