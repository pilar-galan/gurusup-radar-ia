---
name: gurusup-style-reference
description: "Design or build new GuruSup surfaces: pages, components, or product UI, consistent with the GuruSup brand system. Use for new components, new page sections, or when extending the system to a case it doesn't explicitly cover yet."
---

# GuruSup Style Reference
> Flat, square, monospace-forward. A technical system with no ornament: no rounded corners, no drop shadows, one 4px grid underneath everything.

**Theme:** light + dark, both set. Every token table below carries real values for each mode, and they are not mirror images of each other: several pairs that pass comfortably in one mode measure short in the other, so a change to one mode is only half a change.

**Status:** early-stage. Color, typography, the spacing grid, and the components listed in the Components section are decided below. Remaining components, logo usage rules, and content blocks are still open. Nothing about them is asserted here until it's real.

## Guidance map

This file is the canonical entry point and always wins when guidance conflicts. Read it completely. Load the focused guides below only when the work touches their scope; a full interface review loads every applicable guide.

| Guide | Read when |
|---|---|
| [`design/typography.md`](design/typography.md) | Text wraps, numbers update or align, or typography rendering is being audited |
| [`design/interaction.md`](design/interaction.md) | The surface includes links, buttons, controls, hover, focus, active, disabled, loading, or empty states |
| [`design/motion.md`](design/motion.md) | Anything moves, transitions, enters, exits, auto-scrolls, or swaps state visually |
| [`design/icons.md`](design/icons.md) | Icons appear in controls, labels, navigation, states, or directional UI |
| [`design/media.md`](design/media.md) | The surface includes images, logos, video, illustrations, crops, or responsive media |
| [`design/performance.md`](design/performance.md) | The implementation hydrates, animates, changes layout, or needs a performance audit |

Keep stable GuruSup decisions here or in one focused guide, never duplicated across both. Keep review procedure in the project skills, not in the design system.

The focused guides adapt selected ideas from [make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) to GuruSup rather than importing its rules wholesale. GuruSup decisions and constraints always win. Attribution is recorded in [`../../THIRD_PARTY_NOTICES.md`](../../THIRD_PARTY_NOTICES.md).

## Principles

These are the reasoning behind the concrete rules below. Read this section when building something the rest of this document doesn't explicitly cover, and extend from the reasoning rather than guessing.

1. **Structure comes from a shared border, never from gap plus shadow plus radius.** When two blocks of equal rank sit next to each other, they share one line. The block, not the layout, ends with a border on its own trailing edges, and the leading edges are covered by the parent container's own border. Never give both neighbors their own border on the same seam (that reads as two lines, not one), and never use whitespace or a drop shadow to imply grouping when a shared border says it more precisely.

   This is about blocks of equal rank sitting next to each other, which is where a shared border is the more precise instrument. It is not a claim that spacing carries no structure: within a single block, vertical rhythm still does the grouping, and it needs a real step between levels to do it. Use `8px` within a group, `16px` between groups inside one block, and `32px` between sections of a page. The reason to state the steps rather than leave them to taste is that the gap between groups has to be at least twice the gap within one before a reader sees a group at all; a system where everything sits at one density ends up asking borders to do work that space should be doing, which is the failure mode Principle 1 is guarding against from the other direction.
2. **Shadow means "floating above the page."** Reserve elevation (shadow) for things that sit above other content in a separate layer: an overlay, a popover, a menu. Anything that sits in-flow on the page (a card, a button, an input, a badge) gets its separation from a border, never a shadow. Mixing the two signals makes a static element look like it's about to close.
3. **Reuse the established pattern.** Never the nearest generic primitive that "also compiles." If a job already has a component doing it elsewhere in the system (a button, a section label, a chip), use that exact component and its exact styling. A hand-rolled `<a>` with copied-looking classes is not the same as the real `Button`. It will drift the moment the real one changes.
4. **A closed, small set of semantic tones.** Status and emphasis colors are a short, named, closed list. Never invent a new tone to avoid deciding which existing one fits. If nothing fits, that's a signal the existing set needs revisiting on purpose, not a license to add a one-off.
5. **Once a categorical palette exists, changes are reassignment, not new colors.** If a fixed set of colors (say a chart palette) turns out to have a real legibility problem, the fix is reassigning which of the existing colors is used where, never nudging or adding a hex to patch one spot.
6. **A constraint states its resolution path, or says plainly there isn't one.** Never show a disabled or locked control without saying whether, and how, it could change. If there's truly no path yet, say "not configurable yet" rather than inventing one or staying silent.
7. **One canonical word per concept, everywhere.** Pick one term for a given thing (a role, a status, an action) and use it in every label, empty state, and filter. Never let synonyms drift in copy across the system.
8. **A number's display treatment follows its semantic role, not habit.** A count scoped to the control right next to it (think "12 results" beside a filter) is plain muted text, never a `Badge`, which reads as another selectable option next to something like `Tabs`. A page-level total independent of any filter is a bold inline number in a header stat line. Don't reach for `Badge` by default just because a number needs a container.
9. **Time-series reads oldest to newest, left to right. Always.**
10. **An error explains itself before it shows itself.** Lead with a plain-language explanation of what went wrong and what to do about it, and keep the raw technical string available underneath for anyone who needs it, support or debugging. Never replace it, and never show it alone.
11. **Shipped component primitives are restyled, not restructured.** When using a component library (this system uses shadcn/ui on Radix), change color, spacing, and font at the token and class layer only. Never fork a primitive's DOM structure or behavior to fit a one-off need.

## Tokens: Color

Six groups, by role: **Brand** (identity colors), **Semantic** (status colors), **Chart** (the categorical palette), **Surface** (backgrounds, fills, borders), **Text**, and **Syntax** (code highlighting only). Grayscale is warm-tinted rather than clinical, in both modes and with no exception — a neutral gray beside a warm one is visible even when neither color is nameable on its own. Primary is a single deliberate accent, reserved rather than general-purpose (see the Button rule below).

Brand tokens carry a `brand-` prefix on their source variable (`--brand-primary`, `--brand-amber`, and so on, in `src/styles/global.css`). Components don't reference the prefixed name directly; Primary uses the unprefixed alias Tailwind expects (`bg-primary`), which just points at the `brand-` value. Semantic, Chart, Surface, and Text tokens don't get this prefix, they're already unambiguous.

### Brand

Concept: terminal/CRT phosphor, brought forward rather than replicated literally, think the WOPR screens in *WarGames* reimagined for today. Same value in light and dark.

| Token | Hex | Reference |
|---|---|---|
| `primary` | `#2ECF8F` | Phosphor green, **solid fill only**. Reserved for one deliberately-branded CTA (the copy-URL button on the product's Brain MCP page is the designated instance); never a general hover or accent color, never in charts. It measures `2.01:1` against white, so it cannot carry text, an icon, or a hairline on a light surface. |
| `brand-primary-700` / `ring` / `primary-ink` | `#1B8A5E` | Step 700 of the same ramp, promoted to a real token for the focus ring on light surfaces. `4.34:1` against white, which clears WCAG 1.4.11's `3:1` floor for a non-text indicator; the base green does not. This came from the existing ramp rather than a new hex, per Principle 5. In dark mode the ring goes back to the base green, which measures `Lc −62.1` there — each mode uses the step that works in it, and neither step works in both. |
| `brand-cyan` | `#2EC3D1` | Storage-tube cyan (Tektronix) |
| `brand-red` | `#D13C2E` | Alert red (DEFCON-style terminal alarms) |
| `brand-orange` | `#F2701C` | Bright accent orange |
| `brand-lavender` | `#AC80FD` | Bright accent purple |
| `brand-gold` | `#EDC34D` | Bright accent gold |
| `brand-azure` | `#4798FF` | Bright accent blue |

Only Primary has an unprefixed alias (`bg-primary`); no component consumes the rest directly today. They exist as the identity family, not as general-purpose UI colors.

#### Primary: fill and ink

Primary is two roles and therefore two tokens. `primary` (`#2ECF8F`) is a **fill**: a surface, a bar, a mark. `primary-ink` is the same phosphor green corrected for **reading**: `brand-primary-700` (`#1B8A5E`) in light mode, the base green in dark. One value cannot hold both jobs. `#2ECF8F` measures `2.01:1` against white, which is fine behind something and illegible as a letterform or a hairline, so the split is not a preference, it is what the measurement forces.

Where the fill is permitted, and the full list:

| Use | Shape |
|---|---|
| One deliberately-branded CTA | Solid `bg-primary` / `text-primary-foreground`, the designated instance being the copy-URL button on the product's Brain MCP page |
| Progress and volume fills | The filled portion of a bar, gauge or confidence meter |
| Active toggle track | The `on` half of a switch |
| Emphasis or verification mark | A small solid square, on the 4px grid, attached to something the reader can verify: a confirmed fact, a statement line, a badge |
| Live-data accent in a generated field | A minority of points in a dot field or point cloud |
| Terminal node of a flow diagram | A solid frame around the node the flow arrives at, once per diagram |

Where the ink is used: anything meant to be **read** in the brand color. Section labels (see Section label pattern), the `link` variant of Button and Badge, and any glyph that carries meaning rather than decorating, such as the check that marks a step confirmed. On a light surface this is always `primary-ink`, never `primary`.

The one exception is a block that paints its own dark surface with `bg-foreground` without entering `.dark` scope. There the token still resolves to its light-mode value, and the base green is the legible choice: `tetris-footer-29` and `feature-media-card-13` are the two instances.

Everything else stays inverted-neutral. Buttons and badges keep `bg-foreground` / `text-background` (see Button), body links keep `foreground`, hovers keep `secondary` or `accent`, and charts keep the `chart-N` palette. Primary marking something is a statement that the thing is real, verified or active; spending it on ordinary chrome empties that statement.

**Ramps.** Every brand hex above is step `500` of an 11-step ramp (`50` to `950`). Steps are derived, never hand-picked: mix the base with white or black in OKLab at fixed weights, so lightness and chroma scale together and the hue never drifts. White and black are achromatic, so the base hue survives the mix untouched. The weights, as a share of the base: `50` 8%, `100` 16%, `200` 28%, `300` 42%, `400` 62% toward white; `600` 88%, `700` 74%, `800` 58%, `900` 42%, `950` 28% toward black. Every derived step is resolved to a literal hex, not shipped as a `color-mix()` expression: a step has to be readable, quotable, and pasteable into a design tool or a non-CSS surface, and a live mix expression is none of those. When a token needs a lighter or darker variant of a brand color, promote the matching ramp step rather than inventing a new hex.

### Semantic

Status colors, not brand identity, unlike Primary these differ between light and dark.

| Token | Light | Dark | Role |
|---|---|---|---|
| `destructive` | `#C4432E` | `#FF9F8F` | Errors, destructive actions, and negative-delta text. The dark value was `#E2604A`, which measured `Lc −38.1` as text on Background and left its own ink foreground at only `Lc +39.9` — both under the `60` non-body minimum. Raising lightness alone produces a washed salmon (`#F0AA9E`, chroma 0.32); taking saturation to the maximum at the same lightness holds the color together (`Lc −62.6`, chroma 0.44) for the same measured contrast. Saturation barely moves the number, but it is what keeps the red reading as red. Fixing the fill fixes both roles at once, where flipping the foreground to white would only have fixed the fill. |
| `success` | `#15803D` | `#34D399` | Positive state, confirmations |

### Chart

The categorical palette, `chart-1` through `chart-8`, fixed order, same value in both themes. This is the full set. Per Principle 5, a legibility problem gets fixed by reassigning which token is used where, never by adding or nudging a hex. The table below is indexed by token; a swatch display sorted by saturation is a presentation choice and doesn't change which hex a given `chart-N` token holds.

**Known limits of this set, so nobody has to rediscover them.** These hexes were chosen by hand and are deliberately kept, but they are not a validated categorical palette and they fail several standard checks: the whole set sits above the usual lightness ceiling for categorical use, `cyan` falls under the chroma floor, and `amber` and `lime` collapse into each other under the common forms of color-vision deficiency. That last one is the hard constraint: **keep `amber` and `lime` non-adjacent in `chart-N` order**, because adjacent series are the ones a reader has to tell apart. Per Principle 5 the fix for a real legibility problem is reassigning which token is used where, never editing a hex — but reassignment is only safe if you know these three facts first.

| Token | Name | Hex |
|---|---|---|
| `chart-1` | Sky | `#6FA8FF` |
| `chart-2` | Amber | `#E2B85B` |
| `chart-3` | Cyan | `#61C5D2` |
| `chart-4` | Orange soft | `#E78F5F` |
| `chart-5` | Mint | `#69C9A5` |
| `chart-6` | Rose | `#CF82B8` |
| `chart-7` | Lime | `#B6D36A` |
| `chart-8` | Coral | `#E77778` |

### Surface

| Token | Light | Dark | Role |
|---|---|---|---|
| `background` | `#FFFFFF` | `#1D1E1A` | Base app/site background. Never shaded, borders do the separating |
| `card` / `popover` | `#FFFFFF` | `#24261F` | Card and popover surface, distinct from Background in dark mode |
| `sidebar` | `#FFFFFF` | `#191A16` | Sidebar surface, distinct from both Background and Card in dark mode |
| `secondary` | `#F1F1F1` | `#2E3027` | Small-scale fill only (skeleton, badge, toggle hover), never a page surface |
| `accent` | `#F1F1F1` | `#2C2C2A` | Neutral hover fill, distinct from Secondary in dark mode |
| `border` / `input` | `#E5E5E5` | `#34362C` | Component borders, doing all surface separation on this site |
| `canvas` | `#FCFCF8` | `#1D1E1A` | Editorial page ground for marketing surfaces, a warmer paper than `background`. Never shaded, never bordered on its own |
| `well` | `#F1F1EA` | `#24261F` | Recessed field a diagram, chart or card visual sits in. A container for artwork, never a surface for body copy |

`sidebar-primary`, `sidebar-accent`, `sidebar-border`, and `sidebar-ring` are aliases of `primary`, `accent`, `border`, and `ring`, not separate values, so a sidebar can never drift from the rest of the system by having its own copy of the same color.

`canvas` and `well` are page-composition surfaces, not component surfaces. A component never chooses between them: the page picks `canvas` as its ground, and a block that carries artwork puts that artwork in a `well`. `background` and `card` stay the component-level surfaces, unchanged.

#### Inverted section

A full-bleed dark band inside a light page is a composition device, not dark mode. It needs its own four tokens, because reaching into the `.dark` scope from a light page pulls in a whole theme to paint one section, and hand-writing `rgba(248, 249, 242, …)` per element is how a closed set turns into a dozen near-identical alphas.

| Token | Value | Role |
|---|---|---|
| `inverted` | `#1D1E1A` | The band's ground |
| `inverted-foreground` | `#F8F9F2` | Body and heading text on it (15.8:1) |
| `inverted-muted-foreground` | `#F8F9F2` at 70% | De-emphasized text on it (8.3:1) |
| `inverted-border` | `#F8F9F2` at 16% | Every line on it: seams, rules, and control borders |

Four values, and that is the whole set. `inverted-border` covers the section seam, the footer rule and a button outline alike; if one of them needs to read stronger, the fix is a different treatment, not a fifth alpha. Primary is legible here (8.3:1), so an inverted band is the one place Primary may be set as text.

### Text

| Token | Light | Dark | Role |
|---|---|---|---|
| `foreground` | `#1D1E1A` | `#F8F9F2` | Body text. Warm ink and paper, never pure black or white. Also used on Card, Popover, Secondary, and Accent |
| `muted-foreground` | `#6E6C60` | `#BEBBB2` | De-emphasized text, opaque and warm-tinted in both modes like the rest of the grayscale. `Lc +76.3` on Background, `+67.9` on Secondary, `+60.9` on Border in light; `−64.0` / `−62.8` / `−64.5` on Background / Card / Sidebar in dark. Both values changed for the same reason, found the same way. The dark value was `#A4A4A4`, at `Lc −51.2` and a clinical neutral inside a warm ramp; WCAG had approved it at `6.72:1`, which is why it stood. The light value was `oklab(0 0 0 / 0.7)`, the one non-hex value in an all-hex system, kept because a translucent ink blends over photographic fills. Measurement retired that reason rather than confirming it: black at 70% goes from `Lc +89` over white to `Lc +37` over a mid-tone photograph to `Lc 0.0` over a dark one, where the text is gone. A translucent ink tracks its background instead of resisting it, which is a virtue in a fill and a failure in a label. Text over media gets a scrim and then uses this token normally — see [`design/media.md`](design/media.md). |
| `primary-foreground` | `#1D1E1A` | same | Text on Primary fill. Dark ink, not white: white on Primary fails contrast (2.01:1) |
| `destructive-foreground` | `#FFFFFF` | `#1D1E1A` | Text on Destructive fill |
| `success-foreground` | `#FFFFFF` | `#1D1E1A` | Text on Success fill |
| `sidebar-foreground` | `#535262` | `#F8F9F2` | Resting sidebar nav icon/text |
| `sidebar-accent-foreground` | `#282828` | `#F8F9F2` | Active/hover sidebar nav item text |

### Syntax

Syntax tokens are reserved for selectable code rendered by a real syntax highlighter. They follow a familiar classic-editor hierarchy and must not be reused for status, charts, ordinary prose, or decorative color.

Declared in `src/styles/global.css` alongside every other token, and displayed on `/colors/` like every other group. Both of those are recent: this table described system tokens while the values actually lived inside one component's CSS module (`code-section-10`), so `var(--syntax-keyword)` resolved to nothing anywhere else on the site, and the group was missing from the colors page entirely because `ColorGrid` only knew about five groups. The documentation was ahead of the code; the code caught up rather than the table being trimmed.

Measured and clear, in case the six extra hues invite suspicion: on the light background these run from `5.38:1` (`syntax-number`) to `13.29:1` (`syntax-keyword`), `Lc +76` to `+97`. No action needed.

| Token | Light | Dark | Role |
|---|---|---|---|
| `syntax-keyword` | `#0000AA` | `#C586C0` | Keywords and operators |
| `syntax-string` | `#A31515` | `#CE9178` | Strings, selectors, and regular expressions |
| `syntax-comment` | `#3F6F3F` | `#6A9955` | Comments |
| `syntax-function` | `#795E26` | `#DCDCAA` | Functions and class names |
| `syntax-number` | `#087A4E` | `#B5CEA8` | Numbers and booleans |
| `syntax-variable` | `#005C99` | `#9CDCFE` | Variables and properties |

## Tokens: Typography

### Geist. Sans, self-hosted. Body copy, labels, h1/h2. Variable weight 100 to 900. `--font-sans`
- **Weights:** 100–900 available as a variable axis, but not all of them are usable at every size: stay at **400 or heavier below 18px**, and treat anything under 300 as display-only at 28px and up. A thin weight that looks refined in a mockup at 48px disappears at 14px.
- **Role:** Default text face for everything that isn't a heading-mono override or a button.
- **Source:** `@fontsource-variable/geist` (Vercel, self-hosted, no CDN dependency).

### Geist Mono. Monospace, self-hosted. h3/h4, all numeric data, all buttons. Variable weight 100 to 900. `--font-mono`
- **Weights:** 100, 200, 300, 400, 500, 600, 700, 800, 900 (variable)
- **Role:** Anything technical or numeric reads as monospace. This is a deliberate signal, not a default. Also the required face for every button label, regardless of variant.
- **Source:** `@fontsource-variable/geist-mono`.

### Geist Pixel. Display and pixel face, self-hosted, single weight. Punctual labels only. `--font-pixel`
- **Weights:** 400 (static, no variable axis)
- **Role:** Narrow, deliberate use for sparkline date labels and heatmap row labels. Not a body or heading face.
- **Source:** `@fontsource/geist-pixel`.

### Base size
- **16px**, browser default. Never overridden site-wide, and the `Body` tier below is the same 16px, so the declared base is also the size most text actually renders at. An earlier revision of this section declared a 16px base and then assigned 14px to the tier described as "default text", which meant the base was overridden by every component that used it — a contradiction that quietly licenses ignoring the whole scale.

### Type scale
Named tiers, sized off what's already in real use across the product, not invented from scratch. Each tier fixes size, line height **and** weight together, so choosing a role is one decision rather than three. Leaving weight unspecified is how a system ends up with everything at 500 and 600 and no weight left to signal emphasis with.

Line heights snap to the **4px spacing grid** rather than using free ratios, following the same vertical rhythm rule as layout spacing.

| Name | Size | Line height | Weight | Usage |
|---|---|---|---|---|
| Caption | 12px | 16px | 400 | Metadata, badges, and single-line helper text |
| Compact | 14px | 20px | 400 | Dense product UI: table cells, form labels, controls, log rows |
| Body | 16px | 24px | 400 | Default text, paragraphs, and any caption-length copy that wraps |
| Title | 24px | 32px | 600 | Page h1 (most pages) |
| Title lg | 30px | 36px | 600 | Hero h1 |
| Display | 36px | 40px | 600 | Large showcase text |
| Hero display | 48px | 52px | 600 | Primary or editorial hero h1 with a controlled max-width |
| Metric display | 48px | 48px | 600 | Editorial outcome metrics only. Single-line by definition — the 1.0 ratio collides the moment it wraps |

Emphasis inside a tier is one weight step up (400 to 500), never a size change.

**Where the 4px snapping costs something, and what to do about it.** The grid is right for headings, which want a ratio near 1.1: `Display` lands on 1.11 and `Hero display` on 1.08, both correct. It is tighter than ideal for text that wraps, which wants 1.5 to 1.6 and needs at least 1.4 past three lines. `Body` at 16/24 is exactly 1.5, which is why the base tier is the one to reach for whenever copy actually flows. `Compact` at 14/20 is 1.43, fine for the one- and two-line UI strings it exists for. `Caption` at 12/16 is 1.33, which is under the floor — so `Caption` is for metadata and single-line helper text only, and anything caption-shaped that wraps moves up to `Body` rather than being set tighter. At 14px the grid offers only 16, 20 or 24, and none of them lands in the 1.5–1.6 band; that is a real limit of snapping line height to a 4px rhythm, not an oversight, and the way out is choosing the right tier rather than breaking the grid.

### Measure
Cap long-form text at **60 to 75 characters per line**. Any unit does the job as long as a cap exists and the rendered line lands in that range; on this site's 1200px shell an uncapped paragraph runs roughly twice that, which is illegible for a reason that has nothing to do with size or contrast. Headings and short display copy don't need a cap, they need a deliberate `max-width` chosen for the wrap.

Hero `h1` copy does not use terminal punctuation. Keep the final line visually open: no full stop at the end.

### Installing Geist
Vercel's own `geist` npm package is the recommended method for any project: full glyph set and `font-feature-settings` support, which the Google Fonts / `next/font/google` route doesn't have. `npm i geist`, then `import { GeistSans } from 'geist/font/sans'` (same for `geist/font/mono` and `geist/font/pixel`). This site itself self-hosts via `@fontsource-variable/geist(-mono)` and `@fontsource/geist-pixel`, a convenient pre-bundled distribution rather than the officially recommended one. Recommending one route and shipping another is a defect in this document, not a nuance: either the recommendation is wrong for this system, or this site should move to `geist`. Until that is decided, **new projects follow the recommendation above and use `geist`**; this site is the known exception, not the example to copy.

## Layout & Composition

Applies Principle 1 concretely:

- Page shell: centered column, max-width 1200px, with a border on its left and right edges running the full page height. The page reads as one bordered document, not a bare canvas.
- Any grid of same-rank blocks (nav items, content-block tiles, asset previews): the container gets the leading borders (top and left), every cell gets its own trailing borders (right and bottom), and there's no gap between cells. This produces exactly one line at every seam regardless of how many rows or columns, including an uneven last row.
- When column count changes per breakpoint, the "rightmost cell has no trailing right border" rule has to be re-targeted per breakpoint with `nth-child`, since which cell is rightmost changes with the column count. Scope each breakpoint's `nth-child` removal to that breakpoint's own range (e.g. `max-sm:`, `sm:max-lg:`, `lg:`), not an open-ended `sm:`/unprefixed rule. An `nth-child` selector outranks a plain trailing-border utility in specificity, so a rule left unscoped at a smaller breakpoint keeps winning at every larger one instead of the border being restored there, silently dropping most of the grid's dividers.
- No rounded corners anywhere, no exceptions: cards, grids, containers, buttons, chips, overlays. One master switch drives this: `--radius: 0rem` in `:root`. Every `rounded-sm/md/lg/xl/2xl/3xl/4xl` utility is mapped, via `@theme`, to a multiple of `var(--radius)`, so it collapses to a square automatically wherever it's used, project-wide, without touching individual components. `rounded-full` (a circular control: Switch's track, Avatar, a status dot) is untouched by this, it's a shape choice, not a corner-radius choice. A component using a literal arbitrary radius (`rounded-[4px]`) instead of the theme scale is a bug: it silently opts out of the master switch.
- Spacing and sizing grid: every padding, gap, and height is a multiple of **4px**, no half-steps (`px-2.5`, `py-1.5`, `gap-1.5`, and so on). This is enforced, not a guideline. Round to the nearest 4px multiple before shipping.

## Components

Components are the shadcn/ui set: same variant logic, Geist Sans on ordinary controls (not Mono), overlay treatment of a `scrim` token with `border` + `shadow`, not a ring. Corner radius needs no per-component override, it comes from the master `--radius: 0rem` switch below. One deliberate exception: fill color on ordinary chrome (see Button below).

### Button, Badge
**Role:** All interactive actions (Button); status/count chrome (Badge).

- **Fill:** the default variant is `bg-foreground` / `text-background`, an inverted-neutral fill, not the brand primary color. Primary is used punctually, for one specific deliberately-branded moment, not as the everyday button/badge fill. That moment is the "Download design.md" CTA in the header of the overview page: `bg-primary` / `text-primary-foreground`, an explicit override on top of the `default` variant. Every other button on the site stays inverted-neutral. Destructive keeps a solid `bg-destructive` fill, not a subtle tint. Text on any solid fill uses the matching `-foreground` token (`background`, `destructive-foreground`), never a literal `text-white`, since a literal white fails contrast against some of this brand's own colors (verified: white on `#2ECF8F` is 2.01:1).
- **Button size scale:** `default` 36px height and 16px horizontal padding, `sm` 32px and 12px, `lg` 44px and 24px, `xs` 28px and 8px, icon-only `36px` (default) or `24px` (compact). No in-between size. The compact step was `20px`, which sits under WCAG 2.5.8's 24×24 baseline and only passed through the spacing exception — true wherever it was used, but the rule offered the size without the condition, so nothing stopped two of them landing side by side. Default and large text labels stay at 14px; increasing the touch target must not increase their type size. Small and extra-small labels use 12px.
- **Icon use:** a button includes an icon whenever an available icon communicates its action clearly. The icon supports the label and is never added only as decoration. Use an icon-only button only when the action is unambiguous, and always give it an accessible name. If no icon meaningfully represents the action, keep the button text-only.
- **Icon glyphs inside buttons:** 14px for inline and default context, or 20px for large or icon-only buttons. 16px is explicitly disallowed, since it falls between the two intentional steps.

### Overlays (Dialog, Alert Dialog, Sheet, Drawer, Popover, Dropdown Menu, Select, Command, Tooltip)
**Role:** Floating, portal-rendered content: modals, side panels, menus, comboboxes, tooltips.

Scrim is the `scrim` token (`bg-scrim`), no blur. It is translucent rather than a hex, which is deliberate and not an exception to the all-hex rule: a scrim is a fill, and a fill that tracks what sits behind it is doing its job — the opposite of ink, where the same property is a failure (see [`design/media.md`](design/media.md)). What matters is that no component ships it as a literal `bg-black/80`. Content surface is `border` + `shadow`, not a ring. Square corners come from the same master `--radius: 0rem` switch as everything else, not a per-component override. Drawer's default direction is `right`.

Select and Dropdown Menu lock body scroll while open (`react-remove-scroll`), which injects a compensating `margin-right` for the scrollbar it hides. This site already reserves that space permanently via `scrollbar-gutter: stable` on `html`, so the injected margin double-compensates and the page visibly shifts open/close. Neutralized with `body[data-scroll-locked] { margin-right: 0 !important; padding-right: 0 !important; }`. Needed on any project that combines `scrollbar-gutter: stable` with Radix primitives that lock scroll.

### Tabs
**Role:** Switching between sibling views without navigating.

The active-tab highlight is an animated pill (`motion`, shared `layoutId` between triggers), not a static background swap: it slides from the previous active trigger to the new one. Each `Tabs` instance generates its own `layoutId` internally (via `React.useId`), so multiple independent tab groups on one page never animate into each other.

### Avatar
**Role:** Representing a person or identity.

Two distinct tools, not one component with two modes: a real uploaded photo uses the plain Radix Avatar (`Image` + `Fallback`, circular) or a plain `<img>`, `rounded-full`. An identity with no photo uses `avvvatars-react` instead of initials-in-a-circle: a deterministic identicon from a string (email, user id). Radius depends on context, not a fixed value: `radius={size / 2}` for a perfect circle where it sits next to real circular photos in the same list (a team row), a smaller fixed radius like `8` for a standalone profile card where it isn't matched against photos.

### Card patterns
**Role:** Grouping related content on a surface.

The bare `Card` primitive is a shell; real usage falls into a handful of recurring patterns, not ad hoc composition each time:
- **Stat/metric tile:** `CardContent` with a big `font-mono text-2xl font-semibold` number next to a delta pill (square, `bg-success/10 text-success` or `bg-destructive/10 text-destructive`, arrow icon + `%`), then a `text-xs uppercase tracking-wide` muted label, then either a compact sparkline or a plain muted detail line. The sparkline is an `AreaChart` (gradient fill, no axis) over a decorative dotted-grid background (`radial-gradient(var(--border) 1px, transparent 1px)`, masked to an ellipse so it fades at the edges), with the date range in `font-pixel` underneath.
- **Editorial outcome metric:** a 20px-high logo aligned to the top-left, followed by a `font-mono text-5xl` value and a muted uppercase caption. Use a fixed 32px mobile / 40px desktop gap between the logo and value so every value and caption starts at the same height; a wrapping caption grows downward and never shifts the value upward.
- **Chart card:** `CardContent` wrapping a `ChartContainer` directly, no header, the chart is the content.
- **List/header card:** `CardHeader` with an icon + mono muted title (Section label pattern, but not uppercase, this is a card title not a page section label) and a plain muted count on the right, no header background. `CardContent` is rows of icon + name + a muted mono count, each followed by a `Progress` bar (`h-2`, not the thinner default), colored per row by cycling the eight chart tokens via `indicatorStyle`, not left at the default neutral fill. No footer, no action button, unless the card's real job is launching one specific action.
- **Basic card:** `CardHeader` (`CardTitle` + `CardDescription`) plus `CardContent`, for anything that doesn't fit the patterns above.

### Section label pattern
**Role:** Any heading that introduces a block of content.

One fixed shape, no exceptions: a label in Geist Mono, 14px, medium weight, uppercase with letter-tracking, in `primary-ink`, preceded by a 14px icon naming the subject. Never rendered without the icon.

`primary-ink`, not `primary`. This pattern used the fill token and therefore rendered every section heading on the site at `2.01:1` in light mode — the same value-in-the-wrong-role mistake as the focus ring, in the role that carries the most text. The same correction applies to link text (`Button` and `Badge`'s `link` variant) and to any glyph meant to be read in the brand color. `primary` stays for fills. The exception is a block that paints its own dark surface with `bg-foreground` without entering `.dark` scope, where the token still resolves to its light-mode value and the base green is the legible choice; `tetris-footer-29` and `feature-media-card-13` are the two instances.

## Do's and Don'ts

### Do
- Set every button label in Geist Mono, at every size and variant.
- Use `bg-foreground`/`text-background` for every button, at every size and variant. Keep the brand primary color for the marks listed under Primary.
- Keep icon glyphs at exactly 14px or 20px. Pick the step, don't interpolate.
- Round every spacing value to a 4px multiple before shipping it.
- Use the section-label pattern (Mono, 14px, uppercase, 8px Primary square first) for any heading that introduces a block. Don't invent a second heading style for the same job.
- Give same-rank blocks a shared border and no gap, and let the container cover the leading edges.

### Don't
- Don't use `size-4` (16px) icon glyphs inside buttons or anywhere a 14px/20px alternative exists. It's the one explicitly disallowed step.
- Don't fill a control with the brand primary color, or use it for links, hovers, or charts. It marks (a square, a check, a bar fill, a switch track); it never becomes the surface of a button or badge.
- Don't use half-step Tailwind spacing utilities (`px-2.5`, `py-1.5`, `gap-1.5`, `size-3.5` outside the icon-glyph rule) for padding, gap, or height. Round to the grid instead.
- Don't add rounded corners or drop shadows to structural content blocks. Flat and square is the working direction there; real CTA buttons are the only rounded exception, and utility chips reuse Button's styling minus the corner (`rounded-none`).
- Don't hand-roll a styled `<a>` or `<div>` to look like an existing component (Button, Badge, chip). Use the real component so it never drifts from it.
- Don't invent a 4th status tone, a new chart color, or a synonym for an existing term "just this once."

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Typography: Font Families */
  --font-sans: 'Geist Variable', ui-sans-serif, system-ui, sans-serif;
  --font-mono: 'Geist Mono Variable', ui-monospace, SFMono-Regular, Menlo, monospace;
  --font-pixel: 'Geist Pixel', ui-monospace, monospace;

  /* Typography: Base */
  --text-base: 16px;

  /* Spacing */
  --spacing-unit: 4px;
}
```

### Tailwind v4

```css
@theme {
  --font-sans: 'Geist Variable', ui-sans-serif, system-ui, sans-serif;
  --font-mono: 'Geist Mono Variable', ui-monospace, SFMono-Regular, Menlo, monospace;
  --font-pixel: 'Geist Pixel', ui-monospace, monospace;
}
```

Button, section-label, and layout rules above aren't tokens. They're usage rules layered on top of whichever component library ships the base primitives (this system uses shadcn/ui with Radix underneath, restyled only at the token and class layer, never restructured, see Principle 11).

## Open

Not decided yet. Don't fill these in speculatively:
- Logo usage rules (minimum clear space, minimum size, what not to do) beyond the mark itself existing.
- The rest of the shadcn/ui catalog. The Components section below settles Button, Badge, the overlay family, Tabs, Avatar, and the Card patterns; the roughly twenty other primitives on `/components/` are themed but unspecified, and are marked `Undocumented` there rather than being left to look approved.
- Reusable content blocks for product pages (hero, features, CTA, pricing, footer).
- Border radius (beyond buttons and chips) and shadow/elevation rules for overlays.
- Whether this site moves to the `geist` npm package, which is what the Typography section recommends for everyone else.

## Relationship to the product's own design doc

`company_brain/frontend/design.md` in the product repo is a decision log for the Brain app: what was tried on a given screen, what was rejected, and why. It is not a second style reference and must not restate anything settled here. Where the two disagree, this file wins, per the Guidance map at the top.

Two divergences are legitimate rather than drift, and are worth naming so nobody "fixes" them:
- The app runs its default text at the `Compact` tier (14px), because it is a dense operational tool. That is a named tier in the scale above, not an override of the 16px base.
- The app carries Coral-era satellite tokens (`--accent-subtle`, `--accent-ink`, `--surface`, `--fresh`/`--aging`, and so on) that this system has no equivalent for. They exist only to keep unported screens rendering and are being retired screen by screen. Never introduce one into a new surface.

Everything else that appears in both places is a bug in the app's doc, not a local variant. Three rules in particular were re-derived from first principles during an audit of the app and landed on the opposite answer to this system's; this system's answer stands, and the reasoning is recorded where each rule lives:
- Icon glyph sizes are the two fixed steps in [`design/icons.md`](design/icons.md), not sizes relative to adjacent text.
- Icon stroke weight is Lucide's default held constant across a surface, not tuned per instance to the adjacent font weight.
- Grouping between same-rank blocks comes from a shared border, with the spacing tiers scoped as described in Principle 1.
