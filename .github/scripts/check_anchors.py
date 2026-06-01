#!/usr/bin/env python3
"""
Verify internal anchor integrity across the published bundle.

For every <a href="..."> in every HTML file, check that:
  - Relative file refs (e.g. "phase-2-subghz.html") point to a file that exists
  - In-page anchors (e.g. "#foo") match an id="foo" in the same file
  - Cross-page anchors (e.g. "phase-8-defense.html#bar") match an id="bar"
    in that file, OR are known JS-rendered deep links into the Phase 8
    defense matrix (handled by the page's own script — listed in
    PHASE8_DYNAMIC_PREFIXES).

External URLs are NOT checked here — lychee handles those in CI.

Exits non-zero with a list of broken refs.
"""
from __future__ import annotations
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# JS-rendered Phase 8 deep links — the matrix script reads location.hash
# at runtime and resolves these to rows. They are not static anchors,
# so the integrity check must allow them.
PHASE8_DYNAMIC_PREFIXES = ("a=", "phase=", "sort=")
PHASE8_FILE = "phase-8-defense.html"

HREF_RE = re.compile(r'href=["\']([^"\']+)["\']')
ID_RE   = re.compile(r'id=["\']([a-zA-Z0-9_\-:.]+)["\']')

# JS template-literal false positives — skip any href that contains `${...}`
JS_TEMPLATE_RE = re.compile(r'\$\{[^}]+\}')

def collect_files() -> list[str]:
    return sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))

def main() -> int:
    files = collect_files()
    all_ids: dict[str, set[str]] = {}
    for f in files:
        text = open(os.path.join(ROOT, f), encoding="utf-8").read()
        all_ids[f] = set(ID_RE.findall(text))

    broken: list[tuple[str, str, str]] = []

    for f in files:
        text = open(os.path.join(ROOT, f), encoding="utf-8").read()
        for href in HREF_RE.findall(text):
            # Skip external URLs
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            # Skip empty / placeholders
            if not href or href == "#":
                continue
            # Skip JS template literals captured by the regex (e.g. ${href}, #L-${L})
            if JS_TEMPLATE_RE.search(href):
                continue

            # In-page anchor
            if href.startswith("#"):
                anchor = href.lstrip("#")
                if anchor not in all_ids[f]:
                    broken.append((f, href, "in-page anchor missing"))
                continue

            # Split file + anchor
            if "#" in href:
                path, anchor = href.split("#", 1)
            else:
                path, anchor = href, None

            if path and not os.path.exists(os.path.join(ROOT, path)):
                broken.append((f, href, "target file does not exist"))
                continue

            if anchor and path.endswith(".html"):
                # Allow JS-rendered Phase 8 deep links
                if path == PHASE8_FILE and any(
                    anchor.startswith(p) for p in PHASE8_DYNAMIC_PREFIXES
                ):
                    continue
                # Allow JS template literal anchors (${id} captured by the regex)
                if JS_TEMPLATE_RE.search(anchor):
                    continue
                if anchor not in all_ids[path]:
                    broken.append((f, href, f"anchor #{anchor} missing in {path}"))

    if broken:
        print(f"::error::Found {len(broken)} broken internal link(s):")
        for src, href, reason in broken:
            print(f"  {src} -> {href}    [{reason}]")
        return 1

    print(f"OK: zero broken internal links across {len(files)} HTML file(s).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
