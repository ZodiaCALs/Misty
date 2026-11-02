#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 ZodiaCALs
# SPDX-License-Identifier: Apache-2.0
"""Check COL-10: every pair in the contrast table meets its threshold at all
360 hues, in both appearances.

Layers are composited the way the standard's own contrast table does it in
the browser: each colour is quantised to 8 bits and blended over the layer
below. The exit status is 1 if any pair fails.

  python3 scripts/verify_contrast.py
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from misty_color import resolve  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PAIRS = [
    ("Ink 90 on field", "--m-ink-90", ["--m-sky"], 4.5),
    ("Ink 70 on field", "--m-ink-70", ["--m-sky"], 4.5),
    ("Ink 50 on field", "--m-ink-50", ["--m-sky"], 4.5),
    ("Accent text on field", "--m-accent-text", ["--m-sky"], 4.5),
    ("On-accent on accent", "--m-on-accent", ["--m-accent"], 4.5),
    ("Ink 70 on Mist over field", "--m-ink-70", ["--m-sky", "glass:--m-glass-alpha"], 4.5),
    ("Ink 90 on Veil over field", "--m-ink-90", ["--m-sky", "glass:--m-glass-alpha-veil"], 4.5),
    ("Ink 70 on Cloud", "--m-ink-70", ["--m-cloud"], 4.5),
    ("Accent text on accent soft", "--m-accent-text", ["--m-sky", "--m-accent-soft"], 4.5),
    ("Success on field", "--m-success", ["--m-sky"], 4.5),
    ("Warning on field", "--m-warning", ["--m-sky"], 4.5),
    ("Danger on field", "--m-danger", ["--m-sky"], 4.5),
]


def load():
    doc = json.loads((ROOT / "tokens" / "misty.tokens.json").read_text(encoding="utf-8"))
    colours, numbers = {}, {}
    for name, group in doc.items():
        if name.startswith("$"):
            continue
        for key, tok in group.items():
            if key.startswith("$"):
                continue
            ext = tok.get("$extensions", {}).get("org.misty", {})
            if tok["$type"] == "color":
                colours[ext["css"]] = {"light": ext["light"], "dark": ext["dark"]}
            elif tok["$type"] == "number":
                numbers[ext["css"]] = {"light": tok["$value"], "dark": ext.get("dark", tok["$value"])}
    return colours, numbers


def over(dst, rgba):
    r, g, b, a = rgba
    a8 = math.floor(a * 255 + 0.5) / 255
    return tuple(int(math.floor(c * a8 + d * (1 - a8) + 0.5)) for c, d in zip((r, g, b), dst))


def luminance(rgb):
    def lin(v):
        v /= 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = luminance(a), luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def pair_ratio(colours, numbers, fg, layers, appearance, hue):
    dst = (255, 255, 255)
    for layer in layers:
        if layer.startswith("glass:"):
            glass = {"l": numbers["--m-glass-l"][appearance], "c": numbers["--m-glass-c"][appearance], "h": 0.0,
                     "alpha": numbers[layer[6:]][appearance], "hue": "relative"}
            dst = over(dst, resolve(glass, hue))
        else:
            dst = over(dst, resolve(colours[layer][appearance], hue))
    return ratio(over(dst, resolve(colours[fg][appearance], hue)), dst)


def main():
    colours, numbers = load()
    failures = 0
    for appearance in ("light", "dark"):
        print(f"{appearance.capitalize()} appearance, hues 0 to 359")
        for label, fg, layers, need in PAIRS:
            worst, at = min((pair_ratio(colours, numbers, fg, layers, appearance, h), h) for h in range(360))
            ok = worst >= need
            failures += not ok
            print(f"  {'pass' if ok else 'FAIL'}  {label:<28} lowest {worst:5.2f}:1 at {at:3d}°  needs {need}:1")
    print("Every pair passes at every hue." if not failures else f"{failures} pair(s) fail.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
