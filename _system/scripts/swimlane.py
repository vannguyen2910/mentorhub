"""Swimlane diagrams built from data, in the diagram-design skin (paper, ink, tangerine focal).

A data file `programs/<program>/assets/diagrams/<name>.swimlane.json` becomes `<name>.html` next to it
(one self-contained page, inline SVG, no script). `build-home.py` calls generate_all() on every build, and the
page is only rewritten when its content changes, so `--watch` does not loop.

Layout: one row per week, three lanes (columns). A card opens a detail box when it gets focus (CSS `:focus ~`).

  {
    "id": "weeks", "title": "...", "eyebrow": "...", "subtitle": "...", "description": "...",
    "lanes": ["THEORY", "PRACTICE", "OUTCOME"], "focal_label": "...",
    "rows": [ {"label": "TUẦN 1", "stage": "NỀN TẢNG", "focal": false,
               "cells": [ {"title": "...", "sub": "...", "details": ["..."]} | null, x3 ]} ]
  }
"""
import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape as e

NODE_W, NODE_H, ROW_H, HEAD_H, LABEL_W, COL_W, CH_PAD = 192, 56, 96, 40, 96, 216, 16
VW = LABEL_W + 3 * COL_W + CH_PAD

CSS = """
.dd{--paper:#f5f5f5;--ink:#2d3142;--muted:#4f5d75;--soft:#5a6580;--accent:#bf4520;--accent-tint:rgba(191,69,32,.08);--rule:rgba(45,49,66,.12);--label-rule:rgba(45,49,66,.20);--lane:rgba(45,49,66,.018);--dot:rgba(45,49,66,.10);--sans:'Geist',system-ui,sans-serif;--serif:'Instrument Serif',serif;--mono:'Geist Mono',ui-monospace,monospace}
.dd-fig{overflow-x:auto}.dd svg{display:block;width:100%;height:auto;max-width:800px;margin:0 auto}
.dd svg text{font-family:var(--sans)}.dd-lane{fill:var(--lane)}.dd-rule{stroke:var(--rule)}.dd-label-rule{stroke:var(--label-rule)}
.dd-actor{fill:var(--muted);font:500 8px var(--mono);letter-spacing:.12em}.dd-week{fill:var(--ink);font:600 8px var(--mono);letter-spacing:.08em}.dd-step-label{fill:var(--muted);font:500 6px var(--mono);letter-spacing:.12em}
.dd-connector{fill:none;stroke:var(--muted);stroke-width:1}.dd-connector.dd-focal{stroke:var(--accent);stroke-width:1.2}
.dd-node-mask{fill:var(--paper)}.dd-node{stroke-width:1}.dd-theory{fill:#fff;stroke:var(--ink)}.dd-practice{fill:rgba(79,93,117,.10);stroke:var(--soft)}.dd-outcome{fill:rgba(45,49,66,.05);stroke:var(--muted)}
.dd-node.dd-focal{fill:var(--accent-tint);stroke:var(--accent);stroke-width:1.2}
.dd-card{cursor:pointer;outline:none}.dd-card:focus .dd-node{stroke-width:2;stroke:var(--ink)}.dd-card:focus .dd-node.dd-focal{stroke:var(--accent)}
.dd-node-title{fill:var(--ink);font:600 10px var(--sans)}.dd-node-sub{fill:var(--muted);font:7.5px var(--mono)}
.dd-pop{display:none}.dd-pop-box{fill:#fff;stroke:var(--ink);stroke-width:1.2}.dd-pop-title{fill:var(--ink);font:600 10px var(--sans)}.dd-pop-line{fill:var(--muted);font:8.5px var(--sans)}
.dd-legend-key{fill:var(--muted);font:500 7px var(--mono);letter-spacing:.12em}.dd-legend-text{fill:var(--muted);font:8px var(--sans)}
"""

PAGE = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>%(title)s</title>
  <meta name="description" content="%(description)s">
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&amp;family=Geist:wght@400;500;600&amp;family=Geist+Mono:wght@400;500;600&amp;display=swap" rel="stylesheet">
  <style>
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
    body{font-family:'Geist',system-ui,sans-serif;background:#f5f5f5;color:#2d3142;padding:3rem 2rem}
    .frame{max-width:840px;margin:0 auto}
    .eyebrow{font:500 .66rem 'Geist Mono',ui-monospace,monospace;letter-spacing:.18em;text-transform:uppercase;color:#4f5d75;margin-bottom:.5rem}
    h1{font:400 clamp(1.5rem,2.4vw + .75rem,2rem)/1.15 'Instrument Serif',serif;letter-spacing:-.02em;margin-bottom:1.5rem}
    .embedded body{padding:.5rem 0 0}.embedded .eyebrow,.embedded h1{display:none}.embedded .dd svg{min-width:0!important}
%(css)s
  </style>
</head>
<body>
  <div class="frame dd">
    <p class="eyebrow">%(eyebrow)s</p>
    <h1>%(title)s</h1>
    <div class="dd-fig">
%(svg)s
    </div>
  </div>
</body>
</html>
"""


def _cells(row):
    cells = (list(row["cells"]) + [None, None, None])[:3]
    return cells, bool(row.get("focal"))


def render_svg(d):
    rows, lanes, sid = d["rows"], d["lanes"], d.get("id", "swimlane")
    leg_top = HEAD_H + len(rows) * ROW_H
    vh = leg_top + 72
    nx = lambda c: LABEL_W + c * COL_W + 12
    ny = lambda r: HEAD_H + r * ROW_H + 20
    ccx = lambda c: nx(c) + NODE_W // 2
    o = []
    a = o.append
    a(f'<svg viewBox="0 0 {VW} {vh}" xmlns="http://www.w3.org/2000/svg" style="min-width:{VW}px" role="img" aria-labelledby="{sid}-title {sid}-desc">')
    a(f'<title id="{sid}-title">{e(d["title"])}</title>')
    a(f'<desc id="{sid}-desc">{e(d["description"])}</desc>')
    a('<defs>'
      f'<pattern id="{sid}-dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="11" cy="11" r="0.8" fill="var(--dot)"/></pattern>'
      f'<marker id="{sid}-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="var(--muted)"/></marker>'
      f'<marker id="{sid}-arrow-accent" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="var(--accent)"/></marker>'
      '</defs>')
    a(f'<rect width="{VW}" height="{vh}" fill="var(--paper)"/><rect width="{VW}" height="{vh}" fill="url(#{sid}-dots)" opacity=".55"/>')
    for r in range(0, len(rows), 2):
        a(f'<rect class="dd-lane" x="0" y="{HEAD_H + r * ROW_H}" width="{VW}" height="{ROW_H}"/>')
    a('<g class="dd-rule" stroke-width=".8">' + "".join(
        f'<line x1="0" y1="{HEAD_H + r * ROW_H}" x2="{VW}" y2="{HEAD_H + r * ROW_H}"/>' for r in range(len(rows) + 1)) + '</g>')
    a(f'<line class="dd-label-rule" x1="{LABEL_W}" y1="0" x2="{LABEL_W}" y2="{leg_top}"/>')
    a('<g class="dd-actor" text-anchor="middle">' + "".join(
        f'<text x="{ccx(c)}" y="{HEAD_H // 2 + 3}">{e(n)}</text>' for c, n in enumerate(lanes)) + '</g>')
    for r, row in enumerate(rows):
        yy = HEAD_H + r * ROW_H + ROW_H // 2
        a(f'<text class="dd-week" x="{LABEL_W // 2}" y="{yy - 2}" text-anchor="middle">{e(row["label"])}</text>'
          f'<text class="dd-step-label" x="{LABEL_W // 2}" y="{yy + 11}" text-anchor="middle">{e(row.get("stage", ""))}</text>')

    # connectors first
    for r, row in enumerate(rows):
        cs, focal = _cells(row)
        present = [c for c in range(3) if cs[c]]
        for c1, c2 in zip(present, present[1:]):
            acc = focal and c2 == 2
            a(f'<line class="dd-connector{" dd-focal" if acc else ""}" x1="{nx(c1) + NODE_W + 3}" y1="{ny(r) + NODE_H // 2}" x2="{nx(c2) - 3}" y2="{ny(r) + NODE_H // 2}" '
              f'marker-end="url(#{sid}-arrow{"-accent" if acc else ""})"/>')
        if r + 1 < len(rows):
            nxt = [c for c in range(3) if _cells(rows[r + 1])[0][c]][0]
            yb, xo, xt = ny(r) + NODE_H, ccx(2), ccx(nxt)
            a(f'<path class="dd-connector{" dd-focal" if focal else ""}" d="M{xo} {yb + 3} V{yb + 12} a8 8 0 0 1 -8 8 H{xt + 8} a8 8 0 0 0 -8 8 V{ny(r + 1) - 4}" '
              f'marker-end="url(#{sid}-arrow{"-accent" if focal else ""})"/>')

    # cards are direct children of the svg so each popup can be a later sibling
    pops, cid = [], 0
    for r, row in enumerate(rows):
        cs, focal = _cells(row)
        for c in range(3):
            card = cs[c]
            if not card:
                continue
            cid += 1
            det = card.get("details", [])
            kind = ["dd-theory", "dd-practice", "dd-outcome"][c]
            f = " dd-focal" if (focal and c == 2) else ""
            x, y = nx(c), ny(r)
            label = f'{card["title"]}. {card.get("sub", "")}. ' + "; ".join(det)
            a(f'<g class="dd-card" id="c{cid}" tabindex="0" role="button" aria-label="{e(label, {chr(34): "&quot;"})}">'
              f'<rect class="dd-node-mask" x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H}" rx="6"/>'
              f'<rect class="dd-node {kind}{f}" x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H}" rx="6"/>'
              f'<text class="dd-node-title" x="{x + 12}" y="{y + 24}">{e(card["title"])}</text>'
              f'<text class="dd-node-sub" x="{x + 12}" y="{y + 41}">{e(card.get("sub", ""))}</text></g>')
            ph, pw = 30 + 14 * len(det), 308
            px = max(8, min(VW - pw - 8, x + NODE_W // 2 - pw // 2))
            py = y + NODE_H + 6
            if py + ph > vh - 8:
                py = y - ph - 6
            body = "".join(f'<text class="dd-pop-line" x="{px + 14}" y="{py + 40 + k * 14}">· {e(t)}</text>' for k, t in enumerate(det))
            pops.append(f'<g class="dd-pop" id="p{cid}"><rect class="dd-pop-box" x="{px}" y="{py}" width="{pw}" height="{ph}" rx="6"/>'
                        f'<text class="dd-pop-title" x="{px + 14}" y="{py + 20}">{e(card["title"])}</text>{body}</g>')
    o.extend(pops)

    lt, x0 = leg_top, 12
    a(f'<g><text class="dd-legend-key" x="{x0}" y="{lt + 20}">NODE</text>'
      f'<rect class="dd-node dd-theory" x="64" y="{lt + 11}" width="16" height="10" rx="2"/><text class="dd-legend-text" x="88" y="{lt + 20}">{e(lanes[0].title())}</text>'
      f'<rect class="dd-node dd-practice" x="152" y="{lt + 11}" width="16" height="10" rx="2"/><text class="dd-legend-text" x="176" y="{lt + 20}">{e(lanes[1].title())}</text>'
      f'<rect class="dd-node dd-outcome" x="248" y="{lt + 11}" width="16" height="10" rx="2"/><text class="dd-legend-text" x="272" y="{lt + 20}">{e(lanes[2].title())}</text>'
      f'<rect class="dd-node dd-focal" x="344" y="{lt + 11}" width="16" height="10" rx="2"/><text class="dd-legend-text" x="368" y="{lt + 20}">{e(d.get("focal_label", ""))}</text>'
      f'<text class="dd-legend-key" x="{x0}" y="{lt + 44}">FLOW</text>'
      f'<line x1="64" y1="{lt + 40}" x2="92" y2="{lt + 40}" stroke="var(--muted)" marker-end="url(#{sid}-arrow)"/><text class="dd-legend-text" x="104" y="{lt + 44}">Buổi kế tiếp</text>'
      f'<line x1="200" y1="{lt + 40}" x2="228" y2="{lt + 40}" stroke="var(--accent)" stroke-width="1.2" marker-end="url(#{sid}-arrow-accent)"/><text class="dd-legend-text" x="240" y="{lt + 44}">Tới và từ mốc</text>'
      f'<text class="dd-legend-key" x="{x0}" y="{lt + 64}">BẤM</text><text class="dd-legend-text" x="64" y="{lt + 64}">Bấm hoặc Tab tới một thẻ để xem chi tiết; bấm ra ngoài để đóng.</text></g>')
    a('</svg>')
    return "\n".join(o), cid


def render_page(d):
    svg, n = render_svg(d)
    css = CSS + "".join(f"#c{i}:focus~#p{i}{{display:block}}" for i in range(1, n + 1))
    return PAGE % {"title": e(d["title"]), "description": e(d["subtitle"], {'"': "&quot;"}), "eyebrow": e(d["eyebrow"]), "css": css, "svg": svg}


def generate(data_path):
    """Write the page next to its data file. Returns 'updated', 'unchanged'."""
    data_path = Path(data_path)
    out = data_path.with_name(data_path.name[: -len(".swimlane.json")] + ".html")
    page = render_page(json.loads(data_path.read_text(encoding="utf-8")))
    if out.exists() and out.read_text(encoding="utf-8") == page:
        return out, "unchanged"
    out.write_text(page, encoding="utf-8")
    return out, "updated"


def generate_all(programs_dir):
    for f in sorted(Path(programs_dir).glob("*/assets/diagrams/*.swimlane.json")):
        try:
            out, state = generate(f)
            print(f"  diagram {out.name}: {state}")
        except (KeyError, ValueError) as err:
            print(f"  ! diagram {f.name}: {err!r} (page left as it was)")


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(*generate(arg))
