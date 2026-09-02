# Autoscroll — Product Spec

> Living document. Update whenever behaviour changes. Last updated: 2026-08-20.
>
> **This file is the source of truth for how Autoscroll should work.** If code, README, or store listing copy disagree with this spec, update them to match this document.

---

## Purpose

Autoscroll is a Chrome extension that scrolls the current page toward the bottom so you can read or scan a long page without holding the scroll wheel. Click the toolbar icon to start; scroll up or click again to stop.

---

## Surfaces

| Surface | Role |
|---------|------|
| Toolbar button (`action`) | The only control. Click starts or stops scrolling on the active tab. No popup. |
| Injected scroller (`bookmarklet.js`) | Runs in the page after a toolbar click. Moves the viewport down until stopped. |

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
- Restricted Chrome pages (`chrome://`, the Chrome Web Store, and similar) cannot be scripted; the click does nothing there.

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
| `scripting` | Inject `bookmarklet.js` into that tab. |

Manifest V2 used `tabs` plus `http://*/*` and `https://*/*`. Those are **not** in the MV3 package: the toolbar click is enough. Package version **0.3**. The loadable files are Manifest V3; if Chrome still warns, the **published** listing has not been replaced yet.

---

## Non-goals

- Configurable speed, pause, or reverse.
- A popup, options page, or on-page HUD.
- Windows-style middle-click autoscroll.
- Starting on every tab without a click.
- Firefox or Safari ports.
- Guaranteed behaviour on PDFs or other non-HTML viewers.

---

## Local development

Autoscroll is a load-unpacked Chrome extension and does not run a local HTTP
server. Consequently `.dev-port`, a live-reload workflow, and a Bombay proxy
route are not applicable. `.local-domain` is retained as the stable project
hostname for shared tooling; `scripts/ensure-local-domain.sh` can maintain its
loopback hosts entry, but there is no page for `http://autoscroll.local/` to
serve.

## Related docs

| Doc | Role |
|-----|------|
| [`design.md`](./design.md) | How it should look |
| [`../publish/LISTING.md`](../publish/LISTING.md) | Chrome Web Store copy |
