# Autoscroll — Design

> Living document. Update whenever visual design changes. Last updated: 2026-08-17.
>
> Companion to [`spec.md`](./spec.md) (behaviour). This file is the source of truth for **how Autoscroll should look**.

---

## Visual intent

Quiet utility. The host page stays the interface. Autoscroll adds a toolbar icon and otherwise stays out of the way — no overlay, no popup, no landing-page chrome on the page.

Start muted: black toolbar icon, grey arrows. Do not add a status HUD or branded panel on the page.

---

## Toolbar icon

Two identical downward arrows, side by side, on a black square.

| Token | Value |
|-------|--------|
| Background | Black (`#000`) |
| Arrows | Dark grey, flat, no outline |
| Metaphor | Scroll down / go to the bottom |

| Size | File |
|------|------|
| 16 / 48 / 128 | `Autoscroll/icon-16.png`, `icon-48.png`, `icon-128.png` |
| Source | `Autoscroller icon.graffle` (private folder); promo source `Autoscroll/Autoscroll promo image.graffle` |
| Store listing | 128×128, 24-bit PNG **without alpha** (`publish/icon-128.png`) |

Toolbar tooltip: **Autoscroll**.

---

## On-page

There is **no** injected UI. No translucent panel, no “scrolling…” badge, no speed readout.

Motion is the only feedback: the page jumps downward until the user scrolls up or clicks the icon again.

If a future version needs confirmation, keep it brief and functional (a short fade), not decorative.

---

## Copy

British English in any user-facing words (listing, tooltip, future UI). Sentence case. No title-case button labels if controls are added later.

---

## Store listing visuals

Screenshots show a long web page in a browser with the toolbar icon visible — the real control — not a mock marketing layout. Promo tiles reuse the two-arrow mark on black, with the name **Autoscroll**.

---

## What to avoid

- Inventing an on-page overlay or popup “just for attribution”
- Bright brand colour on the host page
- Forcing shadcn/Plasmo visuals onto this vanilla extension
- Title-case labels
