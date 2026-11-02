#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 ZodiaCALs
# SPDX-License-Identifier: Apache-2.0
"""Embed the current platforms/web/misty.css in the pages of the Misty web.

The home page, the Fieldbook sample site and the mark options page are
self-contained, like the standard: each carries a copy of the reference
stylesheet in its first style element, id "misty-css". Run this after
changing misty.css.

  python3 scripts/build_site.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["index.html", "sample/index.html", "brand/index.html"]


def main():
    css = (ROOT / "platforms" / "web" / "misty.css").read_text(encoding="utf-8")
    for page in PAGES:
        path = ROOT / page
        html = path.read_text(encoding="utf-8")
        new, count = re.subn(r'^(\s*<style id="misty-css">).*?(</style>)', lambda m: m.group(1) + "\n" + css + "\n" + m.group(2),
                             html, count=1, flags=re.S | re.M)
        if count != 1:
            print(f'{page}: no <style id="misty-css"> block')
            return 1
        path.write_text(new, encoding="utf-8")
        print(f"  updated {page}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
