"""Build the "How humans and agents talk" site into static/humans-and-agents/.

Each page in src/pages/<slug>.html starts with a metadata comment:

    <!--
    title: Page title
    description: One sentence for search and link previews.
    -->

Links inside pages use {{root}} for the site root, so every page works
at any depth. Run: python3 build.py
"""

import html
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
OUT = HERE.parent.parent / "static" / "humans-and-agents"
SITE_URL = "https://sptr11.github.io/humans-and-agents/"
SITE_NAME = "How humans and agents talk"
AS_OF = "Evidence current to 18 October 2026"

# Reading order. "index" is the home page.
ORDER = [
    "index",
    "inside",
    "corresponding",
    "systems",
    "handoffs",
    "approvals",
    "negotiating",
    "protocols",
    "history",
    "actors",
    "missing",
    "method",
    "references",
]

NAV = [
    ("inside", "Inside a company"),
    ("across", "Across companies"),
    ("protocols", "Protocols"),
    ("history", "History"),
    ("actors", "Actors"),
    ("missing", "What's missing"),
    ("method", "Method"),
]

FONTS = (
    "https://fonts.googleapis.com/css2?"
    "family=IBM+Plex+Mono:wght@400;500"
    "&family=Instrument+Serif"
    "&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;0,7..72,700;1,7..72,400"
    "&display=swap"
)


def parse(path):
    text = path.read_text()
    m = re.match(r"\s*<!--(.*?)-->\s*", text, re.S)
    if not m:
        raise SystemExit(f"{path.name}: missing metadata comment")
    meta = {}
    for line in m.group(1).strip().splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    for key in ("title", "description"):
        if key not in meta:
            raise SystemExit(f"{path.name}: missing {key}")
    return meta, text[m.end():]


def href(root, slug):
    if slug == "across":
        return f"{root}#across"
    return root if slug == "index" else f"{root}{slug}/"


def render(slug, meta, body, pages):
    root = "./" if slug == "index" else "../"
    title = meta["title"] if slug == "index" else f"{meta['title']} · {SITE_NAME}"
    url = SITE_URL if slug == "index" else f"{SITE_URL}{slug}/"

    nav = []
    for target, label in NAV:
        current = ' aria-current="page"' if target == slug else ""
        nav.append(f'<a href="{href(root, target)}"{current}>{label}</a>')

    i = ORDER.index(slug)
    pager = []
    if i > 0:
        prev = ORDER[i - 1]
        pager.append(
            f'<a class="prev" href="{href(root, prev)}"><small>Previous</small>'
            f"<span>{html.escape(pages[prev]['title'])}</span></a>"
        )
    if i < len(ORDER) - 1:
        nxt = ORDER[i + 1]
        pager.append(
            f'<a class="next" href="{href(root, nxt)}"><small>Next</small>'
            f"<span>{html.escape(pages[nxt]['title'])}</span></a>"
        )

    body = body.replace("{{root}}", root)
    desc = html.escape(meta["description"], quote=True)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{html.escape(meta['title'], quote=True)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta name="author" content="Sumit">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
<header class="masthead">
  <div class="masthead-inner">
    <a class="brand" href="{root}">{SITE_NAME}</a>
    <nav class="nav" aria-label="Sections">{''.join(nav)}</nav>
  </div>
</header>
<main>
{body.strip()}
<nav class="pager" aria-label="Reading order">{''.join(pager)}</nav>
<footer class="colophon">
  <p>{AS_OF}. Written by <a href="https://sptr11.github.io/">Sumit</a>. Figures link to their sources where a public source exists; company-reported and second-hand figures are marked. Full list on the <a href="{root}references/">references</a> page.</p>
</footer>
</main>
</body>
</html>
"""


def main():
    pages = {}
    bodies = {}
    for slug in ORDER:
        meta, body = parse(SRC / "pages" / f"{slug}.html")
        pages[slug] = meta
        bodies[slug] = body

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(SRC / "assets", OUT / "assets")

    for slug in ORDER:
        dest = OUT / "index.html" if slug == "index" else OUT / slug / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(slug, pages[slug], bodies[slug], pages))
    print(f"Built {len(ORDER)} pages into {OUT}")


if __name__ == "__main__":
    main()
