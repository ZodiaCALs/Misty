# Misty Design Language

**See what you see.** The most elegant design language for the future.

Misty is made for clear, quiet interfaces: thin glass over a lit field, one hue, native type and motion that shows direction. This repository holds the standard, its reference stylesheet, one token file and a package generated from that file for each platform.

- **Version:** 1.1, stable. Annexes A and B are provisional.
- **Scope:** 248 requirements in 32 clauses and two annexes, and 38 components.
- **Platforms:** web, Apple platforms, Android, Windows, Flutter, React Native and other JavaScript runtimes.
- **Accessibility:** WCAG 2.2 at Level AA.

## Contents

```text
standard/    The standard, as one self-contained HTML file
tokens/      misty.tokens.json, the source of every value
platforms/   Packages generated from the token file
  web/       misty.css (tokens and components) and misty-tokens.css (tokens only)
  apple/     Swift package for iOS, iPadOS, macOS, watchOS, tvOS and visionOS
  android/   Kotlin for Jetpack Compose, and colour resources for views
  windows/   C# for WinUI 3, WPF and .NET MAUI, and a XAML resource dictionary
  flutter/   Dart package for Flutter on any platform
  js/        ES module for React Native and other JavaScript runtimes
  dtcg/      Light and dark token files for design tools
scripts/     The token build, the stylesheet check and the contrast check
```

## Read the standard

Open `standard/Misty_Design_Language_Standard_1_1.html` in a current browser. It works offline and needs no server. Change the hue or the appearance from the palette in the top bar, and every figure follows. To review a product, work through the conformance checklist in clause 31.

## Use Misty

Every package computes theme colours from the hue while the app runs, with the conversion browsers use, so a hue chosen on one device matches on every other. Annex A of the standard maps each token family, material and setting to each platform.

### Web

```html
<link rel="stylesheet" href="platforms/web/misty.css">
```

`misty.css` holds the tokens and every component class that clause 30 lists. For tokens alone, use `misty-tokens.css`. Set `--m-hue` on the root element to change the hue. For a right-to-left language, set `dir="rtl"` on the root element too: the layout mirrors on its own.

### Apple platforms

Add `platforms/apple` to your project as a local Swift package. It supports iOS 15, macOS 12, tvOS 15, watchOS 8, visionOS 1 and later.

```swift
import MistyTokens

let theme = MistyTheme(hue: 250, appearance: colorScheme == .dark ? .dark : .light)

Text("Field notes")
    .foregroundStyle(theme.ink90)
    .padding(MistySpace.s4)
    .background(theme.cloud, in: RoundedRectangle(cornerRadius: MistyRadius.lg))
```

Read `colorScheme` with `@Environment(\.colorScheme)`.

### Android

Copy `platforms/android/MistyTokens.kt` into a module that uses Jetpack Compose, and change its package name to your own. Copy `platforms/android/res` into the module’s resources if you also use views.

```kotlin
val theme = MistyTheme(
    hue = 250.0,
    appearance = if (isSystemInDarkTheme()) MistyAppearance.Dark else MistyAppearance.Light,
)

Text("Field notes", color = theme.ink90, modifier = Modifier.padding(MistySpace.S4))
```

### Windows

Add `platforms/windows/MistyTokens.cs` to a project on .NET 6 or later. For WinUI 3, merge the resource dictionary into your app’s resources:

```xml
<ResourceDictionary.MergedDictionaries>
    <ResourceDictionary Source="MistyTokens.xaml" />
</ResourceDictionary.MergedDictionaries>
```

The dictionary is resolved at hue 250. To follow another hue, resolve colours with `new MistyTheme(hue: 165).Sky` and pass the channels to `Microsoft.UI.ColorHelper.FromArgb`.

### Flutter

```yaml
dependencies:
  misty_tokens:
    path: platforms/flutter
```

```dart
const theme = MistyTheme(hue: 250);

Text(
  'Field notes',
  style: TextStyle(color: theme.ink90, fontSize: MistyType.h3(MediaQuery.sizeOf(context).width)),
);
```

### React Native and other JavaScript runtimes

```js
import { theme, space, radius } from "./platforms/js/misty-tokens.mjs";

const colours = theme({ hue: 250, appearance: "dark" });
const card = { backgroundColor: colours.cloud, padding: space.s4, borderRadius: radius.lg };
```

If your bundler doesn’t resolve `.mjs` files, rename the file to `misty-tokens.js`.

### Design tools

`platforms/dtcg/light.tokens.json` and `dark.tokens.json` follow the Design Tokens Format Module 2025.10, resolved at hue 250, for tools that import that format.

## Languages and writing direction

Set `lang` and `dir` on the root element, and on any part in another language or direction. The stylesheet uses logical properties, mirrors directional glyphs and reaches for faces drawn for Japanese, Chinese and Korean text according to the language tag. Annex B of the standard covers scripts, growth in translation and locale formats. It includes a right-to-left preview of every page and a pseudo-localisation sample for testing.

## Change a token

1. Edit `tokens/misty.tokens.json`.
2. Run `python3 scripts/build_tokens.py` to regenerate every package.
3. Make the same change in `:root` in `platforms/web/misty.css` and in the standard’s embedded stylesheet, then run `python3 scripts/build_tokens.py --check platforms/web/misty.css`.
4. Run `python3 scripts/verify_contrast.py`. It checks every pair in the contrast table at all 360 hues in both appearances, as COL-10 requires, and fails if any pair drops below its threshold.

The scripts need Python 3.8 or later and no other packages.

## Claim conformance

A product that meets every MUST at a level says so in the form GEN-04 gives: “Misty 1.1 Core, reviewed 2 November 2026”. A native product names its platform too, as PLT-11 suggests: “Misty 1.1 Complete on Android, reviewed 2 November 2026”. There’s no certification and no badge; see `TRADEMARKS.md`.

## Licences

| Material | Licence |
| --- | --- |
| Text and figures of the standard | CC BY-ND 4.0, with a permission for unofficial translations |
| Stylesheet, scripts, tokens, icons and platform packages | Apache License 2.0 |
| The name Misty, the mark and the conformance levels | Trademark policy |
| This README and the other documents | CC BY-ND 4.0 |

`LICENSE.md` explains what each licence allows and gives the translation permission in full. `TRADEMARKS.md` sets out how the name and the mark may be used. `REUSE.toml` records the licence of every path in machine-readable form.

## Before you publish

1. Replace `[contact address]` in `TRADEMARKS.md` with an address for permission requests.
2. Run `sh scripts/fetch-licenses.sh` to save the official licence texts in `LICENSES/`.
3. Search the trademark registers in the countries and classes you care about before relying on the name. “Misty” is a common word.
4. Build the Swift, Kotlin, Dart and C# packages once in their own toolchains. They’re generated code and haven’t been compiled yet.
5. Have a lawyer review `LICENSE.md` and `TRADEMARKS.md`.

## Contributing

See `CONTRIBUTING.md`.
