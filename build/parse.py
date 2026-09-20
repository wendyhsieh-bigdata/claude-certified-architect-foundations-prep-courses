#!/usr/bin/env python3
"""Parse the seven overview_*.md files into structured data for the study site.

Usage:  python3 build/parse.py
Output: site/data/course-*.js, site/data/meta.js, and site/data/guide.js
        (guide.js is built from guide_ccaf_zh.md — a separate study guide page)

The Markdown used in the overviews is deliberately limited (headings, paragraphs,
pipe tables, fenced code, ordered/unordered lists with 2-space nesting,
blockquotes, bold, italics, inline code, links, horizontal rules), so a small
purpose-built converter is used instead of a third-party dependency.
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

# Hand-set metadata per course. Order = display order inside each track.
COURSES = [
    {
        "id": "ai-fluency",
        "file": "overview_Introduction_to_AI_Fluency.md",
        "short": "AI Fluency",
        "track": "general",
        "platform": None,
        "audience": "非技術、所有人",
        "tagline": "與 AI 協作的思考框架（4D）",
    },
    {
        "id": "claude-101",
        "file": "overview_Claude101.md",
        "short": "Claude 101",
        "track": "general",
        "platform": None,
        "audience": "一般知識工作者",
        "tagline": "claude.ai 全功能地圖與選用判斷",
    },
    {
        "id": "claude-api",
        "file": "overview_Building_with_the_Claude_API.md",
        "short": "Claude API",
        "track": "dev",
        "platform": "api",
        "audience": "開發者（Python）",
        "tagline": "Anthropic 直連 API 的完整開發路徑",
    },
    {
        "id": "bedrock",
        "file": "overview_Claude_with_Amazon_Bedrock.md",
        "short": "Amazon Bedrock",
        "track": "dev",
        "platform": "bedrock",
        "audience": "開發者（AWS）",
        "tagline": "同一門開發課的 AWS Bedrock 版本",
    },
    {
        "id": "vertex",
        "file": "overview_Claude_on_Google_Cloud.md",
        "short": "Google Cloud",
        "track": "dev",
        "platform": "vertex",
        "audience": "開發者（GCP）",
        "tagline": "同一門開發課的 Vertex AI 版本",
    },
    {
        "id": "mcp",
        "file": "overview_Introduction_to_Model_Context_Protocol.md",
        "short": "Intro to MCP",
        "track": "dev",
        "platform": None,
        "audience": "開發者（Python）",
        "tagline": "親手做一次 MCP server 與 client",
    },
    {
        "id": "claude-code",
        "file": "overview_Claude_Code_in_Action.md",
        "short": "Claude Code in Action",
        "track": "dev",
        "platform": None,
        "audience": "開發者（進階）",
        "tagline": "放手讓 Claude Code 自動化，同時掌控品質",
    },
]

CALLOUT_RE = re.compile(r"搞混|陷阱|誤解|易錯|最常|最易|注意|千萬|務必|不要|別")
# Terms defined inline as **Term**（中文說明）
GLOSSARY_RE = re.compile(r"\*\*([^*\n]{1,40}?)\*\*（([^（）\n]{2,80})）")

# --------------------------------------------------------------------------- inline

def inline(text: str) -> str:
    """Convert inline Markdown to HTML (escaping first)."""
    # protect inline code
    codes: list[str] = []

    def stash(m: re.Match) -> str:
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    text = re.sub(r"(?<![\w*\"'=])(https?://[^\s<）\"]+)", r'<a href="\1" target="_blank" rel="noopener">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", text)

    def unstash(m: re.Match) -> str:
        return f"<code>{html.escape(codes[int(m.group(1))], quote=False)}</code>"

    return re.sub("\x00(\\d+)\x00", unstash, text)


def strip_md(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+?)\*", r"\1", text)
    return text.strip()

# --------------------------------------------------------------------------- blocks

def parse_table(lines: list[str]) -> dict:
    rows = []
    for ln in lines:
        ln = ln.strip()
        if re.match(r"^\|?\s*:?-{2,}", ln):
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        rows.append(cells)
    headers = rows[0] if rows else []
    body = rows[1:]
    return {
        "type": "table",
        "headers": [inline(h) for h in headers],
        "rows": [[inline(c) for c in r] for r in body],
    }


def parse_blocks(lines: list[str]) -> list[dict]:
    blocks: list[dict] = []
    i = 0
    n = len(lines)
    while i < n:
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1
            continue
        # fenced code
        if s.startswith("```"):
            lang = s[3:].strip()
            j = i + 1
            buf = []
            while j < n and not lines[j].strip().startswith("```"):
                buf.append(lines[j])
                j += 1
            blocks.append({"type": "code", "lang": lang, "text": "\n".join(buf)})
            i = j + 1
            continue
        # hr
        if re.match(r"^-{3,}$", s):
            blocks.append({"type": "hr"})
            i += 1
            continue
        # table
        if s.startswith("|"):
            j = i
            buf = []
            while j < n and lines[j].strip().startswith("|"):
                buf.append(lines[j])
                j += 1
            blocks.append(parse_table(buf))
            i = j
            continue
        # blockquote
        if s.startswith(">"):
            j = i
            buf = []
            while j < n and lines[j].strip().startswith(">"):
                buf.append(lines[j].strip()[1:].strip())
                j += 1
            text = " ".join(b for b in buf if b)
            blocks.append({"type": "quote", "html": inline(text)})
            i = j
            continue
        # list
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", ln)
        if m and len(m.group(1)) == 0:
            ordered = m.group(2)[0].isdigit()
            items = []
            j = i
            while j < n:
                mm = re.match(r"^([-*]|\d+\.)\s+(.*)$", lines[j])
                if not mm or (mm.group(1)[0].isdigit()) != ordered:
                    if lines[j].strip() == "" or lines[j].startswith("  "):
                        # continuation / nested content of current item
                        if not items:
                            break
                        items[-1]["raw"].append(lines[j][2:] if lines[j].startswith("  ") else "")
                        j += 1
                        continue
                    break
                items.append({"head": mm.group(2), "raw": []})
                j += 1
            out_items = []
            for it in items:
                nested = [x for x in it["raw"]]
                # trim trailing blanks
                while nested and not nested[-1].strip():
                    nested.pop()
                children = parse_blocks(nested) if any(x.strip() for x in nested) else []
                text = strip_md(it["head"])
                item = {"html": inline(it["head"]), "callout": bool(CALLOUT_RE.search(text))}
                if children:
                    item["children"] = children
                out_items.append(item)
            blocks.append({"type": "list", "ordered": ordered, "items": out_items})
            i = j
            continue
        # paragraph (until blank line or structural start)
        j = i
        buf = []
        while j < n:
            t = lines[j]
            ts = t.strip()
            if not ts or ts.startswith(("|", ">", "```", "#")) or re.match(r"^-{3,}$", ts) or re.match(r"^([-*]|\d+\.)\s+", t):
                break
            buf.append(ts)
            j += 1
        if not buf:  # a line we could not classify (e.g. stray heading) – skip it
            i += 1
            continue
        text = " ".join(buf)
        plain = strip_md(text)
        blocks.append({"type": "p", "html": inline(text), "callout": bool(CALLOUT_RE.search(plain))})
        i = j
    return blocks

# --------------------------------------------------------------------------- document

def split_heading(line: str):
    m = re.match(r"^(#{1,6})\s+(.*)$", line)
    if not m:
        return None
    return len(m.group(1)), m.group(2).strip()


def slugify(text: str, used: set[str]) -> str:
    base = re.sub(r"[^\w一-鿿-]+", "-", strip_md(text)).strip("-").lower()[:60] or "s"
    slug = base
    k = 2
    while slug in used:
        slug = f"{base}-{k}"
        k += 1
    used.add(slug)
    return slug


def parse_units(section_lines: list[str], used: set[str]) -> list[dict]:
    """Within '各單元內容導讀': h3 = unit, h4 = sub-unit (when present)."""
    units: list[dict] = []
    cur = None
    sub = None
    buf: list[str] = []

    def flush():
        nonlocal buf
        if not buf:
            return
        blocks = parse_blocks(buf)
        buf = []
        if sub is not None:
            sub["blocks"].extend(blocks)
        elif cur is not None:
            cur["blocks"].extend(blocks)

    for ln in section_lines:
        h = split_heading(ln)
        if h and h[0] == 3:
            flush()
            sub = None
            cur = {"title": strip_md(h[1]), "title_html": inline(h[1]), "slug": slugify(h[1], used), "blocks": [], "subunits": []}
            units.append(cur)
        elif h and h[0] == 4 and cur is not None:
            flush()
            sub = {"title": strip_md(h[1]), "title_html": inline(h[1]), "slug": slugify(h[1], used), "blocks": []}
            cur["subunits"].append(sub)
        else:
            buf.append(ln)
    flush()
    for u in units:
        u["summary"] = first_sentence(u)
        u["callout_count"] = len(collect_callouts(u["blocks"])) + sum(len(collect_callouts(s["blocks"])) for s in u["subunits"])
    return units


def first_sentence(unit: dict) -> str:
    blocks = unit["blocks"] or (unit["subunits"][0]["blocks"] if unit["subunits"] else [])
    for b in blocks:
        if b["type"] == "p":
            t = html.unescape(re.sub(r"<[^>]+>", "", b["html"]))
            return (t[:90] + "…") if len(t) > 90 else t
    return ""


def collect_callouts(blocks: list[dict]) -> list[str]:
    out = []
    for b in blocks:
        if b["type"] == "p" and b.get("callout"):
            out.append(b["html"])
        if b["type"] == "list":
            for it in b["items"]:
                if it.get("callout"):
                    out.append(it["html"])
    return out


def parse_course(meta: dict) -> dict:
    text = (ROOT / meta["file"]).read_text(encoding="utf-8")
    lines = text.splitlines()
    used: set[str] = set()

    title = ""
    head_meta: list[str] = []
    sections: dict[str, list[str]] = {"intro": [], "keys": [], "units": [], "takeaways": [], "footer": []}
    current = None
    for ln in lines:
        h = split_heading(ln)
        if h and h[0] == 1:
            title = h[1]
            continue
        if h and h[0] == 2:
            t = h[1]
            if t.startswith("這門課在講什麼"):
                current = "intro"
            elif t.startswith("先記住"):
                current = "keys"
                sections.setdefault("keys_title", []).append(t)
            elif t.startswith("各單元內容導讀"):
                current = "units"
            elif t.startswith("讀完這門課"):
                current = "takeaways"
            else:
                current = "footer"
            continue
        if current is None:
            if ln.strip().startswith(">"):
                head_meta.append(ln.strip()[1:].strip())
            continue
        sections[current].append(ln)

    # takeaways: content up to the final '---' (copyright line after it goes to footer)
    tk = sections["takeaways"]
    footer_note = ""
    for idx in range(len(tk) - 1, -1, -1):
        if re.match(r"^-{3,}$", tk[idx].strip()):
            footer_note = " ".join(x.strip() for x in tk[idx + 1:] if x.strip())
            tk = tk[:idx]
            break

    # key tables section: keep h3 sub-headings as labelled groups
    key_groups = []
    grp = None
    buf: list[str] = []

    def flush_grp():
        nonlocal buf, grp
        if buf and any(x.strip() for x in buf):
            blocks = parse_blocks(buf)
            if grp is None:
                grp = {"title": "", "blocks": []}
                key_groups.append(grp)
            grp["blocks"].extend(blocks)
        buf = []

    for ln in sections["keys"]:
        h = split_heading(ln)
        if h and h[0] == 3:
            flush_grp()
            grp = {"title": strip_md(h[1]), "title_html": inline(h[1]), "blocks": []}
            key_groups.append(grp)
        else:
            buf.append(ln)
    flush_grp()

    units = parse_units(sections["units"], used)
    plain_len = len(re.sub(r"\s+", "", strip_md(text)))

    course = dict(meta)
    course.update({
        "title": strip_md(title.replace("— 課程導讀", "").strip()),
        "head_meta": [inline(m) for m in head_meta],
        "intro": parse_blocks(sections["intro"]),
        "keys_title": strip_md((sections.get("keys_title") or [""])[0]),
        "key_groups": key_groups,
        "units": units,
        "takeaways": parse_blocks(tk),
        "footer": inline(footer_note),
        "chars": plain_len,
        "read_minutes": max(3, round(plain_len / 400)),
        "unit_count": sum(max(1, len(u["subunits"])) for u in units),
        "callout_count": sum(u["callout_count"] for u in units),
    })
    course["glossary"] = extract_glossary(text)
    return course


def extract_glossary(text: str) -> list[dict]:
    seen = set()
    out = []
    for m in GLOSSARY_RE.finditer(text):
        term = strip_md(m.group(1))
        definition = m.group(2).strip()
        key = term.lower()
        cjk = len(re.findall(r"[\u4e00-\u9fff]", term))
        if key in seen or len(term) > 32 or len(term) <= 2 or re.match(r"^\d", term) or cjk > 8 or re.search(r"[。！？，]", term):
            continue
        # skip parenthetical that is clearly an example/aside rather than a definition
        if definition.startswith(("如", "例如", "見", "例：", "即")) and len(definition) > 30:
            continue
        seen.add(key)
        out.append({"term": term, "def": inline(definition)})
    return out


# --------------------------------------------------------------------------- study guide (separate page)

GUIDE_FILE = "guide_ccaf_zh.md"
GUIDE_SOURCE = {
    "label": "paullarionov/claude-certified-architect — guide_en.md",
    "url": "https://github.com/paullarionov/claude-certified-architect/blob/main/guide_en.md",
}
QUIZ_MARK = "<!-- quiz -->"
Q_TITLE_RE = re.compile(r"^第\s*(\d+)\s*題(?:（情境：(.+?)）)?$")


def _strip_prefix(html_text: str, label_re: str) -> str:
    """Remove a leading <strong>label</strong> from a paragraph's HTML."""
    return re.sub(r"^\s*<strong>" + label_re + r"</strong>\s*", "", html_text, count=1).strip()


def _no_callouts(blocks: list[dict]) -> list[dict]:
    for b in blocks:
        if b["type"] == "p":
            b["callout"] = False
        elif b["type"] == "list":
            for it in b["items"]:
                it["callout"] = False
                if it.get("children"):
                    _no_callouts(it["children"])
    return blocks


def parse_guide_page_blocks(lines: list[str], used: set[str]) -> tuple[list[dict], list[dict]]:
    """Text page: h3/h4 become heading blocks so the page reads top-to-bottom. Returns (blocks, headings)."""
    blocks: list[dict] = []
    headings: list[dict] = []
    buf: list[str] = []
    in_code = False

    def flush():
        nonlocal buf
        if any(x.strip() for x in buf):
            blocks.extend(_no_callouts(parse_blocks(buf)))
        buf = []

    for ln in lines:
        if ln.strip().startswith("```"):
            in_code = not in_code
        h = None if in_code else split_heading(ln)
        if h and h[0] in (3, 4):
            flush()
            slug = slugify(h[1], used)
            level = 2 if h[0] == 3 else 3
            blocks.append({"type": "h", "level": level, "html": inline(h[1]), "slug": slug})
            if level == 2:
                headings.append({"slug": slug, "title": strip_md(h[1])})
        else:
            buf.append(ln)
    flush()
    return blocks, headings


def parse_question(title: str, lines: list[str]) -> dict:
    m = Q_TITLE_RE.match(strip_md(title))
    num = int(m.group(1)) if m else 0
    scenario = (m.group(2) or "").strip() if m else ""
    blocks = _no_callouts(parse_blocks(lines))
    situation = ""
    stem = ""
    options: list[dict] = []
    why: list[str] = []
    seen_list = False
    for b in blocks:
        if b["type"] == "list" and not seen_list:
            seen_list = True
            for it in b["items"]:
                raw = it["html"]
                correct = "【正確】" in raw
                raw = re.sub(r"\s*<strong>【正確】</strong>\s*", "", raw).strip()
                lm = re.match(r"^([A-D])\)\s*(.*)$", raw, re.S)
                letter = lm.group(1) if lm else chr(ord("A") + len(options))
                text = lm.group(2) if lm else raw
                options.append({"letter": letter, "html": text, "correct": correct})
        elif b["type"] == "p":
            plain = html.unescape(re.sub(r"<[^>]+>", "", b["html"]))
            if not seen_list and plain.startswith("情境："):
                situation = _strip_prefix(b["html"], "情境：")
            elif not seen_list:
                stem = re.sub(r"^<strong>(.*)</strong>$", r"\1", b["html"].strip())
            else:
                why.append(_strip_prefix(b["html"], r"為什麼選\s*[A-D]：?"))
    answer = next((o["letter"] for o in options if o["correct"]), "")
    return {
        "n": num, "scenario": scenario, "situation": situation, "stem": stem,
        "options": options, "answer": answer, "why": " ".join(why),
    }


def parse_guide() -> dict | None:
    path = ROOT / GUIDE_FILE
    if not path.exists():
        return None
    lines = path.read_text(encoding="utf-8").splitlines()
    used: set[str] = set()

    title = ""
    preamble: list[str] = []
    parts: list[dict] = []
    pages: list[dict] = []
    # raw collection: each page = {"part": idx, "title": str, "lines": [...], "quiz": bool}
    cur_page = None
    in_code = False
    state = "pre"
    for ln in lines:
        if ln.strip().startswith("```"):
            in_code = not in_code
        h = None if in_code else split_heading(ln)
        if h and h[0] == 1:
            if not title:
                title = h[1]
                continue
            parts.append({"title": strip_md(h[1]), "title_html": inline(h[1]), "pages": []})
            cur_page = None
            state = "part"
            continue
        if h and h[0] == 2 and parts:
            cur_page = {"part": len(parts) - 1, "title": h[1], "lines": [], "quiz": False}
            pages.append(cur_page)
            continue
        if cur_page is not None:
            if ln.strip() == QUIZ_MARK:
                cur_page["quiz"] = True
            else:
                cur_page["lines"].append(ln)
        elif state == "pre":
            preamble.append(ln)

    def page_slug(pg: dict, n: int) -> str:
        t = strip_md(pg["title"])
        m = re.match(r"^第\s*(\d+)\s*章", t)
        if m:
            base = f"ch-{m.group(1)}"
        else:
            m = re.match(r"^Domain\s*(\d+)", t, re.I)
            base = f"domain-{m.group(1)}" if m else ("quiz" if pg["quiz"] else f"part{pg['part']}") + f"-{n}"
        slug, k = base, 2
        while slug in used:
            slug = f"{base}-{k}"
            k += 1
        used.add(slug)
        return slug

    out_pages: list[dict] = []
    counters: dict = {}
    for pg in pages:
        key = "quiz" if pg["quiz"] else pg["part"]
        counters[key] = counters.get(key, 0) + 1
        slug = page_slug(pg, counters[key])
        page = {
            "slug": slug, "title": strip_md(pg["title"]), "title_html": inline(pg["title"]),
            "part": pg["part"], "kind": "quiz" if pg["quiz"] else "text",
        }
        plain_len = len(re.sub(r"\s+", "", strip_md("\n".join(pg["lines"]))))
        page["read_minutes"] = max(1, round(plain_len / 400))
        if pg["quiz"]:
            intro: list[str] = []
            questions: list[dict] = []
            cur_q = None
            qin_code = False
            for ln in pg["lines"]:
                if ln.strip().startswith("```"):
                    qin_code = not qin_code
                h = None if qin_code else split_heading(ln)
                if h and h[0] == 3:
                    cur_q = {"title": h[1], "lines": []}
                    questions.append(cur_q)
                elif cur_q is not None:
                    cur_q["lines"].append(ln)
                else:
                    intro.append(ln)
            page["blocks"] = _no_callouts(parse_blocks(intro))
            page["questions"] = [parse_question(q["title"], q["lines"]) for q in questions]
            scen = []
            for q in page["questions"]:
                if q["scenario"] and q["scenario"] not in scen:
                    scen.append(q["scenario"])
            page["scenarios"] = scen
            page["headings"] = []
        else:
            page["blocks"], page["headings"] = parse_guide_page_blocks(pg["lines"], used)
        parts[pg["part"]]["pages"].append(slug)
        out_pages.append(page)

    return {
        "id": "ccaf-guide",
        "title": strip_md(title),
        "title_html": inline(title),
        "source": GUIDE_SOURCE,
        "generated_from": GUIDE_FILE,
        "preamble": _no_callouts(parse_blocks(preamble)),
        "parts": parts,
        "pages": out_pages,
        "question_count": sum(len(p.get("questions", [])) for p in out_pages),
        "read_minutes": sum(p["read_minutes"] for p in out_pages),
    }

# --------------------------------------------------------------------------- main

def main() -> None:
    courses = [parse_course(m) for m in COURSES]
    # merged glossary: term -> definition (first seen) + courses
    glossary: dict[str, dict] = {}
    for c in courses:
        for g in c.pop("glossary"):
            key = g["term"].lower()
            if key not in glossary:
                glossary[key] = {"term": g["term"], "def": g["def"], "courses": []}
            if c["id"] not in glossary[key]["courses"]:
                glossary[key]["courses"].append(c["id"])
    glossary_list = sorted(glossary.values(), key=lambda g: g["term"].lower())

    concepts = json.loads((ROOT / "build" / "concepts.json").read_text(encoding="utf-8"))

    out_dir = SITE / "data"
    out_dir.mkdir(parents=True, exist_ok=True)
    for stale in out_dir.glob("*.js"):
        stale.unlink()
    total = 0
    for order, c in enumerate(courses):
        c["order"] = order
        payload = json.dumps(c, ensure_ascii=False, separators=(",", ":"))
        (out_dir / f"course-{c['id']}.js").write_text(
            "window.STUDY_COURSES = window.STUDY_COURSES || [];\nwindow.STUDY_COURSES.push(" + payload + ");\n", encoding="utf-8")
        total += len(payload)
    meta = {"generated_from": [m["file"] for m in COURSES], "glossary": glossary_list, **concepts}
    payload = json.dumps(meta, ensure_ascii=False, separators=(",", ":"))
    (out_dir / "meta.js").write_text("window.STUDY_META = " + payload + ";\n", encoding="utf-8")
    total += len(payload)

    # Separate study guide (not merged with the course data)
    guide = parse_guide()
    if guide is not None:
        payload = json.dumps(guide, ensure_ascii=False, separators=(",", ":"))
        (out_dir / "guide.js").write_text("window.STUDY_GUIDE = " + payload + ";\n", encoding="utf-8")
        total += len(payload)
        print(f"guide: {len(guide['pages'])} pages, {guide['question_count']} questions")

    for c in courses:
        print(f"{c['id']:<12} units={len(c['units']):>2} subunits={c['unit_count']:>2} "
              f"tables={sum(1 for g in c['key_groups'] for b in g['blocks'] if b['type']=='table') + sum(1 for u in c['units'] for b in u['blocks'] + [bb for s in u['subunits'] for bb in s['blocks']] if b['type']=='table'):>2} "
              f"callouts={c['callout_count']:>2} read≈{c['read_minutes']}min")
    print(f"glossary terms: {len(glossary_list)}")
    print(f"wrote {len(courses) + 1} files to {out_dir} ({total // 1024} K chars)")


if __name__ == "__main__":
    main()
