"""Append measured pixel-speed ranges after physical flight speed in a paper table.

Uses the Python standard library only. The input LaTeX file is never modified.
"""
import argparse
import csv
from decimal import Decimal
from pathlib import Path
import re


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--ranges', type=Path, default=Path(__file__).resolve().parents[1] /
                        'docs/metadata/gareud_real_image_plane_speed_ranges.csv')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        raise ValueError('Use a separate output to preserve the original LaTeX.')
    with args.ranges.open(encoding='utf-8-sig', newline='') as stream:
        ranges = {r['sequence']: r for r in csv.DictReader(stream)}
    text = args.input.read_text(encoding='utf-8-sig')
    updated = []
    lines = []
    for line in text.splitlines(keepends=True):
        match = re.match(r'^(?:G2A|A2A)\s*&\s*R\\_(\d+)\s*&', line)
        if match:
            seq = f'GAREUD_R_{int(match[1]):06d}'
            if seq in updated or seq not in ranges:
                raise ValueError(f'Duplicate or unrecognized sequence: {seq}')
            if 'image-plane speed' in line:
                raise ValueError(f'Speed already present: {seq}')
            r = ranges[seq]
            lo = f"{Decimal(r['min_speed_px_s']):.3f}"
            hi = f"{Decimal(r['max_speed_px_s']):.3f}"
            pattern = r'(physical flight speed\s+[^;\r\n]*?~m/s)\.'
            line, count = re.subn(pattern, lambda m: m[1] +
                f'; image-plane speed {lo}--{hi}~pixels/s.', line)
            if count != 1:
                raise ValueError(f'Expected exactly one physical flight speed: {seq}')
            updated.append(seq)
        lines.append(line)
    if set(updated) != set(ranges):
        raise ValueError('The LaTeX sequence set does not match the range CSV.')
    text = ''.join(lines)
    old = 'Each row reports the sequence identifier, number of synchronized RGB frames, target UAV type, illuminance range, and scenario labels.'
    new = (old[:-1] + ', including physical flight speed and image-plane speed ranges. '
           r'Image-plane speed is computed from the displacement of the annotated bounding-box center between adjacent RGB frames, '
           r'using 30~fps and the $1024\times576$ image coordinate system. '
           r'Ranges are the minimum and maximum over valid adjacent-frame pairs, reported in pixels/s to three decimal places; '
           r'camera motion and annotation variation may contribute, so these values are not physical flight speeds in m/s.')
    if text.count(old) != 1:
        raise ValueError('Expected original table caption was not found exactly once.')
    text = text.replace(old, new)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding='utf-8')
    print(f'Updated {len(updated)} sequence rows: {args.output}')


if __name__ == '__main__':
    main()
