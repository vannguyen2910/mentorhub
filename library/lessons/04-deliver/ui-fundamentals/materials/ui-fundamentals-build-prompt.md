---
title: "UI Fundamentals: Slide Deck Build Prompt"
type: reference
program: standalone
date: 2026-09-09
---

# Build Prompt

Paste the block below into Claude Design with the two source files attached or in the project folder.

**Attach or point at:**
- `ui-fundamentals-slide-outline.md` (the slide specs, source of truth for the deck)
- `_system/rules/slide-deck-rules.md` and `Themes/slide-design/tokens.css` (the visual system)
- `assets/style-reference-schematic.png` (the schematic drawing style)

---

```
Build a 44-slide teaching deck from the attached slide outline.

CONTEXT
This is a 90-minute lesson for junior product designers about judging UI decisions
they did not make. The deck's job is to make students SEE things, not read about
them. A slide that states a principle without showing it has failed.

SOURCES, in priority order
1. ui-fundamentals-slide-outline.md is the source of truth for every slide:
   its type, kicker, title, on-slide content, and its "Visual hint" line.
   Build exactly the slides it lists, in order. Do not add, merge or reorder.
2. _system/rules/slide-deck-rules.md and tokens.css define the visual system.
   Follow them exactly. Never invent a colour, font or layout class.
3. style-reference-schematic.png shows the drawing style for schematic diagrams.

BUILD IN THREE PHASES. STOP AFTER EACH AND SHOW ME.

PHASE 1 - Design system file
Set up the token vocabulary from tokens.css, then build the schematic component
kit defined in the outline's "Visual language" section as reusable components:
  - text line (body): short horizontal stroke, --ink-ghost, 2px, round caps, variable length
  - heading line: 4px stroke, --ink-muted, shorter length
  - primary button: the one filled element, --ink fill, rounded rect
  - secondary button: outlined rounded rect, 2px --ink-muted
  - input field: outlined rounded rect, taller than a button, empty
  - radio / checkbox: circle outline, small --ink dot when selected
  - image or map block: outlined rect, no fill, no icon inside
  - specimen frame: 2px --ink hairline, --radius-lg corners (same as DS cards), generous padding
  - annotation set: --sienna arrows, measurement brackets, mono labels (at least 18px)
LINE-ART RULE (Design System): schematic specimens use 2px strokes, no fill, no
gradient. The only fill is --ink for emphasis, and the only colour is the single
--sienna accent for annotation. Colour is allowed elsewhere only in REAL screens and
on the role chips of the "Roles, not palettes" slide.
Also build the five-plane "Decision Stack" diagram as a component, since it
appears on slide 7 and returns as a small locator on all five layer dividers.
Show me the kit before building anything else.

PHASE 2 - Slide templates
Build one template per slide type using the layout classes in RULES.md:
  COVER            -> .cover
  SECTION DIVIDER  -> .section-main (Design System Section Main: yellow full-bleed, corner number, centred title; the five-plane locator sits top right)
  STATEMENT        -> .statement
  COMPARE          -> .compare (two matched specimen frames, equal size)
  DIAGRAM          -> .statement header + full-width specimen canvas below
  IMAGE            -> full-bleed specimen, minimal chrome, no kicker bar
  TWO-COLUMN       -> supplementary two-column split, 1fr 1fr, 80px gap
  MILESTONE        -> .milestone (--sienna background)
  PRACTICE         -> .practice
  END              -> .end (--paper-deeper background, never dark or sienna)
Show me the templates before building pages.

PHASE 3 - The 44 pages
Build every slide from the outline. For each one, read its Visual hint line and
build what it describes.

TWO VISUAL REGISTERS. THIS IS THE MOST IMPORTANT RULE.
The outline marks each visual hint as SCHEMATIC or REAL.

SCHEMATIC: build it fully, using the component kit. Abstracted UI, grey bars for
text, geometric shapes for controls, no real words inside a specimen, no
photography. This is most of the deck and it should look like the style
reference.

REAL: DO NOT ATTEMPT THESE. They need actual rendered product screens that I will
supply. For every REAL slide, build a correctly sized placeholder frame with a
mono caption stating exactly what goes there, taken from the Visual hint line.
Example: "PLACEHOLDER - tracking screen, spacing corrected, --sienna brackets on
the changed gaps." Get the frame size, position and slide composition right so
I can drop the screens in without relayout.

SPECIMEN RULES, apply to every slide
1. Anything inside a hairline frame is a UI being examined. Anything outside it
   is the deck talking. Never let slide chrome bleed into a specimen.
2. One accent per slide. --sienna annotates the single element under discussion and
   nothing else. Emphasis inside a specimen is an --ink fill. If two things are purple, the slide is making two arguments.
3. NO red X, NO green tick, NO "good" and "bad" labels, ever. Mark what is under
   discussion and let the student judge. The slide must never grade the screen.
4. COMPARE slides change exactly ONE variable. Same content, same layout, same
   everything, one decision different. If the two sides differ in more than one
   way, rebuild them.
5. Label comparisons neutrally in --font-mono: "24px" and "18px", never "wrong"
   and "right".
6. Measurement is drawn, not described. If a slide claims a gap is 24, the 24 is
   on the slide with a --sienna bracket.

SPEAKER NOTES
Copy the bullets from each slide's "Speaker notes" into that slide's notes field,
verbatim, as bullets. Do not convert them to prose. Do not summarise them.

HARD RULES from RULES.md
- Use token names, never hex values. --sienna, --ink, --paper, --ochre.
- Never use --purple or --yellow directly, use the --sienna and --ochre aliases.
- Fonts: --font-display (Syne) for headings, --font-body (Inter) for body,
  --font-mono (JetBrains Mono) for kickers, numbers and measurement labels.
- Section dividers use the Design System Section Main layout (yellow full-bleed), never a dark ink background.
- The end slide uses --paper-deeper, never dark or sienna.
- No visible slide numbers or session tags.
- 1920x1080 per slide.
- No em dashes in any copy. Use commas, colons or a full stop.

DO NOT
- Do not rewrite any title, kicker or on-slide copy from the outline. Line breaks
  marked \n in the outline are intentional. Italic markers are intentional and
  should render as --sienna emphasis.
- Do not add slides that are not in the outline.
- Do not fill the empty slide. Slide 5, "Producing is no longer the thing you're
  paid for", is deliberately blank apart from its title. Leave it blank.
- Do not attempt the REAL screens. Placeholders only.

Start with Phase 1.
```

---

## Notes for Winnie

**Why it stops between phases.** The schematic kit is what makes 30 diagrams consistent instead of 30 slightly different drawings. If the tool starts making slides before the kit exists, every specimen drifts and the deck stops reading as one system.

**Why REAL slides are placeholders.** Several slides need genuinely attractive, fully rendered product screens: the tracking screen in its eight versions, and the reveal. A generative tool cannot make those convincing enough to carry the Aesthetic-Usability argument, and an unconvincing one breaks the whole reveal. Build those in Figma and drop them into the frames.

**The assets you still owe the deck:**
1. Stimulus set, 6 to 8 screens of one product, mixed AI and real, genuinely hard to choose between
2. Two real text samples for the contrast slide, deliberately similar, one passing and one failing
3. Cover photo (a real photograph)
4. @2x exports of five tracking screens (original, type, blur and desaturate-collapses already have them)

Done (2026-11-18): the tracking screen in nine versions, in `assets/tracking-screen/` (see `assets/SOURCES.md`).

**Build with the teaching-slide-deck skill and the Design System.** Start from `templates/slide-deck/SlideDeck.dc.html`, do not add layouts, fonts or text sizes, declare the deck language, and run the three Vietnamese editing steps (translationese, style guide, grammar) on any Vietnamese text before delivery.
