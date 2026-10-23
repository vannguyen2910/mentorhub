#!/usr/bin/env python3
"""Sync a slide outline from its built deck (deck wins). Dry run unless --write.

Usage:
  python3 _system/scripts/sync-deck.py <lesson folder or outline.md> [--deck FILE] [--write]

What it does
  - Reads the deck (a Claude Design .dc.html bundle, or plain HTML with <section> slides).
  - Per slide: label, visible text, and the speaker notes in data-speaker-notes.
  - Slides already converted to the new notes format (they hold ">" verbatim lines) are kept
    untouched. Their deck notes are compared with the hash saved at the last sync, and any
    change is reported, never overwritten.
  - Every other slide is regenerated from the deck: notes carried over as bullets,
    [VÍ DỤ THỰC TẾ] and VÍ DỤ GỢI Ý mapped to the Ví dụ field.
  - Before a write that changes slide count or titles, the old outline and lesson are copied
    to materials/_archive/ as <name>-pre-deck-sync-YYYY-MM-DD.md.
  - The lesson file is never edited here; the report lists what to update in it.

State is kept in materials/.deck-sync.json (hashes of deck notes at the last sync).
"""
import datetime
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys

CONCEPT = {"NUMBERED", "COMPARE", "FORMULA", "STATEMENT", "DIAGRAM", "PROCESS", "QUOTE"}


def h(s):
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:10]


# ---------- deck ----------
def load_deck(path):
    src = open(path, encoding="utf-8").read()
    m = re.search(r'<script type="__bundler/template">\s*(.*?)</script>', src, re.S)
    if m:
        src = json.loads(m.group(1))
    body = re.sub(r"<style.*?</style>", "", src, flags=re.S)
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    slides = []
    for sec in re.findall(r"<section\b[^>]*>.*?</section>", body, flags=re.S):
        tag = re.match(r"<section\b[^>]*>", sec).group(0)
        nm = re.search(r'data-speaker-notes="([^"]*)"', tag)
        notes = html.unescape(nm.group(1)) if nm else ""
        text = html.unescape(re.sub(r"<[^>]+>", "\n", re.sub(r"<section\b[^>]*>", "", sec)))
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        slides.append({"lines": lines, "notes": notes})
    return slides


def parse_notes(raw):
    bullets, detail, real, sug, teach = [], None, None, None, False
    for ln in raw.splitlines():
        if not ln.strip():
            continue
        if ln.startswith("CHI TIẾT:"):
            detail = ln[len("CHI TIẾT:"):].strip()
        elif ln.startswith("[VÍ DỤ THỰC TẾ]"):
            real = ln[len("[VÍ DỤ THỰC TẾ]"):].strip()
        elif ln.startswith("VÍ DỤ GỢI Ý:"):
            sug = ln[len("VÍ DỤ GỢI Ý:"):].strip()
        else:
            if ln.startswith("VÍ DỤ THỰC TẾ ĐỂ DẠY"):
                teach = True
            if ln.startswith("•"):
                bullets.append(("-", ln[1:].strip()))
            elif ln.startswith("–"):
                bullets.append(("  -", ln[1:].strip()))
            else:
                bullets.append(("-", ln.strip()))
    return bullets, detail, real, sug, teach


def guess_layout(i, total, L, notes):
    if i == 1:
        return "COVER", False
    if i == total:
        return "END", False
    if len(L) <= 3 and re.fullmatch(r"\d\d", L[0]):
        return "SECTION DIVIDER", False
    if L[0].startswith("Build") or "Phút" in L[:5]:
        return "PRACTICE", False
    return "NUMBERED", True  # guessed


# ---------- existing outline ----------
def split_outline(text):
    i = text.index("\n## Slides")
    head, rest = text[:i], text[i:]
    parts = re.split(r"^### ", rest, flags=re.M)
    pre = parts[0]
    entries = ["### " + p for p in parts[1:]]
    cleaned = [re.sub(r"\n---\s*$", "", e.rstrip()).rstrip() for e in entries]
    return head, pre, cleaned


def entry_layout(e):
    return e.split("\n", 1)[0][4:].split("·")[0].strip()


def entry_title_line(e):
    return e.split("\n", 1)[0]


def is_converted(e):
    return bool(re.search(r"^\s*>\s", e, re.M))


def field(e, name):
    m = re.search(rf"^- {name}:\s*(.*)$", e, re.M)
    return m.group(1).strip() if m else ""


# ---------- entry generation ----------
def build_entry(n, total, slide, layout, guessed):
    L = slide["lines"]
    bl, detail, real, sug, teach = parse_notes(slide["notes"])
    out = []
    mins = None
    if layout == "COVER":
        out += ["### COVER", "- Year: 2026 · Winnie Nguyen", "- Title: " + " ".join(L[:3]),
                f"- Right panel photo: theo deck (slide {n:02d})"]
    elif layout == "SECTION DIVIDER":
        num, title = L[0], L[1]
        sub = L[2] if len(L) > 2 else ""
        out += [f"### SECTION DIVIDER · {title}", f"- Num: {num}", f"- Kicker: {title}",
                f"- Title: {title}", f"- Sub: {sub}"]
    elif layout == "PRACTICE":
        if L[0].startswith("Build"):
            kick, mins, title, rest = L[0], L[1], L[2], L[3:]
        else:
            kick, mins, title, rest = L[0], L[1], L[3], L[4:]
        out += [f"### PRACTICE · {kick}", f"- Num: {mins}", f"- Kicker: {kick}",
                f"- Title: {title}", "- On-slide: " + " | ".join(rest)]
    elif layout == "END":
        out += ["### END · " + L[0], f"- Kicker: {L[0]}", f"- Title: {L[1] if len(L) > 1 else ''}",
                "- On-slide: " + (" | ".join(L[2:]) or "None.")]
    else:
        kick, title = L[0], (L[1] if len(L) > 1 else "")
        out += [f"### {layout} · {kick}", f"- Kicker: {kick}", f"- Title: {title}",
                "- On-slide: " + (" | ".join(L[2:]) or "None.")]
    if layout != "COVER":
        part = re.search(r"Phần\s*\d+\s*·\s*(\d+)\s*phút", slide["notes"])
        if mins:
            gio = f"{mins} phút (theo deck)"
        elif layout == "SECTION DIVIDER" and part:
            gio = f"{part.group(1)} phút cho cả phần (theo deck)"
        else:
            gio = "[to confirm]"
        if teach:
            vd = "có (ví dụ dạy nằm trong notes của deck)"
        else:
            parts = []
            if real:
                parts.append("cần ví dụ: " + real)
            if sug:
                parts.append(f"bản nháp ({sug})")
            if not parts:
                parts.append("cần ví dụ: chưa đánh giá" if layout in CONCEPT else "Không cần.")
            vd = "; ".join(parts)
        out += [f"- Giờ: {gio}", f"- Ví dụ: {vd}", "- Câu hỏi hay gặp: None.", "- Speaker notes:"]
        for b, tx in bl:
            out.append(f"  {b} {tx}")
        if detail:
            out.append(f"  - Chi tiết (từ deck): {detail}")
        out.append("  - Ghi chú: carry-over từ deck, chưa chuyển sang dòng nguyên văn")
        out += ["", f"- 🎨 Visual hint: theo deck (slide {n:02d})."]
    if guessed:
        out.insert(1, "- Layout: đoán từ deck `[to confirm]`")
    return "\n".join(out)


FIELDS = re.compile(r"^- Giờ:.*\n- Ví dụ:.*\n- Câu hỏi hay gặp:.*(?:\n  - .*)*", re.M)


def keep_fields(oe, ne, notes_unchanged):
    """Keep Winnie's Giờ / Ví dụ / Câu hỏi hay gặp from the existing entry.
    If the deck notes changed since the last sync, take the fresh Ví dụ but keep Giờ and FAQ."""
    mo, mn = FIELDS.search(oe), FIELDS.search(ne)
    if not (mo and mn):
        return ne
    if notes_unchanged:
        block = mo.group(0)
    else:
        lo, ln = mo.group(0).split("\n"), mn.group(0).split("\n")
        block = "\n".join([lo[0], ln[1]] + lo[2:])
    return ne[:mn.start()] + block + ne[mn.end():]


# ---------- main ----------
def find_paths(arg):
    arg = os.path.abspath(arg)
    if arg.endswith(".md"):
        outline = arg
        mat = os.path.dirname(arg)
        lesson_dir = os.path.dirname(mat)
    else:
        lesson_dir = arg
        mat = os.path.join(arg, "materials")
        cands = [f for f in os.listdir(mat) if f.endswith("-slide-outline.md")]
        if len(cands) != 1:
            sys.exit(f"expected one *-slide-outline.md in {mat}, found {cands}")
        outline = os.path.join(mat, cands[0])
    lesson = outline.replace("-slide-outline.md", "-lesson.md")
    return lesson_dir, mat, outline, lesson


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    write = "--write" in sys.argv
    deck = None
    if "--deck" in sys.argv:
        deck = sys.argv[sys.argv.index("--deck") + 1]
        args = [a for a in args if a != deck]
    lesson_dir, mat, outline, lesson = find_paths(args[0])
    if not deck:
        sd = os.path.join(lesson_dir, "slides")
        c = [f for f in os.listdir(sd) if f.endswith(".html")] if os.path.isdir(sd) else []
        dc = [f for f in c if f.endswith(".dc.html")]
        pick = dc or c
        if len(pick) != 1:
            sys.exit(f"no single deck in {sd} (found {c}). Put the .html there or pass --deck.")
        deck = os.path.join(sd, pick[0])
    slides = load_deck(deck)
    total = len(slides)

    text = open(outline, encoding="utf-8").read()
    head, pre, old = split_outline(text)
    state_path = os.path.join(mat, ".deck-sync.json")
    state = json.load(open(state_path)) if os.path.exists(state_path) else {"slides": {}}

    new_entries, report = [], []
    for n, s in enumerate(slides, 1):
        oe = old[n - 1] if n <= len(old) else None
        nh = h(s["notes"])
        if oe and is_converted(oe):
            new_entries.append(oe)
            was = state["slides"].get(str(n), {}).get("notes_hash")
            if was and was != nh:
                report.append(f"  slide {n:>2}: GIỮ (đã chuyển format) nhưng notes trong deck đã đổi từ lần sync trước, xem lại")
            else:
                report.append(f"  slide {n:>2}: giữ nguyên (đã chuyển format)")
            continue
        layout, guessed = (entry_layout(oe), False) if oe else guess_layout(n, total, s["lines"], s["notes"])
        ne = build_entry(n, total, s, layout, guessed)
        if oe and layout == "COVER":
            ne = oe  # the cover block is locked
        elif oe:
            ne = keep_fields(oe, ne, state["slides"].get(str(n), {}).get("notes_hash") in (None, nh))
        if oe and ne == oe:
            report.append(f"  slide {n:>2}: không đổi")
        elif oe:
            report.append(f"  slide {n:>2}: tạo lại từ deck (có thay đổi)")
        else:
            report.append(f"  slide {n:>2}: MỚI trong deck" + (" (layout đoán)" if guessed else ""))
        new_entries.append(ne)
    removed = max(0, len(old) - total)

    old_titles = [entry_title_line(e) for e in old]
    new_titles = [entry_title_line(e) for e in new_entries]
    structure_changed = len(old) != total or old_titles != new_titles

    today = datetime.date.today().isoformat()
    new_head = re.sub(r"^slide_count:.*$", f"slide_count: {total}", head, flags=re.M)
    new_head = re.sub(r"^last_synced:.*$", f"last_synced: {today}", new_head, flags=re.M)
    new_head = re.sub(r"(## Slide structure — )\d+( slides)", rf"\g<1>{total}\g<2>", new_head)
    new_text = new_head + pre.rstrip("\n") + "\n\n" + "\n\n---\n\n".join(new_entries) + "\n"

    print(f"Deck: {os.path.relpath(deck)}  ({total} slides)")
    print(f"Outline: {os.path.relpath(outline)}  ({len(old)} slides before)")
    print("\n".join(report))
    if removed:
        print(f"  {removed} slide cuối của outline không còn trong deck")
    kept = sum(1 for r in report if "giữ" in r or "GIỮ" in r)
    print(f"\nTóm tắt: {kept} giữ nguyên (đã chuyển format), "
          f"{sum('tạo lại' in r for r in report)} tạo lại, {sum('MỚI' in r for r in report)} mới, "
          f"{sum('không đổi' in r for r in report)} không đổi.")
    print("Cấu trúc thay đổi: " + ("CÓ (cần archive)" if structure_changed else "không"))

    if os.path.exists(lesson):
        mins = [m.group(1) for e in new_entries if entry_layout(e) == "PRACTICE" for m in [re.search(r"^- Num: (\d+)", e, re.M)] if m]
        print("Số phút activity trong deck: " + ", ".join(mins) + "  -> đối chiếu với Session Structure trong lesson")

    if not write:
        print("\n(dry run: chưa ghi gì. Thêm --write để ghi.)")
        return
    if structure_changed:
        arch = os.path.join(mat, "_archive")
        os.makedirs(arch, exist_ok=True)
        for f in (outline, lesson):
            if os.path.exists(f):
                base = os.path.basename(f)[:-3]
                dst = os.path.join(arch, f"{base}-pre-deck-sync-{today}.md")
                if not os.path.exists(dst):
                    shutil.copy2(f, dst)
                    print("archived ->", os.path.relpath(dst))
    open(outline, "w", encoding="utf-8").write(new_text)
    state = {"deck": os.path.basename(deck), "synced": today,
             "slides": {str(n): {"notes_hash": h(s["notes"])} for n, s in enumerate(slides, 1)}}
    json.dump(state, open(state_path, "w"), indent=1, ensure_ascii=False)
    print("written:", os.path.relpath(outline))
    audit = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes-audit.py")
    print("\n--- notes-audit ---")
    subprocess.run([sys.executable, audit, outline])


if __name__ == "__main__":
    main()
