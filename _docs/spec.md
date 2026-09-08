# Autoscroll — Product Spec

> Living document. Update whenever behaviour changes. Last updated: 2026-09-03.
>
> **This file is the source of truth for how Autoscroll should work.** If code, README, or store listing copy disagree with this spec, update them to match this document.

---

## Purpose

Autoscroll is a browser extension for Chrome, Firefox, and Safari on macOS that scrolls the current page toward the bottom so you can read or scan a long page without holding the scroll wheel. Click the toolbar icon to start; scroll up or click again to stop. Cross-browser support is only considered verified for a browser/package combination after the manual real-browser matrix in [`cross-browser-test-matrix.md`](./cross-browser-test-matrix.md) has been completed.

---

## Surfaces

| Surface | Role |
|---------|------|
| Toolbar button (`action`) | The only control. Click starts or stops scrolling on the active tab. No popup. |
| Injected scroller (`bookmarklet.js`) | Runs in the page after a toolbar click. Moves the viewport down until stopped. |
| Safari App Extension toolbar item | The Safari equivalent of the toolbar button; it sends a message to the page script. |

There is no options page, side panel, or on-page overlay.

---

## Core behaviour

### Start and stop

- **Click the toolbar icon** on a normal web page:
  - If the page is not autoscrolling, start.
  - If it is already autoscrolling, stop.
- **Scroll up** (mouse wheel or trackpad) while autoscrolling: stop. Downward scrolling does not stop it.
- Navigating to a new page ends the script with that page; a new click is required.

### Motion

- While running, jump down **1000px every 100ms** (`scrollTo` from the current `pageYOffset`).
- No speed control, pause, or reverse in this version.

### Where it runs

- Injected only into the tab whose toolbar icon was clicked (`activeTab` + `scripting`).
- Does not run automatically on every page.
- Restricted browser pages (`chrome://`, `about:`, the Web Store, and similar) cannot be scripted; the click does nothing there.

### Architecture

- Built with [WXT](https://wxt.dev/) and TypeScript for cross-browser development
- Single source tree in `src/entrypoints/` generates both Chrome and Firefox packages
- Uses `browser.*` WebExtension APIs (via WXT's polyfill) for cross-browser compatibility
- Background script (`background.ts`) listens for toolbar clicks and injects the scroller
- Scroller script (`scroller.js`) runs in the page context and handles the scroll behavior

### Firefox support

- Built as Manifest V2 for Firefox (WXT default for maximum compatibility)
- Supported floor: Firefox 128 or newer, including Firefox ESR releases based on 128 or newer
- Firefox uses native `browser.*` APIs; the page-scoped interval remains in the injected script
- Build with `npm run build:firefox`; output in `.output/firefox-mv2/`
- Firefox Add-ons signing and submission are publishing work, not performed by this repository
- Manual cross-browser evidence is recorded in [`cross-browser-test-matrix.md`](./cross-browser-test-matrix.md)

### Privacy

- No account, analytics, advertising, or developer backend.
- Nothing is stored in `chrome.storage`.
- The scroller does not read page content for any purpose other than scrolling the window.
- See `privacy-policy.html`.

---

## Permissions

| Permission | Why |
|------------|-----|
| `activeTab` | Access only the tab the user just clicked the icon on. |
| `scripting` | Inject the scroller script into that tab. |

Chrome uses Manifest V3 (`.output/chrome-mv3/`). Firefox uses Manifest V2 (`.output/firefox-mv2/`) for maximum compatibility. Both require only `activeTab` + `scripting`; no broad host permissions needed. Package version **0.4.0**.

---

### Safari support

- macOS Safari only, with a macOS 13.0 deployment floor and the current Xcode SDK.
- The local development package is an Xcode containing app plus Safari App Extension. It is not signed for Developer ID or the Mac App Store.
- Safari website access must be granted by the user. Safari-restricted pages and non-HTML viewers may reject injection.
- Safari packaging is reproducible through `scripts/package-safari.sh` once `Safari/AutoscrollSafari.xcodeproj` has been created in Xcode. The script builds a Debug app with signing disabled and archives it to `publish/autoscroll-safari-development.zip`; it never uploads.
- Safari runtime parity and installation are not currently verified; the repository does not yet contain the Xcode project required to build the local package.

## Non-goals

- Configurable speed, pause, or reverse.
- A popup, options page, or on-page HUD.
- Windows-style middle-click autoscroll.
- Starting on every tab without a click.
- Guaranteed behaviour on PDFs or other non-HTML viewers.

---

## Local development

Built with WXT; run `npm run dev` (Chrome) or `npm run dev:firefox` (Firefox) for live reload during development. Load unpacked from `.output/chrome-mv3/` or `.output/firefox-mv2/` respectively.

There is no local HTTP server. `.dev-port` and a Bombay proxy route are not applicable. `.local-domain` is retained as the stable project hostname for shared tooling.

## Related docs

| Doc | Role |
|-----|------|
| [`design.md`](./design.md) | How it should look |
| [`../publish/LISTING.md`](../publish/LISTING.md) | Chrome Web Store copy |
