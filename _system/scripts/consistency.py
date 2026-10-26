"""Cross-reference checks for a program, so one change shows up everywhere it is mentioned.

Reads `programs/<program>/learning/consistency.json` and reports, per program:
  terms      words or numbers that were retired or renamed but still appear (rule list in the config)
  mentions   facts that must appear in every file that depends on them (a file name, a title)
  outlines   slide_count in a slide outline against the slides it really holds
  practices  minutes of a practice sheet against its session length
  diagrams   the swimlane data against plan.md and the README totals
  lessons    lesson folders missing a file
  links      links on the built hub pages that lead nowhere

It only reports; it never edits. `build-home.py` prints the summary after each build.
  python3 _system/scripts/consistency.py            full report
  python3 _system/scripts/consistency.py --strict   exit 1 when something is wrong
"""
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
PROGRAMS = ROOT / "programs"
DOCS = ROOT / "docs"


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            if _:
                meta[k.strip()] = v.strip().strip('"')
    return meta


def files(root, globs, ignore=("_archive",)):
    seen = set()
    for g in globs:
        for p in sorted(root.glob(g)):
            if p.is_file() and not any(i in p.parts for i in ignore):
                seen.add(p)
    return sorted(seen)


def check_terms(root, cfg):
    out = []
    for rule in cfg.get("terms", []):
        pat = re.compile(rule["pattern"], re.I)
        allow = [re.compile(a, re.I) for a in rule.get("allow", [])]
        for p in files(root, rule["scope"]):
            for n, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                if pat.search(line) and not any(a.search(line) for a in allow):
                    out.append((f"{p.relative_to(root)}:{n}", rule["why"], line.strip()[:90]))
    return out


def check_mentions(root, cfg):
    out = []
    for item in cfg.get("mentions", []):
        for rel in item["in"]:
            p = root / rel
            if not p.exists():
                out.append((rel, f'file missing, expected to mention "{item["term"]}"', ""))
            elif item["term"] not in p.read_text(encoding="utf-8", errors="replace"):
                out.append((rel, f'does not mention "{item["term"]}"', item.get("why", "")))
    return out


def check_outlines(root):
    out = []
    for p in sorted(root.glob("lessons/*/materials/*-slide-outline.md")):
        text = p.read_text(encoding="utf-8")
        declared = front_matter(text).get("slide_count")
        count = 0
        for line in text.splitlines():
            if line.startswith("### "):
                count += 1
                if line.startswith("### END"):
                    break   # slides after END are reference slides and are not counted
        if declared and declared.isdigit() and int(declared) != count:
            out.append((str(p.relative_to(root)), f"slide_count says {declared} but the outline holds {count} slides", ""))
    return out


def check_practices(root):
    out, info = [], []
    for p in sorted(root.glob("lessons/*/materials/*-practice.md")):
        text = p.read_text(encoding="utf-8")
        minutes = sum(int(m) for m in re.findall(r"^### Step \d+ · .*? · (\d+) phút", text, re.M))
        limit = int(re.match(r"\d+", front_matter(text).get("duration", "90")).group(0))
        if minutes > limit:
            out.append((str(p.relative_to(root)), f"steps add up to {minutes} min, session is {limit}", ""))
        else:
            info.append(f"{p.name}: {minutes} of {limit} min planned")
    return out, info


def check_diagrams(root):
    out = []
    plan = root / "learning" / "plan.md"
    plan_text = plan.read_text(encoding="utf-8").lower() if plan.exists() else ""
    readme = front_matter((root / "README.md").read_text(encoding="utf-8")) if (root / "README.md").exists() else {}
    for p in sorted(root.glob("assets/diagrams/*.swimlane.json")):
        rows = json.loads(p.read_text(encoding="utf-8"))["rows"]
        theory = [r["cells"][0]["title"] for r in rows if r["cells"][0]]
        for t in theory:
            if t.lower() not in plan_text:
                out.append((str(p.relative_to(root)), f'lesson "{t}" is not in learning/plan.md', ""))
        total = readme.get("lessons_total")
        if total and total.isdigit() and int(total) != len(theory):
            out.append((str(p.relative_to(root)), f"diagram has {len(theory)} lessons, README says lessons_total {total}", ""))
    return out


def check_lessons(root):
    out, todo = [], []
    for d in sorted(root.glob("lessons/[0-9]*")):
        m = d / "materials"
        for suffix in ("lesson", "slide-outline"):
            if not list(m.glob(f"*-{suffix}.md")):
                out.append((str(d.relative_to(root)), f"no *-{suffix}.md", ""))
        if not list(m.glob("*-practice.md")) and d.name != "07-wrap-up":
            todo.append(f"{d.name}: no practice sheet yet")
    return out, todo


def check_links(root):
    out, slug = [], root.name
    site = DOCS / "programs"
    pages = sorted((site / slug).glob("*.html")) + [site / f"{slug}.html"]
    for f in pages:
        if not f.exists() or f.name.endswith("-frame.html"):
            continue
        s = f.read_text(encoding="utf-8")
        for m in re.finditer(r'<(?:a|img)\b[^>]*?(?:href|src)="([^"]+)"', s):
            u = html.unescape(m.group(1))
            if re.match(r"^(https?:|mailto:|data:|#|javascript:)", u):
                continue
            t = (f.parent / unquote(u.split("#")[0].split("?")[0])).resolve()
            if not t.exists():
                out.append((f.name[-70:], "link goes nowhere", u))
    return out


def run(programs_dir=PROGRAMS, details=True, out=print):
    """Returns the number of problems found across programs that have a consistency.json."""
    total = 0
    for cfg_path in sorted(Path(programs_dir).glob("*/learning/consistency.json")):
        root = cfg_path.parent.parent
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        prac, info = check_practices(root)
        les, todo = check_lessons(root)
        groups = [("terms", check_terms(root, cfg)), ("mentions", check_mentions(root, cfg)),
                  ("outlines", check_outlines(root)), ("practices", prac),
                  ("diagrams", check_diagrams(root)), ("lessons", les), ("links", check_links(root))]
        n = sum(len(g) for _, g in groups)
        total += n
        out(f"consistency {root.name}: " + ("all checks pass" if not n else f"{n} to fix ("
            + ", ".join(f"{len(g)} {name}" for name, g in groups if g) + ")"))
        if details:
            for name, items in groups:
                for where, why, extra in items:
                    out(f"  [{name}] {where}: {why}" + (f"  | {extra}" if extra else ""))
            for line in info + todo:
                out(f"  note: {line}")
    return total


if __name__ == "__main__":
    n = run()
    if "--strict" in sys.argv and n:
        sys.exit(1)
