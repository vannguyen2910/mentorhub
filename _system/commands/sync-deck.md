---
description: Sync a lesson's slide outline from its built deck (deck wins), keep notes already converted to the new format, report drift, then audit the notes
argument-hint: <lesson folder, e.g. library/lessons/03-develop/information-architecture>
---

Sync the outline from the deck: $ARGUMENTS

Reads the deck, updates the outline, never edits the lesson file or the deck. Read `_system/rules/slide-deck-rules.md` → Speaker notes rule and `_system/rules/vi-voice.md` before writing any Vietnamese.

## 1. Find the deck

The deck is the single `.html` directly inside `<lesson>/slides/` (a Claude Design `.dc.html` bundle works). If `slides/` is empty, stop and ask Winnie to download the file and put it there. Do not copy it for her, and do not try to open a `claude.ai/design` link (it needs a login). A published `claude.ai/artifact/...` link can be read with the Artifact tool and saved to a file, then passed with `--deck`.

## 2. Dry run first

```
python3 _system/scripts/sync-deck.py <lesson folder>
```

It prints, per slide: unchanged, regenerated, new, or kept (already in the new notes format). Show Winnie the summary, and in particular:

- **GIỮ ... notes trong deck đã đổi**: a converted slide whose deck notes changed since the last sync. Show both versions side by side and ask which wins. Never overwrite.
- **Cấu trúc thay đổi: CÓ**: slide count or titles changed. A write will archive the old outline and lesson to `materials/_archive/` as `-pre-deck-sync-YYYY-MM-DD`.
- **MỚI (layout đoán)**: a new slide whose layout was guessed from the deck. Confirm the layout with Winnie.

## 3. Write

Only after Winnie has seen the dry run:

```
python3 _system/scripts/sync-deck.py <lesson folder> --write
```

It updates `slide_count` and `last_synced`, saves hashes to `materials/.deck-sync.json`, and runs `notes-audit.py`.

## 4. Lesson sync (by hand, per CLAUDE.md)

The script does not touch `*-lesson.md`. After a write that changed structure, compare with the lesson:

- Session Structure table: phases, timings (the activity minutes the script printed), buffer.
- Slides added or removed: does a lesson phase need a matching change?
- Add a short sync note at the top of the lesson and mark anything unclear `[to confirm]`.

## 5. Rebuild and report

Run `python3 _system/scripts/build-home.py` (site rebuild rule), then report in Vietnamese: what changed, what was kept, the audit flags, and what needs Winnie's decision.

## Rules

- Deck wins for structure, on-slide text and timing. Converted notes (lines starting with `>`) win over the deck's notes until Winnie decides.
- Do not write new `>` lines or examples here; converting a Part to the new notes format is a separate step done with Winnie.
- Examples written by Claude are marked `bản nháp`. No mentee names, no specific AI tool names.
