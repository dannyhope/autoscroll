# Publish in ~30 minutes — your checklist

**Use the interactive guide:** open [`publish/index.html`](index.html) in a browser — copy buttons, image downloads, and the zip are all there.

Markdown below is a backup. The HTML page is what you should use.

## Already done
- Manifest V3 package version **0.3** (`activeTab` + `scripting`; no `tabs`, no host permissions). Chrome’s “update to Manifest V3” email is about the **dashboard listing**, not this folder.
- Extension icons (16, 48, 128)
- Privacy policy HTML (`privacy-policy.html` at project root) — host at https://dannyhope.co.uk/autoscroll/
- Store listing copy (`publish/LISTING.md`)
- Interactive guide (`publish/index.html`)
- Upload zip (`publish/autoscroll.zip`)
- Promo tile 440×280 and marquee 1400×560
- Screenshots in `publish/`

---

## Step 1 — Developer account (already registered)

Your account is active — skip the $5 fee.

Previous listing id (2014): `kgkaecolmndcecnchojbndeanmiokofl`. If Chrome emailed an MV3 warning, that item is still in the dashboard — **upload this zip there**. Remaining Manifest V2 listings leave the store on **31 August 2026**. Use **New item** only if that listing is gone.

## Step 2 — Privacy policy

Host `privacy-policy.html` at:

```
https://dannyhope.co.uk/autoscroll/
```

Paste that URL in the dashboard.

## Step 3 — Screenshots (in `publish/`)

| File | Shows |
|------|--------|
| `publish/screenshot.png` | Long page + toolbar icon (primary) |
| `publish/screenshot-further.png` | Further down the same page |

## Step 4 — Upload
1. [Developer Dashboard](https://chrome.google.com/webstore/devconsole) → **New item** (or the old listing if it still exists)
2. Upload **`publish/autoscroll.zip`**
3. Paste fields from **`publish/index.html`** (or LISTING.md)
4. Upload **`publish/icon-128.png`**
5. Upload **screenshot(s)**
6. Upload **promo tile** (`publish/promo-tile-440x280.png`) if the form asks
7. **Privacy policy URL** — hosted URL from Step 2
8. **Single purpose** — from the guide
9. Category: Productivity group → **Tools**
10. Visibility: **Unlisted** (link only)

## Step 5 — Submit
1. Complete **Privacy practices** (answers in the guide)
2. Fill **permission justifications** — `activeTab` and `scripting` only
3. Click **Submit for review**

Do **not** auto-upload from this repo.

---

## Quick test before upload
1. `chrome://extensions` → Load unpacked → `Autoscroll/` folder
2. Open a long page → click the icon → page should jump downward
3. Scroll up → it should stop
4. Click again → it should start again

## Re-build zip after changes
```bash
cd "/Users/dannyhope/Dropbox/Autoscroll (private)/Repos/autoscroll/Autoscroll"
zip -r ../publish/autoscroll.zip \
  manifest.json background.js bookmarklet.js \
  icon-16.png icon-48.png icon-128.png \
  -x "*.DS_Store"
```
