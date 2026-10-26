# Mentoring Program — Claude Rules

## Commands

Run all of these from the repo root.

| Command | Use |
|---|---|
| `python3 _system/scripts/build-home.py` | Rebuild the website in `docs/`. Add `--watch` to rebuild on every change |
| `python3 _system/scripts/notes-audit.py <outline.md>` | Audit speaker notes of a slide outline (report only) |
| `python3 _system/scripts/sync-deck.py <lesson folder> [--write]` | Sync an outline from its built deck. Dry run unless `--write` |
| `python3 _system/scripts/mentee.py new\|log\|check\|migrate` | Set up mentees and log sessions without hand-editing the site |
| `_system/scripts/new-lesson.sh lesson\|framework\|guide\|slides <name>` | Scaffold a new lesson, framework, guide or slides folder |

To view the site locally, use the `docs` entry in `.claude/launch.json` (port 3002). `.claude/commands` is a symlink to `_system/commands`, so edit slash commands there.

## Repo boundaries

- `docs/` is generated. Never edit it by hand: `build-home.py` rewrites it.
- Private by `.gitignore`, so never expect these on the site or in git: `source/`, `mentees/`, `business/`, `showcase/private/`, `showcase/testimonials.md`, `programs/assessment-tool/`.
- Lessons shared across programs live in `library/lessons/`. Lessons that belong to one program live in `programs/<program>/lessons/<NN-slug>/` (`materials/`, `slides/`, `assets/`, `_archive/`); `build-home.py` scans both.

## AI Design Workflow (`programs/ai-design-workflow/`)

- `learning/plan.md` is the source of truth for the programme structure (weeks, which sessions are theory or practice, key decisions, open questions). Change it before changing a lesson that depends on it. There are no Check points: weeks 1 to 5 pair a theory lesson with a practice session, and week 6 ends with a one-day practice and a reflection and wrap-up session.
- `learning/` is private working material (research, method, lesson details). Only pages listed in `SUMMARY.md` reach the site.
- Lesson files say "buổi N" meaning lesson N, not the session number in the 12-session sequence. Keep that in mind when linking lessons to the plan until the labels are renamed.
- Before restructuring a lesson, copy the old lesson and outline to `materials/_archive/` with a `-pre-<reason>-YYYY-MM-DD` suffix.
- Each lesson folder has three files in `materials/`: `*-lesson.md`, `*-practice.md` (student-facing worksheet for the practice session, from `_system/learning templates/_template-practice.md`) and `*-slide-outline.md`. The hub shows lesson and practice only: list them in the `## Lessons` group of `programs/ai-design-workflow/SUMMARY.md` and never list an outline. When a lesson's activities or output file names change, check its practice sheet too. The wrap-up session has its own folder, `07-wrap-up`, with a practice file only.

## Lesson file sync rule

Every lesson in `library/lessons/` (and in `programs/<program>/lessons/`, for example AI Design Workflow) has two paired files:
- `*-lesson.md` — the source of truth for all content (activities, phases, timing, concepts)
- `*-slide-outline.md` — reflects the lesson structure as slide specs (layout types, visual hints, kickers)

**When either file is updated, always check and update the other.**

New `*-slide-outline.md` files start from `_system/learning templates/_template-slide-outline.md`, not a blank page — it fixes the session metadata table, the standard slide-entry fields, and the speaker-notes rule (verbatim `>` lines plus bullets, with `Ví dụ` and `Câu hỏi hay gặp` fields). Layout types come from the catalogue in `_system/rules/slide-deck-rules.md` (canonical — other paths to a rules file are pointers to it).

**Before editing any `*-slide-outline.md`, read `_system/rules/slide-deck-rules.md` → Speaker notes rule; after editing, run `python3 _system/scripts/notes-audit.py <outline.md>` and report the result in the same response.** This applies to existing outlines too, not only new ones.

Specifically:

| What changed in lesson.md | What to update in slide-outline.md |
|---|---|
| Phase timing (e.g. "15 min" → "20 min") | MILESTONE slide `Num:` value + arc description + slide structure note |
| Phase added or removed | Add/remove the corresponding slide section; update total slide count in the structure note |
| New checkpoint or transition inserted | Add a STATEMENT or MILESTONE slide at the matching position in the outline |
| Section reordered (e.g. concept extension moved) | Reorder the corresponding slides in the outline |
| Slide count changes for any reason | Update the `## Slide structure` header line (e.g. "17 slides" → "18 slides") |

| What changed in slide-outline.md | What to update in lesson.md |
|---|---|
| Slide timing or Num value changed | Update the matching phase timing in the Session Structure table |
| Slide added or removed | Check if the lesson phase needs a matching structural change |
| Kicker or title copy changed | Check if the lesson phase heading or key message should match |

**Always apply both files in the same response.** Never leave one out of sync with the other.

---

## Site rebuild rule

The website (`docs/`) is generated, not live. Lesson pages, slide-deck links and copied assets only update when `_system/scripts/build-home.py` runs. It already covers every lesson, framework, guide, mentee and program, so this rule applies everywhere.

**After adding, moving, renaming or editing anything under `library/` (lessons, frameworks, guides, slides, their `materials/`, `slides/` or `assets/` folders), `programs/*/lessons/` or `mentees/`, run `python3 _system/scripts/build-home.py` in the same response**, then tell the user it was rebuilt. Don't ask first.

- Decks must be `.html` files directly inside the item's `slides/` folder (not `_archive/`, not nested) to get a deck link.
- Images and files a deck uses belong in `slides/` or `assets/`; both are copied to `docs/assets/`.
- If the user edits files by hand outside Claude, they can run `python3 _system/scripts/build-home.py --watch` to rebuild automatically.

---

## Deck edit rule

The built deck (`slides/*.html`) is the version that gets taught, so it drifts from the lesson and outline whenever it is edited by hand after a session. Treat a deck edit like a lesson edit.

| When | Do this, in the same response |
|---|---|
| A deck in `library/lessons/**/slides/` is edited, or a session is taught from a deck that differs from its outline | Reverse-sync: update `*-slide-outline.md` first (slide list, order, MILESTONE `Num:` values, slide count), then `*-lesson.md` (Session Plan, timings, activity placement). For what was delivered, the deck wins. Mark anything in the lesson you would rather keep as `[to confirm]` |
| Reverse-sync changes the structure | Copy the old lesson and outline to `materials/_archive/` first, named with `-pre-<reason>-YYYY-MM-DD`, and add a short sync note at the top of the lesson |
| A lesson has more than one deck (for example EN and VI) | Every variant keeps the same slide order. Language may differ, structure may not. Fix the odd one out, not the outline |
| A deck is new or has been taught | It is committed to git. An untracked deck has no history to recover from |

To sync an outline from its deck, run `/sync-deck <lesson folder>` (script: `_system/scripts/sync-deck.py`; dry run by default). To audit speaker notes, run `/notes-audit`.

This rule sits beside the lesson file sync rule above. That rule keeps lesson and outline together. This one keeps both together with the deck.

---

## Testimonial capture rule

Whenever a prompt includes feedback from a student or mentee about Winnie's teaching/mentoring — praise, a reaction, a quote, however casually mentioned — automatically add it to the central quote bank at `showcase/testimonials.md`, in the same response, without being asked.

Specifically:

| What to do | How |
|---|---|
| Add the entry | Follow the format already defined at the top of `testimonials.md`: name, company/context, programme, date, quote, context line, permission line |
| Set permission status | Default to `Permission to publish externally: not yet confirmed` unless the user explicitly says the student agreed to publish |
| Sync the student's own record | If the student has an existing file (e.g. `mentees/[name]/README.md` or a session recap), also add the quote there so both stay in sync — same principle as the lesson sync rule above |
| Don't gate on being asked | Capture it proactively; just tell the user afterward that it was added, don't ask permission first |

If `showcase/testimonials.md` doesn't exist yet, create it using the same structure as the current file (header, permission note, entry-format block, then entries).

---

## Programme kickoff & close-out rule

Every private-training student should get two artifacts from `_system/learning templates/`: a coaching plan at kickoff (`_template-coaching-plan.md`) and a close-out recap on their final session (`_template-programme-closeout.md`). This makes every future close-out able to show real before/after growth instead of a single snapshot.

Specifically:

| When | Do this |
|---|---|
| Starting a new private-training student | Create their coaching plan from `_template-coaching-plan.md`. Its "Baseline Assessment" section is mandatory — run the self-assessment tool (`programs/assessment-tool/student-design-assessment.html`) with the student at or before Session 1 and save the result into their student folder. Without this, there's nothing to compare the close-out reassessment against. |
| Running the final session of a programme | Create the recap from `_template-programme-closeout.md`, not the plain `_template-session.md`. Pull the Session 1 baseline numbers into its "Baseline vs Reassessment" table — don't just report the final score in isolation. |
| A student has no baseline on file (older/in-flight programmes) | Flag this to Winnie explicitly rather than silently using only the final snapshot — the close-out template's comparison table will be incomplete without it. |
| Close-out is reached | Apply the testimonial capture rule above in the same response — close-out sessions are exactly where testimonials tend to surface. |

---

## Diagram rule

For any user flow, process map, journey, flowchart, swimlane, sequence or architecture diagram, use the `diagram-design` skill (`_system/skills/diagram-design/`). Do not hand-draw SVG or invent another style. Mermaid, draw.io and Excalidraw inputs go through `/import-mermaid`, `/import-drawio`, `/import-excalidraw`; PNG/SVG export goes through `/export-diagram`. Save the diagram next to the file it supports (a lesson's `assets/`, or the student's folder). Diagram labels follow the same language and generic-label rules as the surrounding file.

---

## General lesson conventions

- All specific AI tool names (Claude, Cursor, ChatGPT, Copilot, etc.) should be replaced with generic labels: "AI chat tool", "AI coding tool", "your AI tool". Do not introduce tool names when editing lesson content.
- Lesson and slide-outline content must never reference a specific mentee or student by name — every lesson is built to be taught to any mentee, not just the one it was drafted for. Do not introduce a mentee's name, cohort, or identifying detail when drafting or editing `*-lesson.md` or `*-slide-outline.md`; if an example needs a person, use a role label ("the mentee", "a junior designer") instead. This is separate from the private-session attribution rule in `workflow-rules.md`, which governs crediting a mentee when their session is the *source* of a class example — that rule is about consent to reuse, this one is about the lesson content itself staying generic regardless of where an idea came from.
- Slide `Title` is a short topic label (6 words or fewer, "Process Map là gì?"), and `Kicker` names the slide's role (Định nghĩa, Cách làm, Ví dụ) with no "Phần N" or "Buổi N" prefix. Full rule: `_system/rules/slide-deck-rules.md` → Title and kicker copy. `/notes-audit` flags breaches.
- The `*-slide-outline.md` file contains only slide-specific concerns (layout, visual hints, kickers). Do not add full lesson prose to it.
- The `*-lesson.md` file is the source of truth. If content in the two files conflicts, the lesson file wins.
- **Any Vietnamese content** (lessons, slide outlines, teleprompter scripts, method cards, session recaps, material sent to mentees or students): read `_system/rules/vi-voice.md` first. It sets the voice (natural, professional, no spoken filler such as "thì á", "cho nên là", "tại vì"), the English-titles/Vietnamese-body convention, the terms kept in English, and a list of translated-sounding phrases to avoid. Where it conflicts with `writing-style-guide.md` below, `vi-voice.md` wins. When Winnie corrects a Vietnamese line, add the before/after to `vi-voice.md` so the fix applies next time. Chat with Winnie in Vietnamese.
- For detailed voice/tone rules (tone, English code-switching, punctuation, teleprompter script format, Practice/Bài Tập script structure), see `programs/online-course/AI Prototype Development/writing-style-guide.md`. Read this before drafting or revising any `*-lesson.md`, `*-slide-outline.md`, or teleprompter script. It remains the source for that course's own structural formats; `_system/rules/vi-voice.md` takes precedence on tone, vocabulary and language conventions.
