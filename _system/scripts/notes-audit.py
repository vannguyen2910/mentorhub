#!/usr/bin/env python3
"""Audit speaker notes in a *-slide-outline.md. Report only: never writes to the outline.

Usage: python3 _system/scripts/notes-audit.py <outline.md> [--json]

Checks per slide (rules: _system/rules/slide-deck-rules.md -> Speaker notes rule):
  - has Ví dụ field
  - verbatim (">") line count and bullet count
  - bracketed stage directions inside the notes
  - estimated spoken minutes (130-150 words a minute)
  - concept layouts with no example status
  - Title over 6 words, Kicker with a Phần/Buổi number, Kicker repeating Title
"""
import json
import re
import sys

CONCEPT = {"NUMBERED", "COMPARE", "FORMULA", "STATEMENT", "DIAGRAM", "PROCESS", "QUOTE"}
SKIP_EXAMPLE = {"COVER", "SECTION DIVIDER", "MILESTONE", "END", "IMAGE", "PRACTICE"}
WPM_LOW, WPM_HIGH = 130, 150
# Title and kicker copy rule: _system/rules/slide-deck-rules.md. STATEMENT titles may be a full sentence.
NO_TITLE_CHECK = {"COVER", "SECTION DIVIDER", "END", "STATEMENT"}
TITLE_MAX_WORDS = 6


def words(text):
    return len(re.findall(r"\w+", text, flags=re.UNICODE))


def split_slides(src):
    parts = re.split(r"^### ", src, flags=re.M)[1:]
    slides = []
    for i, part in enumerate(parts, 1):
        head, _, body = part.partition("\n")
        layout = head.split("·")[0].strip()
        title = head.split("·", 1)[1].strip() if "·" in head else ""
        slides.append({"n": i, "layout": layout, "label": title, "body": body})
    return slides


def field(body, name):
    m = re.search(rf"^- {name}:\s*(.*)$", body, flags=re.M)
    return m.group(1).strip() if m else None


def notes_block(body):
    m = re.search(r"^- Speaker notes:\s*\n(.*?)(?=^- [^\s]|\Z)", body, flags=re.M | re.S)
    return m.group(1) if m else ""


def audit(path):
    src = open(path, encoding="utf-8").read()
    rows = []
    for s in split_slides(src):
        notes = notes_block(s["body"])
        lines = [l.strip() for l in notes.splitlines() if l.strip()]
        verbatim = [l for l in lines if l.startswith(">")]
        bullets = [l for l in lines if re.match(r"^[-*] ", l)]
        spoken = words(" ".join(verbatim + bullets))
        vidu = field(s["body"], "Ví dụ")
        issues = []
        if s["layout"] not in NO_TITLE_CHECK:
            title = (field(s["body"], "Title") or "").replace("\\n", " ").replace("*", "")
            kicker = field(s["body"], "Kicker") or ""
            if words(title) > TITLE_MAX_WORDS:
                issues.append(f"Title {words(title)} từ (>{TITLE_MAX_WORDS}), rút thành nhãn chủ đề")
            if re.match(r"^(Phần|Buổi)\s*\d", kicker):
                issues.append("Kicker mang số Phần/Buổi")
            if kicker and kicker.lower() == title.strip().lower():
                issues.append("Kicker lặp Title")
        if not notes.strip():
            issues.append("không có speaker notes")
        if re.search(r"\[[^\]]*\]", re.sub(r"\[[^\]]*\]\([^)]*\)", "", notes)):
            issues.append("có chỉ dẫn trong ngoặc vuông")
        if len(bullets) > 8:
            issues.append(f"{len(bullets)} bullet (>8), cân nhắc tách slide")
        if s["layout"] not in {"COVER", "END"} and notes.strip() and not verbatim:
            issues.append("chưa có câu nguyên văn (>)")
        if s["layout"] in CONCEPT and not vidu:
            issues.append("thiếu field Ví dụ")
        if vidu and vidu.lower().startswith("cần ví dụ"):
            issues.append("đang chờ ví dụ")
        if vidu and vidu.lower().startswith("bản nháp"):
            issues.append("ví dụ bản nháp, chờ xác nhận")
        est = round(spoken / ((WPM_LOW + WPM_HIGH) / 2), 1)
        rows.append({
            "n": s["n"], "layout": s["layout"], "label": s["label"],
            "verbatim": len(verbatim), "bullets": len(bullets),
            "words": spoken, "est_min": est, "vi_du": vidu,
            "issues": issues,
        })
    return rows


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    rows = audit(sys.argv[1])
    if "--json" in sys.argv:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return
    print(f"{'#':>2}  {'Layout':<16} {'>':>2} {'•':>2} {'từ':>4} {'~ph':>4}  Vấn đề")
    for r in rows:
        print(f"{r['n']:>2}  {r['layout']:<16} {r['verbatim']:>2} {r['bullets']:>2} "
              f"{r['words']:>4} {r['est_min']:>4}  {'; '.join(r['issues']) or 'ok'}")
    flagged = sum(1 for r in rows if r["issues"])
    print(f"\n{flagged}/{len(rows)} slide có vấn đề.")


if __name__ == "__main__":
    main()
