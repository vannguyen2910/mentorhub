---
name: learning-loop
description: Compass for preparing and reviewing Winnie's teaching and mentoring. Checks that every theory session, practice session, coaching and mentoring moment, and every mentee's plan covers the full learning loop (knowledge, experience, skill, training, performance, coaching, mentoring, feedback, logging, reflection), and flags what is missing, especially logging and reflection. Use when preparing or designing a lesson, practice, session, coaching plan or programme, or when Winnie says "learning loop", "vòng lặp học", "kim chỉ nam", "chuẩn bị theory", "chuẩn bị practice", "coaching hay mentoring", "learning log", "reflection", "feedback có được ghi lại chưa". Report only, edits nothing.
metadata:
  version: "0.1"
---

# Learning Loop

A compass, not a generator. It does not write lessons. It asks, before and after teaching, whether the whole loop is covered, and says in a few lines where it is not.

Source and definitions: `references/components.md`. The source is one personal blog post (2021), so treat it as a thinking frame, never as evidence, and never cite it to a mentee as research.

## The loop

Knowing (knowledge, experience, skill) → Doing (training, performance) → Assessing (coaching, mentoring, feedback, logging, reflection) → back to Knowing. The loop is only as strong as its weakest part. In this workflow the weak parts are **logging** and **reflection**: feedback is given in sessions but rarely recorded, and rarely turned into something the mentee changes.

## Four kinds of session, one question each

Every session Winnie prepares is mainly one of these. Name which one before preparing.

| Kind | Loop part | The question to answer before the session |
|---|---|---|
| **Theory** | Knowledge | What single concept does the learner leave able to explain in their own words, and which later activity uses it? |
| **Practice / training** | Experience, skill, training | Which real work (their own case or task) do they do, and what file or output proves they did it? |
| **Coaching** | Feedback on performance | What will Winnie watch them do, so that she can give feedback they could not see themselves? |
| **Mentoring** | Knowledge fitted to their situation | What decision or doubt of theirs will the advice be about, so it is not generic? |

Two further checks apply to all four:

- **Performance:** is there a moment where the learner does the real thing for real (a peer test, a presentation, a delivered file), not only exercises?
- **Assessing:** where is the feedback written down (logging), and when does the learner turn it into one thing they will change (reflection)?

## How to run it

1. Identify the target: a lesson, a practice sheet, one session of a mentee (`/prep` output), a coaching plan, or a whole programme. Read it. Do not guess from the title.
2. Map what is there to the ten components (see `references/components.md`). One line per part, quoting where it appears (file and section).
3. Report, in Vietnamese, a **Loop check** of at most 8 lines:
   - Covered: parts that are present, in one line.
   - Missing or weak: each gap with the file or section where it should live.
   - One suggested fix per gap, as small as possible (a 3-line log, a 3-minute reflection question, a rename of a role). Respect the time limits in `mentoring-rules.md` (Rule LP-3): do not add activity inside a Theory block of 40 minutes or less.
4. Stop. Make no edits. If Winnie accepts a fix, apply it with the normal rules in `CLAUDE.md` (lesson and outline in sync, consistency check, site rebuild).

## Standard pieces to suggest

Keep these small. Do not invent heavier ones.

| Gap | Standard piece |
|---|---|
| No logging | A **learning log** after each session: three lines (what I did, feedback I got, what I will change). About 5 minutes. For a mentee it sits beside `sessions.md`; for a class, in the case folder |
| No reflection | One fixed question, 3 minutes, at the end of a practice or mentoring session: which feedback today changed how you think? The answer goes into the log |
| Roles unclear | Say once, early: theory is mentoring (knowledge), practice is coaching (performance), peer review is feedback. Learners then know what to ask in each session |
| No performance moment | One real delivery per cycle (a short share-out, a peer test, a file handed over), reviewed against the same criteria as the practice |
| Loop never closes | At the end of a programme, read the whole log for repeating patterns (the kind of feedback that returns, the step that keeps failing) |

## Where it plugs into the existing workflow

`business/mentoring-workflow.md` is the map. This skill adds a check at these existing steps. It does not change those commands until Winnie says so:

| Step | Command | Loop check adds |
|---|---|---|
| Prep | `/prep` | Which kind of session this is, and its one question |
| Build lesson | `/build-lesson` | Theory and practice are paired; every concept is used by an activity |
| Log | `/log-session` | A draft learning-log entry and one reflection question for the mentee |
| Close-out | `/closeout` | Read the log for patterns, next to baseline vs reassessment |

## Rules

- Report only. No file is edited, nothing is sent.
- Vietnamese output follows `_system/rules/vi-voice.md`: English headings and terms of the trade, Vietnamese body, no spoken filler.
- Lessons and outlines never name a mentee (see `CLAUDE.md`). Use "học viên" or "mentee".
- Use generic tool labels ("AI chat tool", "AI coding tool"), never product names.
- Do not teach all ten components in one session. Name the three groups; introduce the log and the reflection question as habits, not theory.
- Winnie decides what changes. When unsure, report the gap and ask.
