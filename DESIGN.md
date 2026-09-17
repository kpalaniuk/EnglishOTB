---
name: English Outside the Box
description: A sunroom of framed mid-century posters — English confidence as something warm, bright and hand-made.
colors:
  sun: "#F5C542"
  sun-deep: "#E0A426"
  honey: "#FFE79A"
  butter: "#FFF3C4"
  paper: "#FFFDF7"
  white: "#FFFFFF"
  sage: "#A9B89B"
  sage-tint: "#E9EEE2"
  clay: "#DB8353"
  clay-deep: "#A4522A"
  ink: "#2B2A28"
  ink-soft: "#4A453E"
  ink-mute: "#8B857B"
typography:
  display:
    fontFamily: "Shantell Sans, Comic Neue, Segoe Print, cursive"
    fontSize: "clamp(3rem, 2rem + 4.2vw, 5.1rem)"
    fontWeight: 700
    lineHeight: 0.98
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Shantell Sans, Comic Neue, Segoe Print, cursive"
    fontSize: "clamp(2.1rem, 1.6rem + 2vw, 3rem)"
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Shantell Sans, Comic Neue, Segoe Print, cursive"
    fontSize: "clamp(1.25rem, 1.15rem + 0.5vw, 1.5rem)"
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.01em"
  hand:
    fontFamily: "Shantell Sans, Comic Neue, Segoe Print, cursive"
    fontSize: "clamp(0.88rem, 0.85rem + 0.15vw, 0.95rem)"
    fontWeight: 400
    lineHeight: 1.4
  lede:
    fontFamily: "Nunito, Nunito Sans, system-ui, sans-serif"
    fontSize: "clamp(1.25rem, 1.15rem + 0.5vw, 1.5rem)"
    fontWeight: 400
    lineHeight: 1.45
  body:
    fontFamily: "Nunito, Nunito Sans, system-ui, sans-serif"
    fontSize: "clamp(1.05rem, 1rem + 0.25vw, 1.15rem)"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Nunito, Nunito Sans, system-ui, sans-serif"
    fontSize: "clamp(0.88rem, 0.85rem + 0.15vw, 0.95rem)"
    fontWeight: 800
    lineHeight: 1
rounded:
  none: "0px"
  mark: "4px"
  pop: "6px"
  word: "8px"
  field: "12px"
  pill: "999px"
  round: "50%"
spacing:
  mat: "12px"
  xs: "0.5rem"
  sm: "0.75rem"
  md: "1.25rem"
  lg: "1.5rem"
  xl: "2rem"
  gutter: "clamp(1rem, 4vw, 2.5rem)"
  section: "clamp(3.5rem, 8vw, 6.5rem)"
  grid-2: "clamp(1.5rem, 4vw, 3.5rem)"
  grid-3: "clamp(1.25rem, 3vw, 2.25rem)"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: "0.95rem 1.5rem"
  button-sun:
    backgroundColor: "{colors.sun}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: "0.95rem 1.5rem"
  button-sun-hover:
    backgroundColor: "{colors.honey}"
    textColor: "{colors.ink}"
  button-clay:
    backgroundColor: "{colors.clay}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: "0.95rem 1.5rem"
  button-clay-hover:
    backgroundColor: "{colors.honey}"
    textColor: "{colors.ink}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: "0.95rem 1.5rem"
  button-ghost-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
  button-white:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: "0.95rem 1.5rem"
  button-white-hover:
    backgroundColor: "{colors.butter}"
    textColor: "{colors.ink}"
  button-sm:
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.7rem 1.1rem"
  button-lg:
    typography: "{typography.lede}"
    rounded: "{rounded.pill}"
    padding: "1.1rem 1.9rem"
  nav-link:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0.55rem 0.8rem"
  nav-link-hover:
    backgroundColor: "{colors.butter}"
  nav-link-current:
    backgroundColor: "{colors.sun}"
  chip:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0.4rem 0.85rem"
  chip-hover:
    backgroundColor: "{colors.butter}"
  chip-selected:
    backgroundColor: "{colors.sun}"
  tag:
    backgroundColor: "{colors.butter}"
    textColor: "{colors.ink}"
    typography: "{typography.hand}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.75rem"
  frame:
    backgroundColor: "{colors.white}"
    rounded: "{rounded.none}"
    padding: "{spacing.mat}"
  quote:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "1.5rem 1.5rem 1.25rem"
  quote-sun:
    backgroundColor: "{colors.sun}"
    textColor: "{colors.ink}"
  plan:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "1.25rem 1.5rem"
  plan-hot:
    backgroundColor: "{colors.butter}"
    textColor: "{colors.ink}"
  episode:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "1.1rem 1.25rem 1rem"
  post-card:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "1.1rem 1.25rem 1.25rem"
  field:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    padding: "0.8rem 0.95rem"
---

# Design System: English Outside the Box

## Overview

**Creative North Star: "The Sunroom Poster Wall"**

The site is a bright room with framed posters on the wall. Whole sections are painted sunflower yellow or warm white; every photo and illustration sits inside a thin charcoal frame on a white mat, tilted a degree or two as if it were hung by hand. Headlines are hand-lettered (Shantell Sans, the same voice as the refreshed logo) and the reading text is a rounded, friendly humanist sans (Nunito). Nothing is glossy: no gradients, no drop shadows on flat surfaces, no icon-card grids. Depth comes from the 2px ink line that edges every panel, section, and button.

It is deliberately not a school and not a "premium mentor" site. It refuses the coaching-site default (hero photo, three icon cards, testimonial slider) and its dark opposite. The palette is mustard-adjacent sunshine, sage and clay from a flat paper-cut illustration set, and one charcoal ink for all lines and text. The build is a static, no-build-step site, so every rule here is expressible in plain CSS classes a future editor can copy.

Divergences from the direction contract that the build settled: clay landed at #DB8353 (the contract said #D4784A); the "1px ink rule" became the universal 2px ink line; the sun-ray badge is the hero's only ornament, while illustration plates (open box, notebook, sun) carry the rest.

**Key Characteristics:**
- Sunflower fields: yellow, butter, and sage-tint own entire sections on a warm-white page.
- The 2px ink line is the universal edge: frames, section rules, buttons, cards, nav border.
- Poster frames: white mat (12px) inside a 2px ink border, tilted -1.5° or +1.2°.
- Hand-lettered display voice over rounded humanist body.
- Pill buttons, pill chips, pill tags; rectangles everywhere else.
- Flat paper-cut illustrations and Jennifer's own photos; nothing else.
- One motion grammar: quiet fade-up on scroll, plus a single hero spring and a slow sun spin.

## Colors

A sunshine palette: one saturated yellow doing the heavy lifting, pale yellows for warmth, sage and clay as the flat-illustration companions, and a single warm charcoal for every line and letter.

### Primary
- **Sunflower** (`sun`): the field color. Owns the hero's left column, the footer, the CTA band, "sun" sections, the current nav item, the selected blog chip, text selection, `.mark` highlights, pillar 1, one featured quote, and the `most popular` plan flag. Also the `theme-color`.
- **Deep Sunflower** (`sun-deep`): pillar numerals only. The darker sibling reserved for large hand-lettered numbers on white.
- **Honey** (`honey`): the hover state for sun and clay buttons and social circles; the sun-section link color on ink.
- **Butter** (`butter`): the softest yellow. Section fill, page-hero variant, nav hover, chip hover, the featured plan card, quote provenance tags, `.tag` chips, blog blockquotes and callouts, empty post-card thumbnail background.

### Secondary
- **Sage** (`sage`): the `.mark--sage` highlight; otherwise it lives in the illustrations.
- **Sage Tint** (`sage-tint`): the quiet section fill for the student-quotes block, the Night Connections band, and the sage page-hero variant.

### Tertiary
- **Clay** (`clay`): the single most important action on a page (the Night Connections buy button, the featured plan's sign-up), the focus ring, the caret, and the dot on every provenance tag.
- **Deep Clay** (`clay-deep`): the link color in body copy, big stat numerals, post-meta links, `details` +/- markers, and episode "About this episode" summaries.

### Neutral
- **Paper** (`paper`): the page background and sticky header; form field background.
- **White** (`white`): the mat inside every frame, card and quote surfaces, the hero photo column, white sections, and button text on ink.
- **Ink** (`ink`): all headings and body text, every 2px line, the primary button, the ribbon, the ink section, the video well.
- **Soft Ink** (`ink-soft`): ledes on white, captions, meta lines, plan kinds, pillar body text, the aside.
- **Mute Ink** (`ink-mute`): placeholder text and excluded plan features only.

### Named Rules
**The One Ink Rule.** Every line, border, rule, and outline is the same charcoal ink at 2px. There is no grey border, no light divider, no second stroke color. Faded rules (`hr`, year heads) are ink at 20% opacity, never a different hue.

**The Clay Once Rule.** Clay is the saturated accent held back for the single most important action per page. Two clay buttons on one page is one too many; the rest are ink, sun, white, or ghost.

**The Field Rule.** Yellow is applied as a field that owns a whole section or column, never as a stripe, strip, or gradient. Sun, butter, and sage-tint sections alternate against white and are separated by a 2px ink line.

## Typography

**Display Font:** Shantell Sans 400/700 (with Comic Neue, Segoe Print, cursive)
**Body Font:** Nunito 400/700/800 (with Nunito Sans, system-ui)
**Hand/Caption Font:** Shantell Sans 400 at the smallest step (captions, provenance tags, `.tag`, `.pt-flag`)

**Character:** A hand-lettered, slightly bouncy display voice that matches the logo, paired with a rounded humanist sans whose 800 weight carries all buttons, nav, and meta. Headings are tight (`line-height` 1.08, tracking -0.01em, `text-wrap: balance`); reading text is loose (1.6).

### Hierarchy
- **Display** (Shantell Sans 700, `--step-5` clamp(3rem, 2rem + 4.2vw, 5.1rem), 0.98): the home hero title only; drops to `--step-4` under 900px. Also used inline for the "YES" moment.
- **Headline** (Shantell Sans 700, `--step-4` for page h1 / post h1 and `--step-3` for h2 and inner page-hero h1, 1.08): section titles, capped at 22ch (`.section__title`) or 26ch (page-hero).
- **Title** (Shantell Sans 700, `--step-2` for h3 and `--step-1` for card h3, 1.08): pillar, plan, episode, and contact-card headings. Post-card titles are a fixed 1.2rem.
- **Hero sub** (Shantell Sans 400, `--step-2`, 1.2): the one-line promise under the hero title; the "Is it possible?" beat.
- **Lede** (Nunito 400, `--step-1`, 1.45): the first paragraph of a section, soft ink on white, full ink on yellow fields; max 66ch.
- **Body** (Nunito 400, `--step-0`, 1.6): reading text; `.prose` and `.section__lead` cap at 66ch.
- **Label** (Nunito 800, `--step--1` or 0.85–0.98rem, uppercase never): buttons, nav links, chips, meta lines, plan kinds, stat captions. Bold weight does the labelling; there is no letterspaced uppercase eyebrow anywhere.
- **Hand caption** (Shantell Sans 400, `--step--1`): frame figcaptions, provenance tags, `.tag`, `.pt-flag`, quote marks, plan flag, legacy `cite`.

### Named Rules
**The Two Voices Rule.** Shantell Sans speaks the headlines, numbers, captions, and hand-written asides; Nunito speaks everything you read or click. Never set body paragraphs in the display face; never set a heading in Nunito.

**The Bold Label Rule.** Emphasis and labelling are done with Nunito 800 at sentence case. No uppercase tracking, no kickers, no eyebrows.

## Layout

A single centered column with three widths: `.wrap` at min(100% − 2×gutter, 1180px), `.wrap--mid` at 960px, `.wrap--narrow` at 780px. The gutter is clamp(1rem, 4vw, 2.5rem). Sections stack vertically with padding-block clamp(3.5rem, 8vw, 6.5rem) and alternate fills (white / butter / sun / sage-tint), each fill change marked by a 2px ink line (`.section--line-top`).

The home hero is a two-column grid (1.15fr / 1fr) with min-height min(100vh − 76px, 860px): a sunflower column on the left with the copy and box scene, a white column on the right holding the tilted poster frame and the spinning sun badge. Under 900px it stacks yellow-first, with the box scene moving inline under the copy. Inner pages open with a `.page-hero` (sun by default; butter, sage, white variants) using a 1.2fr / 0.8fr grid that collapses at 800px.

Content grids are auto-fit: `.grid-2` minmax(320px), `.grid-3` minmax(260px), quotes minmax(300px), plans minmax(290px), post cards minmax(280px). The three pillars are a single 2px-bordered bar divided by 2px ink rules that becomes a vertical stack at 800px. The footer is a 1.3fr / 1fr / 1fr / 1fr grid that goes to two columns at 860px and one at 520px. Nav collapses to a toggle-driven dropdown at 960px.

Rhythm inside components is 1.25–1.5rem padding, 0.6rem list gaps, 0.75rem button-row gaps. Headings carry 0.5em bottom margin; paragraphs 1em. The sticky header is 74px tall with a 2px ink bottom line; anchors offset by 90px.

## Elevation & Depth

The system is flat. Depth is drawn, not cast: every panel is edged by the 2px ink line and sits on a field of a different value (white on butter, white on sun, sage-tint behind white quotes). The only resting shadow is the soft poster shadow under frames and video wells, which reads as the frame standing off the wall rather than as UI elevation. Buttons, post cards, resource links, and social circles lift 2–4px on hover and pick up the same soft shadow.

### Shadow Vocabulary
- **Poster shadow** (`box-shadow: 0 10px 30px -14px rgba(43, 42, 40, .35)`): under `.frame`, `.video`, and post cards on hover. Tight, warm, low.
- **Lift shadow** (`box-shadow: 0 12px 24px -12px rgba(43,42,40,.55)`): under any `.btn` on hover, paired with translateY(-2px).

### Named Rules
**The Drawn-Depth Rule.** Surfaces are flat at rest. A shadow appears only under a poster frame or as a hover lift; no card, section, nav, or button carries a shadow at rest. No hard offset shadows, no glows, no inner shadows.

## Shapes

Two shapes only. Anything that holds content is a sharp-cornered rectangle with a 2px ink border: frames, sections, pillars, quotes, plans, episodes, post cards, stats, contact cards, callouts, the video well. Anything you press or that labels something is a full pill (999px): buttons, nav links, chips, tags, provenance tags, the plan flag, the nav toggle, series navigation, even the native audio control. Small exceptions are functional, not decorative: form fields at 12px, the hero `.pop` and springing `.word` labels at 6–8px, the `.mark` highlight at 4px, focus outlines at 6px, and the round portrait frame and social circles at 50%.

Frames tilt by a hair (-1.5° default, +1.2° for the right-hand variant) and the plan flag rotates 3°; that tilt is the hand-hung signature and should stay within ±3°. Illustrations are flat paper-cut PNGs with keyed alpha, no outline, no shadow.

## Components

### Buttons
Friendly pills with a 2px ink border in every variant; the fill changes, the edge does not.
- **Shape:** full pill (999px), 2px solid ink border, Nunito 800, inline-flex with a 0.55rem gap for the optional inline SVG icon (1.15em).
- **Primary (`.btn`):** ink fill, white text, 0.95rem 1.5rem. The default action ("Message me on WhatsApp", "How the system works").
- **Sun (`.btn--sun`):** sunflower fill, ink text; hover to honey. The nav CTA and video-series starts.
- **Clay (`.btn--clay`):** clay fill, ink text; hover to honey. One per page, for the purchase that matters most.
- **Ghost (`.btn--ghost`):** transparent, ink text; hover inverts to ink/white. The secondary action beside a primary.
- **White (`.btn--white`):** white fill; hover to butter. The secondary action on a yellow field.
- **Sizes:** `.btn--sm` (label size, 0.7rem 1.1rem) for the nav; `.btn--lg` (lede size, 1.1rem 1.9rem) for CTA bands.
- **Hover / Focus:** translateY(-2px) with the lift shadow over 0.35s exponential ease-out; active returns to 0. Focus-visible is a 3px clay outline offset 3px.

### Chips
- **Style:** white pill, 2px ink border, Nunito 800 at 0.9rem, 0.4rem 0.85rem. Used for blog category filters and series navigation.
- **State:** hover butter; selected (`aria-pressed="true"` / `aria-current`) sunflower. Series nav marks the current item with a sun `span`.

### Tags
- **Style:** butter pill, 2px ink border, Shantell Sans at the smallest step, 0.2rem 0.75rem. Short hand-written labels ("Self-study", "1:1").

### Poster Frame (signature)
Every photo and illustration hangs in one.
- **Style:** white mat (12px padding) inside a 2px ink border, poster shadow, image `object-fit: cover`. Hero portrait is 4/5, max 460px.
- **Variants:** `.frame--tilt` (-1.5°), `.frame--tilt-r` (+1.2°), `.frame--round` (circular, 8px mat, for the podcast portrait), `.frame--cut` (a sun mat with no padding for a keyed-alpha cutout of Jennifer).
- **Caption:** Shantell Sans, soft ink, centered, 0.6rem above.

### Section Fields
- **Style:** `.section` with a fill modifier: `--white`, `--butter`, `--sun`, `--sage`, `--ink` (paper text, sun links). `--line-top` / `--line-bottom` add the 2px ink rule. Ledes and paragraphs switch to full ink on yellow fields.
- **Titles:** `.section__title` caps at 22ch; `.center` centers the title and lede.

### Pillars
- **Style:** one 2px-bordered white bar split into three columns by 2px ink rules; the first pillar is filled sunflower. Big Shantell Sans numeral in deep sunflower, `--step-1` heading, soft-ink body.

### Quotes with Provenance Tags (signature)
- **Style:** white rectangle, 2px ink border, 1.5rem padding; a large sunflower opening quote mark in Shantell Sans hangs at the top-left; text indented 1.6rem.
- **Tag:** every quote ends in a stitched provenance tag: butter pill with a 2px dashed ink border, a clay dot, Shantell Sans, reading "Name · Country[, living in the US]". No quote ships without one.
- **Variant:** `.quote--sun` fills sunflower with a white quote mark; at most one per quote grid.

### Pricing Plan Cards
- **Style:** white column card, 2px ink border, three stacked bands separated by 2px ink rules: head (title + soft-ink kind), price (Shantell Sans `--step-3` figure with soft-ink cadence line), feature list with inline SVG check marks (excluded features in mute ink), then a full-width pill button.
- **Featured (`.plan--hot`):** butter fill with a 3px sunflower outline offset 4px, a rotated (3°) sunflower "most popular" pill flag on the top edge, and the page's one clay button.

### Episode Cards
- **Style:** white rectangle, 2px ink border, 1.1rem 1.25rem padding; `--step-1` title, soft-ink meta ("Feb 21, 2024 · 30 min"), a native `<audio controls preload="none">` with pill radius, then a `details` "About this episode" whose summary is deep-clay Nunito 800 with a "+ / –" text marker.
- **Archive:** older episodes sit inside a `details.archive` whose summary is a ghost button that disappears once opened.
- **Stats:** `.stat` white boxes with a deep-clay Shantell Sans `--step-4` number over a soft-ink 800 caption.

### Post Cards
- **Style:** white rectangle, 2px ink border, 16/10 thumbnail on butter (empty thumbnails show the logo at 40%), meta in 0.85rem 800 soft ink, 1.2rem title, 0.95rem soft-ink excerpt. Hover lifts 4px with the poster shadow. Year groups open with a `--step-2` heading and a 20%-ink rule.

### Inputs / Fields
- **Style:** paper fill, 2px ink border, 12px radius, 0.8rem 0.95rem, inherited font, clay caret, mute-ink placeholder; Nunito 800 0.95rem label above.
- **Focus:** 3px sunflower outline offset 2px (the one place focus is sun rather than clay).

### Navigation
- **Header:** sticky, paper fill, 2px ink bottom rule, 74px min height; bold logo mark (46px tall) left, links right.
- **Links:** Nunito 800 0.98rem pills; hover butter, current page sunflower; the WhatsApp CTA is a small sun button.
- **Mobile (≤960px):** a pill outline "Menu" toggle opens a full-width paper dropdown under the header, 2px ink bottom rule, stacked links, CTA centered.
- **Ribbon:** ink bar above the hero, label size 700, sun links (honey on hover); its trailing clause hides under 640px.
- **Footer:** sunflower field with a 2px ink top rule; charcoal logo mark, four columns, white 42px social circles that lift 3px and turn honey on hover; a 2px ink rule above the legal line.

### Motion
One reveal grammar plus two hero moments; nothing else moves.
- **Reveal:** `.reveal` elements start at opacity 0 / translateY(18px) and settle on entry (IntersectionObserver, threshold 0.08, −8% bottom margin) over 0.7s opacity / 0.9s transform with `cubic-bezier(.16, 1, .3, 1)`. Elements already in the viewport at 300ms are shown; no-JS shows everything.
- **Hero spring:** the three words spring out of the open box with `springOut` 1.1s, staggered 0.5s / 0.75s / 1s, landing at ±8–9° tilt in white 8px-radius ink-bordered labels.
- **Sun spin:** the hero sun badge rotates 360° every 60s, linear.
- **Hover:** 0.2–0.35s; lifts use the same exponential ease-out.
- **Reduced motion:** `prefers-reduced-motion: reduce` disables smooth scroll, the reveal, the spin, and the spring (words render in their final position). Every future animation must carry the same guard.

## Do's and Don'ts

### Do:
- **Do** put every photo and illustration inside a poster frame (2px ink, 12px white mat) and tilt it -1.5° or +1.2°.
- **Do** edge every panel and every field change with the same 2px ink line; fade rules to 20% ink when they must be quiet.
- **Do** keep buttons, nav links, chips, and tags as full pills, and keep containers sharp-cornered.
- **Do** end every student quote with a provenance tag ("Name · Country") in the dashed butter pill.
- **Do** use one clay button per page, on the purchase or message that matters most.
- **Do** use inline SVG (`fill="currentColor"`, 24-unit viewBox) for every icon, sized in em inside buttons and lists.
- **Do** use `.reveal` for scroll entry and nothing else; guard any new animation with `prefers-reduced-motion`.
- **Do** keep Jennifer's copy verbatim, including her Portuguese asides and her emoji inside her own sentences.
- **Do** use only her photos and the paper-cut illustration set recorded in `assets/img/PROVENANCE.md`; every new raster carries its provenance.

### Don't:
- **Don't** use gradients anywhere: not in fields, buttons, overlays, or illustrations.
- **Don't** use emoji, icon fonts, or glyph characters as UI icons; the only emoji on the site are inside Jennifer's own sentences.
- **Don't** add drop shadows to resting surfaces, hard offset shadows, glows, or inner shadows.
- **Don't** introduce a second stroke color, a grey divider, or a border thinner or thicker than 2px (tables inside legacy prose at 1px are the tolerated exception).
- **Don't** set uppercase tracked labels, kickers, or eyebrows above headings.
- **Don't** set body text in Shantell Sans or headings in Nunito.
- **Don't** apply yellow as a stripe, strip, or highlight bar; yellow owns whole sections, columns, or a single word via `.mark`.
- **Don't** add per-section animation novelty; the reveal, the hero spring, and the sun spin are the whole vocabulary.
- **Don't** add a dark "premium" theme or icon-card grids; the ink section exists for contrast bands only.
