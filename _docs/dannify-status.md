# Dannify status — Autoscroll

> Living audit. Regenerated whenever `/dannify` runs. Last updated: 2026-08-19.
>
> What still needs doing, then what’s already up to spec. Do not treat this file as product truth — that’s `_docs/spec.md` and `_docs/design.md`.
>
> **Detected:** vanilla Chrome extension (toolbar click injects `bookmarklet.js`). Keep this stack — do not migrate to Plasmo.
>
> **Surfaces:** toolbar button + injected page scroller. No popup, options, or side panel.
>
> **Store:** previously listed as Chrome Web Store id `kgkaecolmndcecnchojbndeanmiokofl` (2014; store page now looks unpublished). Manifest is **MV3**.

## Improvements

None — clean bill of health.

## Already right

- Public feedback hrefs (README, privacy policy, store Support URL) go via https://dannyhope.co.uk/feedback
- `.in/` inbox exists
- `.gitignore` includes `_vibing/` and `.DS_Store`
- `_vibing/` exists (git-ignored)
- `autoscroll.code-workspace` with a Peacock colour
- `CLAUDE.md` covers load unpacked, vanilla stack, and docs split
- Usability-test scaffold (`_docs/usability-tasks.json` + `usability-test.html`)
- Toolbar icons are a mid-grey glyph (`#7B858A`) on transparent; `_docs/design.md` matches
- Privacy policy hosted at https://dannyhope.co.uk/autoscroll/ (page in the website repo; not live until that site is deployed)
- Notion vs in-repo split documented in `CLAUDE.md` (product truth stays in `_docs/`)
- Local package is loadable: `Autoscroll/manifest.json`, `background.js`, `bookmarklet.js`, icons 16/48/128
- Vanilla stack kept (do not Plasmo-migrate)
- Manifest V3 with `activeTab` + `scripting`
- `_docs/spec.md` covers purpose, toolbar click, injected scroller, permissions, and non-goals
- README has a purpose section, then load-unpacked steps (acknowledgements kept)
- Attribution “A Danny Hope product” → https://dannyhope.co.uk in the README footer and privacy policy (kind is **product**; no popup to put a footer in)
- `publish/` pack (`index.html`, listing copy, zip, screenshots, promo, privacy policy)
- British English in listing copy; `activeTab` and `scripting` justified
- Bombay `projects.json` lists `autoscroll`
- OmniGraffle sources exist (`Autoscroller icon.graffle` in the private folder; `Autoscroll promo image.graffle` in the package)
- Sitemap skipped (not a public website)
- Dev-port skipped (no local server)
- Prototype Panels skipped (not a web app)
