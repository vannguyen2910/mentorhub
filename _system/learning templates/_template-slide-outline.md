---
title: ""
lesson_file: ""             # e.g. customer-understanding-lesson.md — the paired source-of-truth file
level: ""                   # Junior | Senior/Lead | (blank if the track has no split)
slide_count: 0
duration: "90 min"
status: draft                # draft | ready-to-build | matches-built-deck
built_deck: ""               # filename of the .html/.dc.html deck once one exists, else leave blank
last_synced: 2026-00-00      # date lesson.md and this file were last confirmed in sync
---

> **Source of truth:** `[lesson_file]`
> All content changes (activities, phases, timing, concepts) are made there first, then reflected here.
> This file contains only slide-specific concerns: layout types, on-slide text, visual hints, kickers, and speaker notes.
> See `CLAUDE.md` → Lesson file sync rule for what triggers an update on which side.

> **Layout vocabulary is fixed.** Every `###` slide header below must use one of the 15 types
> documented in `_system/rules/slide-deck-rules.md` (Cover, Section divider, Statement, Numbered,
> Compare, Process, Quote, Milestone, Practice, End, Diagram, Formula, Image, plus the two
> remaining reserved slots). If a slide genuinely needs something none of these cover, add the
> type to `RULES.md` first — do not invent a one-off name here. `SECTION`, `COMPARISON`, and
> `ACTIVITY` are drift, not valid types — use `SECTION DIVIDER`, `COMPARE`, `MILESTONE`.

---

## Session metadata

| Field | Value |
|---|---|
| Program | <!-- ux-class \| private-training --> |
| Track / session | <!-- e.g. Track 3, Session 3 --> |
| Stage | <!-- Discover \| Define \| Develop \| Deliver \| Foundation --> |
| Prior session | <!-- what this hands off from --> |
| Next session | <!-- what this hands off to --> |
| Running example | <!-- e.g. food delivery — see framework files before introducing a new case --> |

---

## Slide structure — [N] slides

<!-- One line per block, mirroring the lesson.md Run-of-Show in the same order.
     Class lessons are theory first, then practice (mentoring-rules.md, Rule LP-3):
     Open → Theory (3–4 parts) → Bridge → Practice → Close. -->

- Arc: **Open** → **Theory** → **Bridge** → **Practice** → **Close**.
- Section dividers mark the big shifts only: **Theory** and **Practice** (and the Close if it changes topic). Parts inside Theory are marked by the kicker, not a divider.
- Bridge = one `MILESTONE` slide (`Num:` = 5, break and check) and one `DIAGRAM` **Cheat sheet** slide that stays on screen during Practice.
- Practice slides: `MILESTONE` for each activity (`Num:` = minutes) and `PROCESS` or `PRACTICE` for the task card.
- Timing on screen lives only on `MILESTONE` slides. Theory ≤ 40 minutes in total.

---

## Standard slide entry

<!-- Every slide below follows this field set. Do not drop fields; write "None." rather than omitting one. -->

```
### [LAYOUT TYPE] · [Slide title / short label]
- Kicker: [eyebrow line above the title — this slide's own topic only; no "Part 01 ·" prefix, the part number lives on the SECTION DIVIDER]
- Title: [on-slide title — line breaks written as \n]
- On-slide: [the actual visible text/labels — short, not prose. "None." if the layout has no body copy field]
- Giờ: [minutes for this slide]
- Ví dụ: [có (tên ví dụ) | bản nháp (tên ví dụ) | cần ví dụ: loại ví dụ cần | Không cần. + lý do]
- Câu hỏi hay gặp:
  - [câu hỏi? Trả lời ngắn.  — or "None."]
- Speaker notes:

  > [câu nói nguyên văn: mở bằng ví dụ hoặc tình huống, rồi mới đến khái niệm]

  - [ý cần giải thích, một ý một dòng, nói bằng lời của mình]

  > **[câu không được bỏ]**

  > [câu hỏi cho lớp, hoặc câu nối sang slide kế tiếp]
- 🎨 Visual hint: [SCHEMATIC / REAL / TYPOGRAPHIC, then the description]
```

Speaker notes follow `_system/rules/slide-deck-rules.md` → Speaker notes rule: `>` lines are exact words (3–6 per slide: example opener, the must-not-miss line, the class question, the transition); bullets are the ideas between them (4–8 per slide). No prose paragraphs and no bracketed stage directions. Give the example first, the concept after. Run `/notes-audit` before building the deck.

---

## Slides

<!-- COVER is locked. Copy this block as-is and change ONLY Stage, Title, Subtitle and Right panel photo.
     See CLAUDE.md → Cover slide rule. No badge, tag, session number, level or duration. -->

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: [Foundation | Discover | Define | Develop | Deliver | Leader Level]   <!-- from the lesson folder, no number -->
- Title: [Line one]\n*[Accent line]*
- Subtitle: [One sentence, 12 words or fewer, no em dash]
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer at NAB
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: [one line: real photo, subject and mood]
- Speaker notes:
  - [3–6 bullets]
- 🎨 Visual hint: Cover layout, fixed. White left panel with year line, stage label, title (accent on line 2) and subtitle. Right panel is the real photo with dark gradient overlay, name and three credential lines bottom-left.

---

<!-- Slide entries go here, in the standard field format above, one section-divider per lesson phase. -->
