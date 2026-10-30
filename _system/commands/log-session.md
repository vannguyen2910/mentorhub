---
description: Log a mentoring session end to end from a Zoom/Meet transcript (or Notion): cleaned transcript, sessions.md, public playback, private recap, homework draft, Notion playback page with examples from other learners, homework images, testimonial capture, site rebuild and preview
argument-hint: <mentee> <topic> [date] [transcript path, or paste the transcript after the command]
---

Log a session: $ARGUMENTS

Everything below is a draft until the user approves it. Nothing is sent to a mentee. The only thing this command writes outside the repo is the Notion playback page (step 6), and only after the playback is approved. No Zalo message is drafted (dropped 2026-10-26). Read `_system/rules/vi-voice.md` before writing any Vietnamese.

**Language and skills:** write private notes and everything the mentee reads in Vietnamese (decided 2026-10-11): body text in Vietnamese, section headings and professional terms in English, file names and front matter keys in English. Apply the Vietnamese skills in this order:

1. `vietnamese-voice-dictionary`: first, on the user's own words in `$ARGUMENTS` and chat when they look like speech-to-text errors. Ask once if a word is ambiguous. Do not run it on the mentee's words in the transcript (the cleaner handles those).
2. `vietnamese-transcript-cleaner`: on any Zoom/Meet transcript or caption file (step 3).
3. `vi-voice`: load before drafting the playback, the recap, and follow `_system/rules/vi-voice.md`.
4. `vietnamese-copy-polish`: last, on the playback (the text the mentee sees): diacritics, sentence length, filler, dashes, a clear next step. On private notes use it as a check only and do not restructure them.


## 1. Identify the session

Work out the mentee, the topic and the date (default today). Ask once if the mentee or topic is unclear. Find the session number from `mentees/<slug>/sessions.md`.

## 2. Get the source material (first match wins)

1. **Transcript file or pasted text** from Zoom or Meet (txt, vtt, srt, docx, or pasted into chat). Keep **one file per session** in `mentees/<slug>/transcripts/`, named `session-NN-YYYY-MM-DD.md` (private, never published). Save the cleaned version from step 3 there, not the raw `.vtt` or `.srt`, and do not leave a second copy. If the mentee's folder holds older names such as `Session N - Transcript - <Name>.md`, rename them to this pattern so all files match. Never overwrite or delete a file silently: if two files for the same session exist, say which one is wrong and ask first.
2. **Notion**: search the page "Coaching Program - <Full Name>" and open the matching session sub-page (notion-search, then notion-fetch).
3. **Neither exists**: ask the user for 3 to 5 bullets and work from those. Do not invent session content.

## 3. Clean and extract (private working notes, from the transcript)

Follow the `vietnamese-transcript-cleaner` conventions (run its `scripts/clean_subs.py` on `.vtt`/`.srt`, restore diacritics and punctuation, fix misheard terms from context, merge broken lines, label speakers from the source). Write the result to `transcripts/session-NN-YYYY-MM-DD.md` with front matter (`title`, `type: transcript`, `student`, `session_number`, `date`, `source`, `status`), a quality note, then Tóm tắt, Quyết định, Việc cần làm (table: task, owner, due) and the cleaned transcript. No paragraph over 120 words, mark unclear spots `[?]` and report their count, and say in the note that timestamps are the nearest source cue. Then pull out:

- topics covered and the mentee's key moments
- decisions made and what the mentee committed to do (action items, with owner and rough due date)
- the mentee's blockers, patterns and strengths shown
- anything Winnie promised during the session (to send, to show later, to explain), listed separately from the mentee's commitments
- anything the mentee said about Winnie's teaching (testimonial candidates). Never invent one; if there is none, say so
- anything reusable for class (WF-2 candidates), described generically with no names

Mark anything you are unsure of as `[to confirm]` rather than guessing.

## 4. Draft the public playback

Write 2 to 3 plain sentences on what was covered and what the mentee did or will do next. Public-safe only: no company names, no third parties, no candid assessment or weaknesses, no scores, nothing from the private recap. Strengths-framed and neutral. Show the draft and wait for the user to approve or edit it.

**Keep every mentee-facing playback generic** (the `--playback` text, and the session page in the mentee's Notion Coaching Program hub): no first person for Winnie ("mình", "tôi"), no mentee name, address the mentee as "bạn" only where needed. Write "Buổi học có demo…", "sẽ được gửi riêng", "Hướng dẫn sẽ được gửi sau", not "Mình demo…" or "Mình sẽ gửi…". Winnie appears by name only in the ADPList "Questions Between Sessions" footer. Before/after examples are in `_system/rules/vi-voice.md`.

## 5. Run the log script (after playback approval)

`python3 _system/scripts/mentee.py log <mentee> --topic "<topic>" --date YYYY-MM-DD --playback "<approved text>" --build`

Add `--n N` to edit an existing session, `--status` if not Completed, and `--lesson <slug>` if the output says no lesson matched and the user names one. This creates the private recap from the template under `mentees/<slug>/sessions/`.

## 6. Create the Notion playback page (after playback approval)

Search Notion for the page "Coaching Program - <Full Name>", then fetch the mentee's previous session page and copy its structure. Create the new page directly under the hub, next to the previous session page, titled `Session N — <Topic>` with the number emoji icon. Sections: Date and Status line, Parts 1..N of what was covered, From Your Live Project — Concerns & Coaching, Areas to Keep Developing, Your Committed Homework (Before Session N+1) as checkboxes, Examples from Other Learners (see below), Key Takeaway (next session date), Materials for This Session (use "sẽ được cập nhật sau" when there is no deck or recording link), Questions Between Sessions with the ADPList link. Follow the generic-playback rule in step 4: Vietnamese body, English headings, no mentee name, no first person for Winnie.

**Examples from Other Learners:** when Winnie promised examples, take homework for the same lesson from other mentees' `mentees/*/homework/<lesson-slug>/` folders. View each image first. Use an image only if it shows no person name and no brand or company name; describe the others in text instead. Upload images with `notion-create-file-upload`, then `curl` the file with a neutral filename (never the mentee's name), and embed with `<image source="file-upload://...">`. Tell Winnie which images were used and which were skipped and why, since project content may still need her check.

Fetch the page back once to confirm images render. Report the page link.

## 7. Fill the private recap

Fill the recap the script created from step 3, in Vietnamese per the Language note above: Session Summary, Topics Covered, Key Observations, Student Work Reviewed, Feedback Given, Commitments & Next Steps (homework and owners), My Notes as Trainer, Next Session Plan. Keep `draft: true`. Candid observations belong here, never in the playback. If the recap already exists (re-run or edit), check every quote in it against the transcript and flag any quote that does not appear there, instead of overwriting it.

## 8. Follow-up drafts (append to the recap under `## Follow-up drafts`)

- **Homework**: one clear task, expected output, due date, and the lesson or template it relates to. If the lesson has a homework section, reuse it rather than inventing a new task.
- **Learning log** (`learning-loop` skill): a draft entry of three lines for the mentee in Vietnamese: what they did, feedback they got (quote the recap's Feedback Given), what they will change. Add one reflection question from the session, such as "feedback nào hôm nay làm bạn đổi cách nghĩ?". Draft only; the mentee writes the final answer.
- **Next-session seed**: 3 bullets for `/prep` to pick up (open questions, what to check on the homework, what to teach next). Put the same bullets in the recap's Next Session Plan.

## 9. Testimonial capture

If step 3 found feedback about Winnie's teaching, apply the testimonial capture rule in CLAUDE.md in this same response: add it to `showcase/testimonials.md` (permission: not yet confirmed unless the user says otherwise) and to the mentee's own record. Tell the user it was added.

## 10. Homework files the user sends

When the user sends homework images or files, copy them to `mentees/<slug>/homework/<lesson-slug>/` (create the folder if missing) with a descriptive name and no mentee name, for example `design-process.webp`, `evaluate-current-experience.webp`. Note if a file carries a person's name, since it cannot be reused as an example without masking. Rebuild the site afterwards.

## 11. Report

The build prints a "Mentee health check". Pull out the lines for this mentee and say what is still open (missing playback, slides, dates, baseline). Then report:

- lesson link and slides found (the user should drop a deck named `Session N - ...` into the mentee's `slides/` folder if none)
- the private recap path and the follow-up drafts, ready to review
- WF-2 candidates, if any, as a short list (do not adapt them without asking)
- the Notion page link, and what is still waiting on the user: add deck and recording links to the Notion page, check the example images, and anything Winnie promised in the session

## 12. Preview (when asked, or after a site change)

Run `python3 _system/scripts/build-home.py`, then start the `docs` entry from `.claude/launch.json` (port 3002). If it answers 404, serve the folder yourself with `python3 -m http.server <port> --directory docs` on a free port, open `/mentees/<slug>.html`, and tell the user which port is running and that it stays up until stopped.

## 13. Final session only

If this was the programme's final session, follow the close-out rule in CLAUDE.md (close-out template, baseline vs reassessment, testimonial capture) and set `status: "completed"` and `end:` in `mentees/<slug>/mentee.md`, and fill the Post-training column of `mentees/<slug>/assessment.md` from the reassessment (numbers only). If no baseline is on file, flag that explicitly.
