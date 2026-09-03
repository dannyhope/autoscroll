# Autoscroll

Browser extension for Chrome and Firefox that scrolls the current page toward the bottom. Click the toolbar icon to start; scroll up or click again to stop.

**Install from the [Chrome Web Store](https://dannyhope.co.uk/autoscroll/store/)** · [Product page](https://dannyhope.co.uk/autoscroll/) · [Source](https://dannyhope.co.uk/autoscroll/source/)

## Usage

- **Click** the toolbar icon to start scrolling down.
- **Click again** to stop.
- **Scroll up** (wheel or trackpad) to stop.

It only affects the tab you click on. It does not run on `chrome://` pages or the Chrome Web Store.

## Load unpacked (local)

1. Open `chrome://extensions/`
2. Turn on **Developer mode**
3. **Load unpacked** → select the `Autoscroll` folder (the one that contains `manifest.json`)
4. Open a long web page and click the Autoscroll icon in the toolbar

Reload the extension on `chrome://extensions` after you change the scripts.

## Firefox (local development)

The Firefox package is a separate Manifest V3 package. It supports Firefox 128 and newer, including ESR releases based on 128 or newer.

Run `./scripts/package-firefox.sh` to create the unsigned `publish/autoscroll-firefox.xpi`. In Firefox, open `about:debugging`, choose **This Firefox**, select **Load Temporary Add-on**, and choose the package's `Firefox/manifest.json` (or the generated XPI). Temporary add-ons are removed when Firefox restarts.

Firefox Add-ons signing and submission are not automated here.

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
