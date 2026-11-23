<h1 align="center">Misty Design Language</h1>
<p align="center"><em>See what you see.</em></p>

<p align="center">
  <a href="media/misty-in-motion.mp4"><img src="media/misty-poster.jpg" width="640" alt="Watch Misty in motion. Three blue glass sheets float around a pearl of light."></a>
</p>

<p align="center">
  <a href="https://misty-beta.vercel.app/"><strong>Explore the demo</strong></a> &nbsp;·&nbsp;
  <a href="standard/Misty_Design_Language_Standard_1_2.html">Read the standard</a> &nbsp;·&nbsp;
  <a href="#build-with-misty">Build with Misty</a>
</p>

Misty starts with one hue. It tints the light behind a toolbar, the ink on a page and the glass between them. Four material grades control how much of the field shows through. Native type and directional motion help people keep their place as the interface changes.

**Edition 1.2** is stable, with 38 components and 251 requirements across 32 clauses and two annexes. The accessibility target is WCAG 2.2 AA. The platform and internationalisation annexes are provisional.

## Explore the demo

Open `index.html` in a browser to explore locally. The pages embed their styles. Keep the `media/` folder beside the homepage for offline film playback.

| Study | What to try |
| --- | --- |
| [Glass lab](index.html#glass-lab) | Pull the sheets apart, pick a hue and switch the top layer between Clear, Mist, Veil and Cloud. |
| [Animation](index.html#animation) | Scrub the same 600 ms across Fluid, Spring, Exit and Linear. Stop halfway to compare how far each dot has travelled. |
| [Component playground](index.html#components) | Filter the controls, edit a field and preview feedback. |
| [Fieldbook](sample/index.html) | Follow a walk across Black Down. Select a stop on the map to read its journal entry. |
| [Misty in motion](index.html#film) | Watch the materials separate, change hue and settle in a 24-second film. |

## Inside the standard

The standard opens offline. In its palette, change the hue, appearance or panel material. The material lab lets you tune opacity, blur and saturation independently. Clause 31 gathers the numbered requirements for product reviews. [Material lab](standard/Misty_Design_Language_Standard_1_2.html#materials-lab) · [Review checklist](standard/Misty_Design_Language_Standard_1_2.html#checklist-review) · [Previous edition](standard/Misty_Design_Language_Standard_1_1.html)

Three product patterns informed the design. In FlashCard, a draft keeps its selection when an inspector moves. In Jellyfesh, cover art supplies a hue until the listener chooses one. In ShoalNex, closing a full-screen photo returns keyboard focus to the current thumbnail. [Design concept](standard/Misty_Design_Language_Standard_1_2.html#design-concept) · [Product patterns](standard/Misty_Design_Language_Standard_1_2.html#product-patterns)

The brand gallery compares Daybreak, Grades, Monogram and Field at different sizes and in both appearances. Try a mark in the gallery’s own toolbar. [Mark gallery](brand/index.html) · [SVG originals](brand/marks/)

## Build with Misty

For a web project, link the reference stylesheet and choose a hue on the root element. The same Mist classes used on the demo’s navbar also work on a card.

```html
<!doctype html>
<html lang="en" style="--m-hue: 165">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Field notes</title>
    <link rel="stylesheet" href="platforms/web/misty.css">
  </head>
  <body>
    <main class="wrap section">
      <article class="card glass glass--mist">
        <h1>Field notes</h1>
        <p>Low cloud over Black Down this morning.</p>
      </article>
    </main>
  </body>
</html>
```

Every platform package reads from the same token source. Native packages resolve a hue at runtime using the browser colour conversion. Design-tool exports include light and dark values at hue 250. [Source tokens](tokens/misty.tokens.json) · [Platform mappings](standard/Misty_Design_Language_Standard_1_2.html#platforms-packages)

| Platform | Integration |
| --- | --- |
| Web | [Components and tokens](platforms/web/misty.css) · [Tokens only](platforms/web/misty-tokens.css) |
| Apple platforms | [Swift package](platforms/apple/) |
| Android | [Jetpack Compose](platforms/android/MistyTokens.kt) · [View resources](platforms/android/res/) |
| Windows | [C# tokens](platforms/windows/MistyTokens.cs) · [XAML resource dictionary](platforms/windows/MistyTokens.xaml) |
| Flutter | [Dart package](platforms/flutter/) |
| React Native and JavaScript | [ES module](platforms/js/misty-tokens.mjs) |
| Design tools | [Light tokens](platforms/dtcg/light.tokens.json) · [Dark tokens](platforms/dtcg/dark.tokens.json) |

<details>
<summary><strong>Platform setup and code examples</strong></summary>

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

</details>

### Languages and writing direction

Set `lang` and `dir` on the root element, and on passages that use a different language or direction. Logical spacing mirrors the layout, directional glyphs turn and language tags select typefaces for Japanese, Chinese and Korean text. Annex B includes a right-to-left preview and a pseudo-localisation sample for testing text growth. [Writing direction](standard/Misty_Design_Language_Standard_1_2.html#international-direction) · [Translation and text growth](standard/Misty_Design_Language_Standard_1_2.html#international-growth)

## Maintain the reference

After editing the source token file, update the matching declarations in the web reference stylesheet and the current standard’s embedded stylesheet. From the repository root, regenerate the packages, check the stylesheet, verify contrast and refresh the demo pages.

```sh
python3 scripts/build_tokens.py
python3 scripts/build_tokens.py --check platforms/web/misty.css
python3 scripts/verify_contrast.py
python3 scripts/build_site.py
```

The scripts use Python 3.8 or later and the standard library. The contrast check tests each specified foreground and background pair at all 360 hues in light and dark appearances. For a stylesheet-only change, `build_site.py` refreshes the homepage, Fieldbook and the brand gallery. [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

## Conformance and licences

A conformance claim names the edition, level and review date. A native claim can also name the platform. For example, “Misty 1.2 Complete on Android, reviewed 22 November 2026” records a review against every MUST at that level. [Conformance](standard/Misty_Design_Language_Standard_1_2.html#overview-conformance) · [Trademark policy](TRADEMARKS.md)

| Material | Terms |
| --- | --- |
| Standard text and figures, including design concepts and product patterns | CC BY-ND 4.0, with permission for unofficial translations |
| Stylesheet, scripts, tokens, icons and platform packages | Apache License 2.0 |
| README and other documentation | CC BY-ND 4.0 |
| Misty name, mark and conformance levels | Trademark policy |

The licence describes the translation permission in full. Per-file declarations are available in REUSE format. [Licences](LICENSE.md) · [REUSE declarations](REUSE.toml) · [Notice](NOTICE)

<details>
<summary><strong>Before publishing a release</strong></summary>

1. Check the permission contact in `TRADEMARKS.md`.
2. Choose one of the four mark options in `brand/`. Until then, the pages keep the 1.0 mark.
3. Run `sh scripts/fetch-licenses.sh` to save the official licence texts in `LICENSES/`.
4. Search the trademark registers in the countries and classes you care about before relying on the name. “Misty” is a common word.
5. Build the Swift, Kotlin, Dart and C# packages once in their own toolchains. They’re generated code and haven’t been compiled yet.
6. Have a lawyer review `LICENSE.md` and `TRADEMARKS.md`.

</details>
