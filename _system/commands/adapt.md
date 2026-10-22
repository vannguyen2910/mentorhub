---
description: Turn WF-2 candidates from a private session into de-identified class ideas, a placement proposal and short briefs. Edits no lesson, outline or deck
argument-hint: <mentee> [session number | candidate text]
---

Adapt private-session ideas for class use: $ARGUMENTS

This command is the step between `/log-session` or `/closeout` (which only list WF-2 candidates) and `/build-lesson` (which builds). It reads, de-identifies, proposes where each idea belongs, and drafts briefs. It never edits `*-lesson.md`, `*-slide-outline.md` or a deck, never creates a lesson folder, never runs the site build, and never sends anything. Today's date comes from the system.

**Vietnamese:** write the output in Vietnamese per `_system/rules/vi-voice.md`: body in Vietnamese, headings and professional terms in English, file names and front matter keys in English. Follow with `vietnamese-copy-polish` as a check only (diacritics, sentence length, filler, dashes).

## 1. Find the candidates

Work out the mentee slug and session. Read, in this order, and stop at the first source that lists candidates:

1. the "WF-2 candidates" section of the latest recap in `mentees/<slug>/sessions/` (or the named session)
2. the "Reusable material (WF-2)" section of a close-out recap
3. the candidate text the user pasted

If none exist, say so in one line and stop. Do not mine the transcript for ideas unasked; offer it instead.

Before going on, check each candidate against `_inbox/wf2-briefs-*.md` and the lesson update notes (for example "Cập nhật ... (WF-2)" at the top of a `*-brief.md`). A candidate already briefed or already applied is reported as such and gets no new brief. Never write a duplicate brief set.

## 2. De-identify (WF-2 checklist)

For each candidate, check and apply:

- remove every name, company, cohort and project detail that could identify the person
- reframe the example so it fits any student, and widen the problem statement
- keep specific tool names out: use "AI chat tool", "AI coding tool", "your AI tool"
- never quote feedback that was personal or situation-specific
- record `source: adapted-from-private-session` in the front matter of the output

If a candidate cannot be generalised without losing its point, mark it `[keep private]` and say why.

## 3. Propose where each idea goes

Read the lesson tree under `library/lessons/` and `library/guides/`. For each idea choose one placement and one alternative:

| Type | When |
|---|---|
| Small update to an existing lesson | The lesson already covers the topic and only a delta is missing |
| New block in a lesson not yet started | The idea only makes sense at a later stage. Do not create the folder; programme READMEs say it is created when the lesson starts |
| New guide | The idea stands alone and several lessons would reference it |
| Not worth adding | Already covered, or too narrow |

Give the exact target path, and name the existing lesson's approved/built state if it has one. Check the idea is not already in the target file.

## 4. Draft the briefs

For each idea marked as update, block or guide, write a short brief in the WF-5 format (title, type, audience, level, duration, Purpose, Structure, Key decisions). For an update to an existing lesson, list only the delta and say which part of the lesson's timing it fits in (use the existing buffer; never change phase timing silently). Mention which paired file (`*-lesson.md` or `*-slide-outline.md`) will need the matching change.

## 5. Write the output

- One file: `_inbox/wf2-briefs-<mentee-slug-or-source>-YYYY-MM-DD.md`, front matter `type: brief-set`, `source: adapted-from-private-session`, `status: brief, chờ Winnie duyệt`. Use the existing file in `_inbox/` as the shape reference.
- Do not use the mentee's name in the file name or body. Use the slug only in the file name if the user wants traceability.
- Do not create any other file.

## 6. Report

A short table: idea, placement, type of change, alternative. Then what waits on the user: approve, edit or drop each brief, then run `/build-lesson` for the approved ones. If nothing qualified, say so in one line.
