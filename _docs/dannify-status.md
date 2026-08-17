# Dannify status — Autoscroll

> Living audit. Regenerated whenever `/dannify` runs. Last updated: 2026-08-17.
>
> What’s already up to spec, and which improvements to apply. Do not treat this file as product truth — that’s `_docs/spec.md` and `_docs/design.md`.
>
> **Detected:** vanilla Chrome extension (toolbar click injects `bookmarklet.js`). Keep this stack — do not migrate to Plasmo.
>
> **Surfaces:** toolbar button + injected page scroller. No popup, options, or side panel.
>
> **Store:** previously listed as Chrome Web Store id `kgkaecolmndcecnchojbndeanmiokofl` (2014; store page now looks unpublished). Manifest is **MV3**.

## Already right

- Local package is loadable: `Autoscroll/manifest.json`, `background.js`, `bookmarklet.js`, icons 16/48/128
- Vanilla stack kept (do not Plasmo-migrate)
- Manifest V3 with `activeTab` + `scripting` (no `tabs`, no host permissions)
- `_docs/spec.md` covers purpose, toolbar click, injected scroller, permissions, and non-goals
- `_docs/design.md` covers toolbar icons and on-page behaviour (no popup)
- README has a purpose section, load-unpacked steps, acknowledgements, feedback, and attribution
- “A Danny Hope product” → https://dannyhope.co.uk in the README footer (and privacy policy)
- Feedback link to danny.hope@gmail.com
- `publish/` pack (`index.html`, listing copy, zip, screenshots, promo, privacy policy)
- British English in listing copy; `activeTab` and `scripting` justified (MV2 `tabs` / hosts dropped)
- Bombay `projects.json` lists `autoscroll`
- OmniGraffle sources exist (`Autoscroller icon.graffle` in the private folder; `Autoscroll promo image.graffle` in the package)
- Sitemap skipped (not a public website)
- Dev-port skipped (no local server)
- Prototype Panels skipped (not a web app)

## Improvements

### Should

- Add `.in/` inbox (optional `.in/README.md`)
- Add `.gitignore` including `_vibing/` and `.DS_Store`
- Create `_vibing/`
- Add `autoscroll.code-workspace`
- Add `CLAUDE.md` (dev guidance, load unpacked, preferred stack kept vanilla)
- Add usability-test scaffold (`_docs/usability-tasks.json` + `usability-test.html`)

### Nice

- Offer a Notion vs in-repo documentation split (product truth stays in `_docs/`)
