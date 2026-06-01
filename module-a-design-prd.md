# Module A — Design PRD
## UTAKATA LAB ウタカタ・ラボ · AI Digital Marketing Lab

**Version:** 1.0  
**Date:** 2026-05-22  
**Status:** Finalized - Long Light palette (2026-05-22)

---

## 1. Design Philosophy

UTAKATA LAB is an AI-powered digital marketing lab. The visual identity should feel intelligent without being cold, minimal without being bare, and bilingual without being awkward.

### 1.1 Aesthetic Philosophy

UTAKATA LAB is named after the Japanese word for ephemeral bubbles on water — fleeting, small, but real. The visual language must carry this tension: human scale against vast time and space.

**Core principles:**

- **Real over decorative.** No empty flourishes. Every visual element must earn its place.
- **Human warmth.** The site should feel made by a person, not a brand machine.
- **Sublime undertone.** Space, scale, and restraint that quietly suggest: the world is large, time is infinite, a human life is brief — and yet here is someone making something.
- **Courage in simplicity.** The confidence to leave space empty. The confidence to say less.

**Avoid:** trend-chasing aesthetics, AI-generated generic visuals, anything that feels corporate or performed.

**Aim for:** the feeling of a thoughtful person working at the edge of something large.

---

### 1.2 Design Direction

**North star reference:** Anthropic.com — generous white space, strong typographic hierarchy, deliberate restraint. Not a strict imitation; the UTAKATA LAB aesthetic is warmer and more personal. See Section 9 for the full Anthropic.com design comparison.

**Palette:** "02 / Long Light" — warm forest sage, ember orange, and cream. Every color has a natural, slightly desaturated character. No pure black, no pure white, no cool grays.

**Three design principles:**

1. **Content first.** Layout disappears; the work speaks. No decorative chrome that competes with project showcases.
2. **Quiet confidence.** Typography and spacing do the heavy lifting. Accent colors appear sparingly, not as wallpaper.
3. **Bilingual as a feature, not an afterthought.** Japanese and English coexist with equal visual weight. Font pairing must work in both scripts simultaneously.

---

## 2. Color System

> **Status:** ✅ Palette finalized — "02 / LONG LIGHT"
> All values are confirmed and ready for the Module E build. Replace any previous placeholder hex values with those below.

### 2.1 Palette Identity: Long Light

*"Time passing. Soft light holds everything briefly."*

The palette is drawn from natural, desaturated tones — forest sage, warm cream, ember orange — evoking quiet outdoor light. It reads sophisticated and human simultaneously, avoiding both sterile tech-blue and generic warm-minimal clichés.

### 2.2 Base Palette (60% + 30%)

Five steps from deep to light, all warm-neutrals with a subtle sage-green undertone.

| Step | Token | Hex | Name | Primary Usage |
|------|-------|-----|------|---------------|
| 1 — Deepest | `--color-deep` | `#1B1F1E` | Deep Forest | Primary text, dark card backgrounds |
| 2 — Dark | `--color-dark` | `#4A524A` | Sage Dark | Dark card surface, secondary text on light |
| 3 — Mid | `--color-mid` | `#7D8278` | Sage Gray | Tertiary text, dividers, placeholder |
| 4 — Light | `--color-light` | `#D8D6CE` | Warm Gray | Borders, inactive states, light dividers |
| 5 — Lightest | `--color-bg` | `#F2EEE6` | Warm Cream | Page background, card backgrounds |

**Usage ratio guidance (from palette spec):** 60% base neutrals (steps 4–5) · 30% mid-tones (steps 2–3) · 10% accent colors.

### 2.3 Semantic Token Mapping

All components reference semantic tokens, not raw steps. This makes future theme changes a single-file operation.

| Role | Token | Resolves to | Usage |
|------|-------|-------------|-------|
| Background | `--color-bg` | `#F2EEE6` | Page background |
| Surface (light card) | `--color-surface` | `#F2EEE6` + slight contrast | Elevated cards on warm cream bg |
| Surface (dark card) | `--color-surface-dark` | `#4A524A` | Featured/dark card backgrounds |
| Text Primary | `--color-text-primary` | `#1B1F1E` | Headings, body copy on light bg |
| Text on Dark | `--color-text-on-dark` | `#F2EEE6` | Body copy on dark card surfaces |
| Text Secondary | `--color-text-secondary` | `#4A524A` | Captions, labels, metadata on light bg |
| Text Tertiary | `--color-text-tertiary` | `#7D8278` | Placeholder text, dividers |
| Border | `--color-border` | `#D8D6CE` | Card outlines, input borders, dividers |
| Accent (primary) | `--color-accent` | `#C47A3A` | CTAs, hover underlines, active states, links |
| Accent Hover | `--color-accent-hover` | `#A8612A` | Button/link hover (darkened ~15%) |
| Accent Light | `--color-accent-light` | `#E7C5B6` | Secondary accent, highlights, warm tint |
| Overlay | `--color-overlay` | `rgba(27,31,30, 0.55)` | Card hover scrim, modal backdrop |

> ✅ **Pale Dusk hex confirmed:** `#E7C5B6` (warm dusty blush).

### 2.4 Accent Colors

| Swatch | Token | Hex | Name | Usage |
|--------|-------|-----|------|-------|
| 🟠 | `--color-accent` | `#C47A3A` | Soft Ember | Primary CTA buttons, active nav dots, link arrows |
| 🍑 | `--color-accent-light` | `#E7C5B6` | Pale Dusk | Hover tints, card highlight borders, subtle warmth |

**Accent usage rules:**
- Soft Ember (`#C47A3A`) is the **only** action color. All buttons, links, "View →" arrows, and active indicators use it.
- Pale Dusk (`#E7C5B6`) is a **supporting warm tint** — never on text, never on interactive elements. Use for background washes, card border highlights, or decorative accents only.
- Neither accent appears as page-level background color. Accent is always a 10% presence — not wallpaper.

### 2.5 Color Pairing Examples

From the palette spec — three validated pairings:

| Pairing | Foreground | Background | Use case |
|---------|-----------|------------|---------|
| High contrast | `#1B1F1E` | `#C47A3A` | Avoid — too heavy for large areas |
| Dark + Ember | `#C47A3A` | `#4A524A` | Dark card CTAs ("View project →") |
| Light + Ember | `#C47A3A` | `#F2EEE6` | Standard page CTAs, text links |
| Neutral pair | `#7D8278` | `#F2EEE6` | Metadata, secondary text on page |

### 2.6 Dark Mode

Not in scope for v1. The two-surface architecture (light cream + dark sage) already provides natural visual contrast without a full dark mode. Architecture must not block a future theme toggle — all colors are CSS custom properties in `:root`.

---

## 3. Typography

> **Status:** ✅ Type system confirmed via palette spec.

### 3.1 Three-Font System

UTAKATA LAB uses a **three-role type system** confirmed by the palette design:

| Role | Latin | Japanese | Weight | Source |
|------|-------|----------|--------|--------|
| **Display / Hero** | [DM Serif Display](https://fonts.google.com/specimen/DM+Serif+Display) | Noto Serif JP | 400 (Regular) | Google Fonts |
| **Heading / UI** | [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) | Noto Sans JP | 600 (SemiBold) | Google Fonts |
| **Body / Prose** | [Inter](https://fonts.google.com/specimen/Inter) | Noto Sans JP | 400 (Regular) | Google Fonts |
| **Mono / Code** | [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) | — | 400 | Google Fonts |

**Role clarity:**

- **DM Serif Display** → hero studio name, feature headlines, large display moments only. Always large (≥ 36px). Never in UI chrome or body copy. Creates the "editorial weight" of the page.
- **Space Grotesk** → navigation labels, section headings, card titles, buttons, tags, all UI text. Geometric, confident, contemporary. Its slightly quirky terminals give UTAKATA LAB personality without being decorative.
- **Inter** → body paragraphs, project descriptions, captions. Neutral, highly readable, pairs cleanly with both Noto JP variants.

> **Design rationale:** Space Grotesk was chosen (over the earlier DM Serif Display-led approach) for UI headings because it gives the brand a distinctive geometric identity — less editorial magazine, more intelligent studio. The serif is reserved for the moments that need weight and warmth, not used everywhere.

### 3.2 Font Pairing in Practice

```
Hero headline:       DM Serif Display 400, large (56px+)
                     "Small things. Real moments."

Section heading:     Space Grotesk 600, medium (20–30px)
                     "Latest Work"

Card title:          Space Grotesk 600, body-scale (18–20px)
                     "Project Name"

Body paragraph:      Inter 400, 16–18px
                     "A short description of the project…"

Nav link:            Space Grotesk 400–600, 14–16px
                     "Works · Thoughts · About"

Tag / label:         Space Grotesk 600, 12px, uppercase tracked
                     "BRANDING"
```

### 3.3 Font Loading Strategy

Load only the weights in active use to keep page weight under ~130KB:

| Font | Weights to load | Approx size |
|------|----------------|-------------|
| DM Serif Display | 400 only | ~20KB |
| Space Grotesk | 400, 600 | ~35KB |
| Inter | 400, 500 | ~35KB |
| Noto Sans JP | 400, 500 | ~25KB subset |
| Noto Serif JP | 400 only | ~15KB subset |

Use `font-display: swap` on all `@font-face` declarations to prevent invisible text during load.

### 3.4 Type Scale

All values in `rem` (base: 16px). Token names map directly to CSS custom properties.

| Token | rem | px equiv | Font | Usage |
|-------|-----|----------|------|-------|
| `--text-xs` | 0.75rem | 12px | Space Grotesk | Tags, labels, fine print |
| `--text-sm` | 0.875rem | 14px | Space Grotesk | Navigation, captions, metadata |
| `--text-base` | 1rem | 16px | Inter | Body copy |
| `--text-lg` | 1.125rem | 18px | Inter | Lead paragraphs, card descriptions |
| `--text-xl` | 1.25rem | 20px | Space Grotesk | Card titles, section subheadings |
| `--text-2xl` | 1.5rem | 24px | Space Grotesk | Section headings |
| `--text-3xl` | 1.875rem | 30px | Space Grotesk | Page-level headings |
| `--text-4xl` | 2.25rem | 36px | DM Serif Display | Hero subtitle / secondary display |
| `--text-display` | 3.5rem | 56px | DM Serif Display | Studio name / hero display (desktop) |
| `--text-display-sm` | 2.5rem | 40px | DM Serif Display | Studio name / hero display (mobile) |

### 3.5 Line Heights and Letter Spacing

| Context | Line Height | Letter Spacing | Notes |
|---------|-------------|----------------|-------|
| Body (Inter) | `1.7` | `0` | Generous for mixed-script readability |
| UI Headings (Space Grotesk) | `1.2` | `0` | Tight, editorial |
| Tags / Labels (Space Grotesk) | `1` | `0.06em` | Uppercase labels need tracking |
| Japanese body | `1.9` | `0` | Japanese requires more leading than Latin |
| Display (DM Serif) | `1.1` | `-0.02em` | Optical tightening at large sizes |

---

## 4. Layout System

### 4.1 Grid

Single-column on mobile; shifting to a 12-column grid on desktop.

| Breakpoint | Token | Value | Notes |
|------------|-------|-------|-------|
| Mobile | `--bp-sm` | 375px | Base layout, single column |
| Tablet | `--bp-md` | 768px | Two-column portfolio grid unlocks |
| Desktop | `--bp-lg` | 1024px | Full 12-column grid, side-by-side sections |
| Wide | `--bp-xl` | 1280px | Max content width caps here |

**Max content width:** `--max-width: 1200px` — centered with `margin: 0 auto`.

### 4.2 Spacing Scale

Consistent 8px base unit. Token names reflect the multiplier.

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 4px | Tight internal gaps (icon + label) |
| `--space-2` | 8px | Input padding, small gaps |
| `--space-3` | 12px | Tag padding |
| `--space-4` | 16px | Card internal padding (mobile) |
| `--space-6` | 24px | Section sub-gaps |
| `--space-8` | 32px | Card internal padding (desktop), between elements |
| `--space-12` | 48px | Between sections (mobile) |
| `--space-16` | 64px | Between sections (desktop) |
| `--space-24` | 96px | Hero section top padding |
| `--space-32` | 128px | Large section breathing room |

### 4.3 Layout Principles

- **Vertical rhythm:** All vertical gaps follow the 8px scale. No arbitrary pixel values.
- **Horizontal margins:** `5vw` on mobile, `max-width` container on desktop — never full bleed text.
- **Section rhythm:** Hero → About → Portfolio → Contact follows a visual weight descending curve: bold opening, quieter close.
- **Alignment:** Left-aligned for Japanese/mixed content (centered Japanese is harder to read at body sizes).

---

## 5. Component Definitions

### 5.1 Navigation / Header

- **Position:** Fixed top on desktop, sticky on mobile
- **Contents:** Logo/studio name (left) · Language toggle (right) · optional nav links (center, hidden mobile)
- **Height:** 60px desktop, 52px mobile
- **Behavior:** Transparent at page top; gains `background-color: var(--color-bg)` + subtle `box-shadow` on scroll
- **Language toggle:** Pill-style button — `EN | JP` — active state is filled, inactive is ghost

### 5.2 Hero Section

- **Layout:** Full viewport height (100svh) on desktop. **Two-column grid** on desktop (`55% / 45%`): copy left, illustration right. Single column on mobile (copy above, illustration below).
- **Content:** Studio name (display type) · tagline · one-sentence positioning statement · single CTA button
- **Hero illustration:** Flat vector-style illustration of a human and AI in dialogue. Borderless — floats directly on the warm cream background. CSS-filtered to harmonize with the Long Light palette (`hue-rotate(-22deg) saturate(0.87) brightness(1.03)`). Image file: `hero-illustration.png` in the project root.
- **Illustration rationale:** Communicates the human-AI collaboration theme of the lab without generic stock photography. Flat style reads as "crafted," consistent with the studio's "made by a person, not a brand machine" principle.
- **Scroll indicator:** Line indicator at bottom center

### 5.3 Portfolio Card

This is the primary interactive component. Cards display project work in the portfolio grid.

**States:**

| State | Description |
|-------|-------------|
| Default | Title + short descriptor (2 lines max) + tags. Clean, minimal. |
| Hover (desktop) | Card lifts (`translateY(-4px)` + `box-shadow`). Expanded area reveals fuller description (3–4 lines) + a "View →" link. Transition: `0.25s ease`. |
| Tap/Focus (mobile) | Same expansion triggered by tap, not hover. Requires JS toggle class. |
| Expanded | Max height reveals project details, tags, and action link. |

**Anatomy:**

```
┌─────────────────────────────────┐
│  [Image slice / color block]    │  ← 160px height, object-fit: cover
│─────────────────────────────────│
│  Project Title           [Tag]  │  ← text-xl, bold
│  Short description line 1       │  ← text-base, secondary color
│  Short description line 2       │
│─────────────────────────────────│  ← Revealed on hover/expand
│  Extended description here,     │
│  up to 3–4 lines of detail.     │
│                                 │
│  View project →                 │  ← Accent color link
└─────────────────────────────────┘
```

**Card grid:** 1 column mobile → 2 columns at md → 2–3 columns at lg (max 3 per row)

**New card insertion:** Each card is a self-contained `<article class="card">` block. Adding a new project = inserting one new `<article>` block. Documented in Module C.

### 5.4 Tags / Labels

- Pill shape: `border-radius: 999px`
- Size: `text-xs`, `padding: 3px 10px`, Space Grotesk SemiBold, uppercase, letter-spacing `0.06em`
- Variants: Outlined (default) · Filled (accent, for featured)
- Colors on light surface: border `#D8D6CE`, text `#4A524A`; filled uses `#C47A3A` bg with `#F2EEE6` text
- Colors on dark surface: border `rgba(242,238,230,0.25)`, text `#D8D6CE`

### 5.5 Buttons

| Variant | Usage | Background | Text | Border |
|---------|-------|-----------|------|--------|
| Primary | Main CTA (hero, contact) | `#C47A3A` (Soft Ember) | `#F2EEE6` (Warm Cream) | none |
| Primary on Dark | CTA on dark card surface | `#C47A3A` | `#F2EEE6` | none |
| Secondary | Secondary actions | transparent | `#C47A3A` | `1.5px solid #C47A3A` |
| Ghost / Text | Nav links, "View →" | none | `#C47A3A` | none |

- Height: 48px (touch-friendly), padding: `12px 28px`
- Border-radius: `6px` for filled/outlined; none for ghost text links
- Hover: Primary button darkens to `#A8612A` + subtle `box-shadow: 0 4px 12px rgba(196,122,58,0.25)` — warm amber glow lift
- Focus: `outline: 2px solid var(--color-accent)` with `outline-offset: 3px` (accessibility)
- Arrow suffix "→" on primary and ghost CTAs (matches palette spec UI examples)

### 5.6 Language Toggle

- Position: Top-right of header
- Behavior: Clicking switches the `lang` data attribute on `<html>` tag; JS shows/hides elements with `data-lang="en"` or `data-lang="jp"`
- Visual: Active language label is filled/bold; inactive is muted
- No page reload

### 5.7 Section Dividers

- No decorative lines unless structural
- Use white space (spacing tokens) as the primary section separator
- Optional: A single `1px` border in `--color-border` between major sections if content density demands it

### 5.8 Contact / CTA Section

- Minimal: One headline + one email address or contact form link
- Matches footer function — low visual weight, no competing elements
- Optional: Social links as icon-only buttons (GitHub, LinkedIn, X/Twitter)

---

## 6. Motion and Interaction

### 6.1 Animation Principles

- **Purposeful:** Animation communicates state change, not decoration
- **Fast and subtle:** All transitions ≤ 300ms; prefer `ease` or `cubic-bezier(0.4, 0, 0.2, 1)`
- **Respect preferences:** Wrap all non-essential animation in `@media (prefers-reduced-motion: no-preference)`

### 6.2 Defined Transitions

| Trigger | Property | Duration | Easing |
|---------|----------|----------|--------|
| Card hover | `transform`, `box-shadow` | 250ms | ease |
| Card expand | `max-height`, `opacity` | 300ms | ease-in-out |
| Header scroll | `background`, `box-shadow` | 200ms | ease |
| Button hover | `transform`, `box-shadow` | 150ms | ease |
| Language toggle | `opacity` on content | 200ms | ease |
| Page load | `opacity` on hero | 500ms | ease (one-time) |

---

## 7. Accessibility Baseline

- **Color contrast:** All text on background meets WCAG 2.1 AA (4.5:1 for body, 3:1 for large text)
- **Focus states:** Visible for all interactive elements (keyboard navigation)
- **Language attribute:** `<html lang="ja">` or `lang="en"` switches with toggle — critical for screen reader correct pronunciation
- **Alt text:** All portfolio images require descriptive `alt` attributes
- **Touch targets:** Minimum 44×44px for all interactive elements on mobile

---

## 9. Anthropic.com Design Reference — Live Analysis

> **Purpose:** This section documents the actual design system observed on [anthropic.com](https://www.anthropic.com/) as of May 2026, extracted directly from the live site via browser inspection. It serves as the concrete reference point for UTAKATA LAB's "north star" aesthetic — not a template to copy, but a benchmark to consciously adapt from.

---

### 9.1 Screenshot Reference

The page at the time of analysis:

- **Above the fold:** Warm cream background, wordmark "ANTHROPIC\" in all-caps sans-serif (top-left), minimal nav (top-center), black pill CTA "Try Claude" (top-right). Hero body text is a serif, right-aligned at ~24px, sitting in generous white space.
- **Featured card:** Full-width dark block (`#141413` background) with generative geometric art (hexagonal mesh pattern). Display headline uses large serif type at ~96px — dramatic contrast against the surrounding cream.
- **Content cards:** Three equal cards in a warm beige / sandy tone, rounded corners (~16px radius), no visible border, with sans-serif labels and serif body.

---

### 9.2 Color Palette — Extracted Values

| Role | Observed Value | CSS Variable / Name |
|------|---------------|---------------------|
| Page background | `#FAF9F5` (warm cream) | Body `background-color` |
| Primary text | `#141413` (warm near-black) | Body `color` |
| Border / divider | `rgba(20,20,19, 0.10)` | `--_color-theme---border` |
| Accent / clay | `#D97757` (terracotta) | `--swatch--clay` |
| Dark section bg | `~#1A1A18` (rich black) | Featured card background |
| Card surface | `~#E8E3DA` (warm sand) | Content card background |
| CTA button bg | `#141413` (near-black filled) | "Try Claude" button |
| CTA button text | `#FAF9F5` (cream) | "Try Claude" button |

**Key insight:** Anthropic's palette is entirely warm-toned — no cool grays, no pure whites, no pure black. Every value has a subtle warm undertone. This creates cohesion across light and dark surfaces.

**UTAKATA LAB adaptation:** The existing placeholder palette (`#F5F4F0` bg, `#1C1C1C` text, `#E8604C` accent) correctly captures this warm-neutral direction. The main calibration point is the accent: Anthropic's clay (`#D97757`) is more muted and earthy than UTAKATA LAB's current coral (`#E8604C`). Owner should decide on final tone when resolving the TBD color palette.

---

### 9.3 Typography — Extracted Values

Anthropic uses a **proprietary typeface pair** that is not publicly available:

| Role | Font | Fallback |
|------|------|----------|
| Body & Display | `Anthropic Serif` | `Georgia, sans-serif` |
| UI / Headings | `Anthropic Sans` | `Arial, sans-serif` |

**Key insight:** Contrary to typical tech-brand convention, Anthropic uses **serif as the dominant typeface** — for body copy, hero text, and large display moments. Sans-serif appears only for UI chrome (navigation, labels, metadata). This gives the site an editorial, intellectual quality — more _The Atlantic_ than _Vercel_.

**Observed type scale:**

| Element | Size | Weight | Line-height | Notes |
|---------|------|--------|-------------|-------|
| Hero / Featured display | 96px | 400 (regular) | 1.1 | Serif — large and light, not bold |
| H1 | 64px | 700 | 1.1 | Sans — nav-context headings |
| Body paragraph | 24px | 400 | 1.4 | Serif — generous size for readability |
| Nav links | 20px | 400 | — | Serif |
| Card labels | ~13px | 600 | — | Sans, uppercase tracked |

**UTAKATA LAB adaptation:** UTAKATA LAB's PRD uses DM Serif Display + Inter. This directionally matches Anthropic's approach (serif-led, sans for UI) but with publicly available fonts. The UTAKATA LAB type scale is well-calibrated — no revision needed. The key principle to carry over: **big serif display type should be light weight (400), not bold** — boldness comes from scale, not weight.

---

### 9.4 Layout & Spacing

| Property | Anthropic Value | Notes |
|----------|----------------|-------|
| Max content width | `min(89.5rem, 100vw)` ≈ 1432px | Wider than UTAKATA LAB's 1200px |
| Horizontal margin | `clamp(2rem, ~4vw, 5rem)` | Fluid gutters |
| Vertical section spacing | `clamp(3.5rem → 6rem)` | Fluid, ~56–96px |
| Card grid | 3-column equal | At desktop breakpoint |
| Card border-radius | ~16px | Soft, not sharp |
| Grid system | 12-column with fluid margins | CSS Grid with named lines |

**Key insight:** All spacing uses `clamp()` for fluid responsive scaling — no fixed pixel breakpoints for padding. This means the layout breathes at every viewport width, not just at defined breakpoints.

**UTAKATA LAB adaptation:** The existing 8px base spacing scale is correct. Consider adopting `clamp()` for section-level spacing in Module E to match this fluidity. UTAKATA LAB's `--max-width: 1200px` is intentionally narrower (more focused, personal studio feel — appropriate given the single-person context).

---

### 9.5 Navigation

| Property | Observed |
|----------|---------|
| Position | Fixed top |
| Background | Transparent → `#FAF9F5` on scroll (subtle transition) |
| Logo behavior | Full wordmark "ANTHROPIC\" at page top → condensed "A\" monogram on scroll |
| Nav links | Center-aligned, serif, ~20px |
| CTA button | Right-aligned, black filled pill, "Try Claude" |
| CTA dropdown | Split-button with a chevron for secondary actions |

---

### 9.6 Visual Accent: Generative / Geometric Art

Anthropic's signature visual motif is **procedural / generative art** — abstract geometric forms (cellular meshes, particle systems, organic structures). These appear:
- As full-bleed background images in dark feature cards
- As subtle textures and overlays
- Rendered in muted tones that don't compete with text

**UTAKATA LAB adaptation:** The existing PRD flags "gradient blob or noise texture" as the hero accent option. Anthropic's execution confirms this is the right direction. Recommendation: use a subtle SVG or CSS-based abstract form (particle dots, soft mesh, or ink-wash texture) that renders without heavy JS. Avoid photography in the hero — keep it abstract and typographic.

---

### 9.7 Summary: What UTAKATA LAB Takes from Anthropic, and What It Diverges On

| Dimension | Anthropic | UTAKATA LAB (from Anthropic) | UTAKATA LAB Divergence |
|-----------|-----------|--------------------------|-------------------|
| Background | Warm cream `#FAF9F5` | ✅ Same direction | Slightly more off-white warmth |
| Text | Warm near-black `#141413` | ✅ Same direction | — |
| Accent | Terracotta `#D97757` | Coral `#E8604C` (TBD) | More saturated / personal |
| Serif lead | Proprietary Anthropic Serif | DM Serif Display (display only) | Inter leads in body — more accessible |
| Type scale | Serif-dominant across all sizes | Serif for display, Inter for body | More conventional tech hierarchy |
| Layout width | 1432px max | 1200px max | Narrower, more focused |
| Dark sections | Full-bleed dark cards | Optional — not specified | Could add for featured work |
| Language | English only | Bilingual EN/JP | UTAKATA LAB's key differentiator |
| Tone | Corporate / institutional | Personal / warm / studio | More human, less formal |

---

## 8. Open Items for Owner Resolution

| Item | Current State | Notes |
|------|---------------|-------|
| ~~Final color palette~~ | ✅ **Resolved** — "Long Light" palette confirmed | All hex values locked: base 5-step + Soft Ember `#C47A3A` + Pale Dusk `#E7C5B6` |
| Hero visual accent | TBD — gradient blob vs. noise texture vs. none | Should be tested with real content before final call |
| Social link icons | Placeholder architecture included | Owner to confirm which profiles to link |
| ~~Portfolio image treatment~~ | ✅ **Resolved** — case slices available | Card 1 uses `01-hero-premium-beauty-llmo.png`; Card 2 uses `01-home.png`. Full paths and alt text specified in Module B §2.2. Ensure `object-fit: cover` at the 160px card image height defined in §5.3. |
