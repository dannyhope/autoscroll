# Autoscroll — Design

> Living document. Update whenever visual design changes. Last updated: 2026-08-20.
>
> Companion to [`spec.md`](./spec.md) (behaviour). This file is the source of truth for **how Autoscroll should look**.

---

## Visual intent

Quiet utility. The host page stays the interface. Autoscroll adds a toolbar icon and otherwise stays out of the way — no overlay, no popup, no landing-page chrome on the page.

Start muted: a mid-grey glyph on a transparent toolbar. Do not add a status HUD or branded panel on the page.

---

## Toolbar icon

Two identical downward arrows, side by side. The glyph *is* the icon — no square tile.

| Token | Value |
|-------|--------|
| Colour | Mid-grey `#7B858A` (brand palette) |
| Background | Transparent |
| Padding | ~12% inset so the mark does not touch the canvas edge |
| Metaphor | Scroll down / go to the bottom |

| Size | File |
|------|------|
| 16 / 48 / 128 | `Autoscroll/icon-16.png`, `icon-48.png`, `icon-128.png` (RGBA) |
| SVG source | `icons/icon.svg` |
| Historic OmniGraffle | `Autoscroller icon.graffle` (private folder); promo source `Autoscroll/Autoscroll promo image.graffle` |
| Store listing | 128×128, 24-bit PNG **without alpha**, glyph flattened onto white (`publish/icon-128.png`) |

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

Screenshots show a long web page in a browser with the toolbar icon visible — the real control — not a mock marketing layout. Promo tiles sit the two-arrow glyph on black, with the name **Autoscroll**.

---

## What to avoid

- Inventing an on-page overlay or popup “just for attribution”
- Bright brand colour on the host page
- Painting the toolbar icon onto a coloured square
- Forcing shadcn/Plasmo visuals onto this vanilla extension
- Title-case labels
