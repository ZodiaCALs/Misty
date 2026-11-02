# Changelog

Misty follows the versioning rules in clause 3.6 of the standard.

## 1.1 (2026)

A minor release. Every product that conforms to 1.0 still conforms to 1.1: the new requirements are SHOULD or MAY, and the fixes change the reference implementation, not the requirements.

### Added

- Annex A, Platforms: how tokens, materials, type, motion, settings and accessibility map to Apple platforms, Android, Windows, Flutter and JavaScript runtimes, with requirements PLT-01 to PLT-11.
- Annex B, Internationalisation: writing direction, scripts and typefaces, growth in translation and locale formats, with requirements INT-01 to INT-11, a right-to-left preview of every page and a pseudo-localisation sample.
- `tokens/misty.tokens.json` in the Design Tokens Format Module 2025.10, and packages generated from it for web, Apple platforms, Android, Windows, Flutter, JavaScript and design tools.
- `scripts/verify_contrast.py`, which checks COL-10 at all 360 hues in both appearances.
- Clause 1.7, on copyright, licences and trademarks, with `LICENSE.md`, `TRADEMARKS.md`, `NOTICE` and `REUSE.toml`.

### Fixed in the reference implementation

- LAY-06 and ACC-15: long one-word titles, long inline code and one segmented control no longer scroll the page sideways at 320 px.
- LAY-12, ACC-12 and ICO-08: on touch screens, controls drawn smaller than 44 px grow to 44 px, and switches, links and copy buttons get a 44 px hit area, so neighbouring targets don’t overlap.
- ICO-10 and WRI-12: the stylesheet uses logical properties throughout, directional glyphs mirror in right-to-left layouts, and tab arrow keys and the Beside transition follow the writing direction.
- TYP-08: Chinese, Japanese and Korean text drops negative tracking and keeps a line height of 1.7, and each language reaches for faces drawn for it.
- TYP-06: control labels set at 11 or 12 px are now 13 px, and no text is set below 11 px.
- WRI-03: two uppercase labels longer than three words are shorter.
- DAT-05: every table header cell carries `scope`.
- STA-02: two hover effects that move things are limited to devices that can hover.

### Corrected

- The light Ink 50 entry in the corrections table now reads at least 4.7:1 at every hue, not 4.8:1. The measured minimum is about 4.76:1, so ACC-03 and COL-10 still pass.

## 1.0 (2026)

The first stable release: 32 clauses, 226 requirements and 38 components.
