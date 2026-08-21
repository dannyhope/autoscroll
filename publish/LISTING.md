# Chrome Web Store listing — paste these fields

Aligned with the **Store listing** form in the Developer Dashboard.
British English throughout. Visibility starts **Unlisted**.

## Title from package
*(from `manifest.json` → `name` — not edited in the listing form)*

Autoscroll

## Summary from package
*(from `manifest.json` → `description`)*

Scroll to the bottom of the page. Click the toolbar icon; scroll up to stop.

## Description
*(paste into Description — max 16,000 characters)*

Autoscroll scrolls the current page toward the bottom so you can read or scan a long page without holding the wheel.

**How to use it**
- Click the Autoscroll icon in the toolbar to start
- Click again to stop
- Scroll up (mouse wheel or trackpad) to stop

It only affects the tab you click on. There is no popup and no overlay on the page — the page stays as it is.

**Privacy**
No account required. No analytics. No data sent to the developer. Nothing is stored in Chrome storage.

**Not for**
Restricted Chrome pages (such as `chrome://` or the Chrome Web Store) cannot be scripted, so the icon does nothing there.

## Category
**Tools** (under the Productivity *group* — Productivity itself is not selectable)

Other options in that group: Education, Functionality & UI, Household, Privacy & Security, Workflow & Planning.

## Language
English (United Kingdom) — British English spelling in all listing copy. If the dropdown only has “English”, use that and keep British spelling.

## Graphic assets
| Asset | File | Spec |
|-------|------|------|
| Store icon | `icon-128.png` | 128×128, 24-bit PNG no alpha |
| Screenshots (up to 5) | `screenshot.png`, `screenshot-further.png` | 1280×800, 24-bit PNG no alpha |
| Small promo tile | `promo-tile-440x280.png` | 440×280 |
| Marquee promo tile | `marquee-promo-tile-1400x560.png` | 1400×560 |
| Promo video | — | Skip |

## Additional fields
| Field | Value |
|-------|--------|
| Official URL | None (or dannyhope.co.uk if verified in Search Console) |
| Homepage URL | https://dannyhope.co.uk/autoscroll/ |
| Support URL | https://dannyhope.co.uk/autoscroll/ |
| Mature content | No |
| Visibility | **Unlisted** (link only — not Public until you choose) |
| Item support | On |

## Single purpose
*(Privacy / distribution tab — not Store listing)*

Scroll the current web page toward the bottom when the user clicks the toolbar icon.

## Permission justifications (dashboard)

Manifest V2 asked for `tabs` and `http://*/*` / `https://*/*`. Those are **not** in this MV3 package. Justify only what Chrome lists:

**activeTab**
Used only when you click the toolbar icon, so the extension can run on that one tab. It does not have standing access to other tabs or your browsing history.

**scripting**
Injects the scroller script into the tab you just clicked so the page can move toward the bottom. The script does not send page content to the developer.

## Privacy practices (dashboard questionnaire — typical answers)
- **Collect personal data?** No (developer does not collect)
- **Data used for:** Functionality only (scrolling the current tab in the browser)
- **Data sold?** No
- **Privacy policy URL:** https://dannyhope.co.uk/autoscroll/

Hosted at that URL (`dannyhope.co.uk/autoscroll/index.html`).

## Support email
danny.hope@gmail.com
