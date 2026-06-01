# Maintaining this bundle

This is the **published mirror** of HTML visuals from
`cybersecurity/docs/flipper-zero/visuals/` in the source workspace. The source
is canonical; this bundle is a derivative.

Live site: <https://n0xide.github.io/flipper-zero-visuals/>

## Direction
Edit in the source workspace's `visuals/` folder first, then mirror the
change into this bundle. Don't edit the bundle's HTML by hand without
matching the change upstream — it desyncs.

## Outbound .md hrefs are stripped here
The source visuals link back to the curriculum markdown (`../02-sub-ghz.md`,
`../README.md`, `../../../CONTEXT.md`, etc.). Those markdowns are not in this
bundle. The publish process rewrites every `<a href="…md">filename</a>` into
a dim non-link span:

```html
<span style="opacity:0.55;cursor:default" title="Source lives in the private workspace">filename.md</span>
```

When you re-mirror a visual from the source, re-run the same rewrite:

```bash
sed -i -E 's|<a href="[^"]*\.md">(.*)</a>|<span style="opacity:0.55;cursor:default" title="Source lives in the private workspace">\1</span>|g' *.html
```

## Before pushing — integrity checklist

CI runs both checks automatically on every push to `main` (see
`.github/workflows/ci.yml`), but you can replicate locally:

```bash
# 1. Internal anchor + relative-link integrity (handles JS-rendered
#    Phase 8 deep links and template-literal false positives).
python .github/scripts/check_anchors.py

# 2. No .md hrefs survived the mirror.
grep -rE 'href="[^"]+\.md"' . --include='*.html' | wc -l
# expect 0

# 3. HTML well-formedness.
npx --yes htmlhint@1 --config .github/htmlhint.json *.html
```

All three should pass before `git push`. CI also runs `lychee` for
external links, non-blocking.

## og:image / twitter:card meta tags

Every HTML page carries a `<!-- og:meta-injected -->` block before
`</head>` with per-page title + description, social card image
(`og-image.svg`), and canonical URL. The block is managed by:

```
<workspace-root>/scripts/inject-flipper-meta.py
```

Run from the workspace root:

```bash
python scripts/inject-flipper-meta.py \
  cybersecurity/docs/flipper-zero/visuals \
  cybersecurity/docs/flipper-zero/dist
```

It's idempotent — re-running cleans the prior block before writing
the new one. To change a page's title/description, edit the `PAGES`
dict in the script and re-run.

## Adding a new phase visual

1. Add the source HTML in `cybersecurity/docs/flipper-zero/visuals/`.
2. Copy the file into this bundle.
3. Strip `.md` hrefs (sed snippet above).
4. Update `index.html`'s phase grid + navigation to include the new page.
5. Update `README.md`'s "What's inside" table.
6. Run integrity checks → `git add -A; git commit; git push`.

Pages rebuilds in ~30s.

## Style is local

This bundle's look-and-feel (cyberpunk / amber / Flipper-Zero-inspired)
is defined inline per file. Don't borrow styles from other bundles
(e.g. mechatronics-visuals' dark monospace) — Flipper has its own
identity.

## Source workspace

```
<workspace-root>/cybersecurity/docs/flipper-zero/visuals/
<workspace-root>/cybersecurity/docs/flipper-zero/*.md  (curriculum markdowns)
<workspace-root>/cybersecurity/CONTEXT.md
```

Full publish pattern (round-trip rules, repo naming, integrity checks):
`<workspace-root>/docs/publish-pattern.md`.
