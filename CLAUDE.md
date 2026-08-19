# CLAUDE.md

Guidance for working on Autoscroll.

## What this is

Vanilla Manifest V3 Chrome extension. Toolbar click injects `bookmarklet.js` into the active tab so the page scrolls toward the bottom. No popup, options page, or side panel.

**Keep this stack.** Do not migrate to Plasmo.

## Load unpacked

1. Open `chrome://extensions/`
2. Turn on **Developer mode**
3. **Load unpacked** → select the `Autoscroll` folder (the one that contains `manifest.json`)
4. Open a long web page and click the Autoscroll icon

Reload the extension on `chrome://extensions` after changing the scripts.

## Layout

| Path | Role |
|------|------|
| `Autoscroll/` | Loadable package (`manifest.json`, `background.js`, `bookmarklet.js`, icons) |
| `_docs/spec.md` | How it should work |
| `_docs/design.md` | How it should look |
| `privacy-policy.html` | Store privacy policy (source) |
| `publish/` | Chrome Web Store pack (`index.html`, listing copy, zip, assets) |

## Documentation

**In-repo is the source of truth** for product behaviour and look: `_docs/spec.md` and `_docs/design.md`. If code, README, or store copy disagree, align those to the docs (or update the docs first if the product decision has changed).

**Notion** (if used) is for working notes, research, and history — not product truth. Do not let a Notion page override spec or design.

## Privacy policy hosting

The Chrome Web Store privacy-policy URL is https://dannyhope.co.uk/autoscroll/. The page lives in the dannyhope.co.uk repo as `autoscroll/index.html`. When you change `privacy-policy.html` here, copy it there too. It is not live until that site is deployed.

## Rebuild the upload zip

After changing the package:

```bash
cd Autoscroll
zip -r ../publish/autoscroll.zip \
  manifest.json background.js bookmarklet.js \
  icon-16.png icon-48.png icon-128.png \
  -x "*.DS_Store"
```

Do not auto-upload to the Chrome Web Store.

## Copy

British English in user-facing words (listing, tooltip, any future UI).

## What this repo does not have

No local web server, so no `.dev-port`. Not a public website of its own (privacy policy is hosted on dannyhope.co.uk).
