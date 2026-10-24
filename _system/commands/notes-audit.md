---
description: Audit the speaker notes of a slide outline: which slides need a real example, are too thin or too long for their time, or break the notes format. Report only
argument-hint: <path to *-slide-outline.md, or lesson folder>
---

Audit speaker notes: $ARGUMENTS

This command reads and reports. It does not edit the outline, the lesson or the deck. Read `_system/rules/slide-deck-rules.md` → Speaker notes rule and `_system/rules/vi-voice.md` before judging any Vietnamese.

## 1. Run the mechanical check

```
python3 _system/scripts/notes-audit.py <outline.md>
```

It reports, per slide: verbatim (`>`) lines, bullets, spoken words, estimated spoken minutes, missing `Ví dụ` fields, bracketed stage directions, and slides with no verbatim line. It also flags Title and Kicker copy that breaks `_system/rules/slide-deck-rules.md` → Title and kicker copy (Title over 6 words, Kicker with a Phần/Buổi number, Kicker repeating Title).

## 2. Judge what the script cannot

Read the outline and its paired `*-lesson.md`. For every concept slide (`NUMBERED`, `COMPARE`, `FORMULA`, `STATEMENT`, `DIAGRAM`, `PROCESS`, `QUOTE`):

1. **Needs an example?** Yes when the notes explain an idea with no concrete situation, number, artifact or outcome. No when the slide only names, sequences or transitions.
2. **Does the lesson already hold one?** Search the lesson file first. If it does, point to it. The lesson is the source of truth, so an example belongs there before the outline.
3. **Is the example first?** The situation comes before the concept name (concreteness fading).
4. **Is the transfer explicit?** The notes end with a question or line tying the example to the mentee's own project.
5. **Is one example enough?** A concept used in several contexts needs a second, different example, so learners do not memorise the case.

## 3. Report

One table, then a short list. Vietnamese, headings in English.

| Slide | Layout | Vấn đề | Đề xuất |
|---|---|---|---|

- **Cần ví dụ:** each slide with the kind of example needed (one line, no invented case).
- **Format:** slides with missing fields, stage directions, or over length.
- **Timing:** total estimated minutes against the lesson's session table.
- **Sync:** anything that would also need a change in `*-lesson.md`.

## Rules

- Never fill in an example as if it were real. If you suggest one, label it `bản nháp`.
- No mentee, company or cohort names in suggestions.
- No specific AI tool names; use "AI chat tool", "AI coding tool".
- Do not rewrite notes. Offer to, and wait.
