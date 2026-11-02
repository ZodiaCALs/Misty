# Licences

Copyright © 2026 ZodiaCALs

Misty uses a different licence for each kind of material. The standard’s text stays authoritative, and anyone can build products with its code.

| Material | Where | Licence | SPDX identifier |
| --- | --- | --- | --- |
| Text and figures of the standard | `standard/` | Creative Commons Attribution-NoDerivatives 4.0 International, with the translation permission below | `CC-BY-ND-4.0` |
| Stylesheet, scripts and icon sprite embedded in the standard | `standard/` | Apache License 2.0 | `Apache-2.0` |
| Reference stylesheet, token file, platform packages and scripts | `platforms/`, `tokens/`, `scripts/` | Apache License 2.0 | `Apache-2.0` |
| README, CHANGELOG, CONTRIBUTING, TRADEMARKS and this file | repository root | Creative Commons Attribution-NoDerivatives 4.0 International | `CC-BY-ND-4.0` |

The standard is one HTML file that holds both kinds of material, so its SPDX expression is `CC-BY-ND-4.0 AND Apache-2.0`: the text and figures are under CC BY-ND 4.0, and the code in its `style` and `script` elements and its icon sprite are under Apache-2.0. `REUSE.toml` records the licence of every path.

## What each licence allows

**CC BY-ND 4.0** lets anyone copy and share the standard without changes, in any medium and for any purpose, including commercial ones. They must credit ZodiaCALs, link to the licence and say whether they changed anything. Changing the format to use it in another medium doesn’t count as a change. The licence doesn’t allow sharing an adapted version, so nobody else can publish a modified standard.

**Apache-2.0** lets anyone use, change and ship the code in any product, including closed-source ones. They must include the licence and the contents of the `NOTICE` file, keep the copyright notices and mark the files they changed. It includes a patent licence from each contributor, which ends for anyone who brings a patent claim over the code. It grants no right to use the trademarks.

## Additional permission for translations

> In addition to the rights granted by the Creative Commons Attribution-NoDerivatives 4.0 International licence, ZodiaCALs grants you permission to translate the text of the Misty Design Language Standard into any language and to share your translation, provided that:
>
> 1. the translation states at its beginning that it is an unofficial translation and that the English text governs;
> 2. it names and links to the version of the standard that it translates;
> 3. it keeps every requirement identifier, token name, clause number and figure number unchanged;
> 4. it makes no change other than translation and the typographic adjustments that the target language needs; and
> 5. it does not suggest that ZodiaCALs made, reviewed or endorses it.
>
> A translation shared under this permission is licensed under CC BY-ND 4.0 with this same permission.

## Trademarks

Neither licence grants any right to use the name Misty, the Misty mark or the names of the conformance levels. `TRADEMARKS.md` sets out how they may be used.

## Full licence texts

Run `sh scripts/fetch-licenses.sh` to save the official texts in `LICENSES/`. They’re also published at:

- Apache License 2.0: <https://www.apache.org/licenses/LICENSE-2.0>
- CC BY-ND 4.0: <https://creativecommons.org/licenses/by-nd/4.0/legalcode>

## No warranty

Both licences provide the material as it is, without warranties of any kind, and limit the licensor’s liability. The full texts give the exact terms.
