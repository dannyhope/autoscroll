# Autoscroll

Browser extension for Chrome and Firefox that scrolls the current page toward the bottom. Click the toolbar icon to start; scroll up or click again to stop.

**Install from the [Chrome Web Store](https://dannyhope.co.uk/autoscroll/store/)** · [Product page](https://dannyhope.co.uk/autoscroll/) · [Source](https://dannyhope.co.uk/autoscroll/source/)

## Usage

- **Click** the toolbar icon to start scrolling down.
- **Click again** to stop.
- **Scroll up** (wheel or trackpad) to stop.

It only affects the tab you click on. It does not run on `chrome://` pages or the Chrome Web Store.

## Development

This extension is built with [WXT](https://wxt.dev/) and TypeScript.

### First-time setup

```bash
npm install
```

### Development mode (live reload)

**Chrome:**
```bash
npm run dev
```

**Firefox:**
```bash
npm run dev:firefox
```

Then load the extension:
- **Chrome:** Open `chrome://extensions/`, enable Developer mode, and Load unpacked → `.output/chrome-mv3`
- **Firefox:** Open `about:debugging`, This Firefox, Load Temporary Add-on → `.output/firefox-mv2/manifest.json`

### Production build

**Chrome:**
```bash
npm run build
```

**Firefox:**
```bash
npm run build:firefox
```

Output directories:
- Chrome: `.output/chrome-mv3/` (Manifest V3)
- Firefox: `.output/firefox-mv2/` (Manifest V2, supports Firefox 128+)

### Package for distribution

```bash
npm run zip          # Chrome
npm run zip:firefox  # Firefox
```

Creates zip files in `.output/` ready for store submission.

## Chrome Web Store publish

Open [`publish/index.html`](publish/index.html) in a browser — checklist, copy-paste fields, images, and the upload zip.

Live listing: https://dannyhope.co.uk/autoscroll/store/ (hop). Operator URL: `chromewebstore.google.com/detail/autoscroll/kgkaecolmndcecnchojbndeanmiokofl`.

## Docs

- [`_docs/spec.md`](_docs/spec.md) — how it should work
- [`_docs/design.md`](_docs/design.md) — how it should look
- Public page (install + privacy): https://dannyhope.co.uk/autoscroll/

## Acknowledgements

Thanks @rem for the original script which was used to make a bookmarklet which was used to make the browser extension.

Thanks to Peter Legierski for the [Convert bookmarklet to Chrome extension tool](https://dannyhope.co.uk/bookmarklet-to-extension/).

## Feedback

[Feedback](https://dannyhope.co.uk/feedback)

---

[A Danny Hope product](https://dannyhope.co.uk)
