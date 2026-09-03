# Port Autoscroll to Firefox
**Readiness:** auto-refined
**Roadmap:** now
**Parent:** `port-extension-to-safari-and-firefox.md`

Create a Firefox WebExtension that preserves the toolbar-click start/stop behaviour and upward-wheel stop behaviour of the Chrome implementation. Resolve Manifest/API and permission differences, package a reproducible development/release add-on, and document the supported Firefox version and publishing prerequisites.

**Done when:** The Firefox package installs in a supported Firefox version, passes the agreed behaviour matrix, and has submission-ready Mozilla Add-ons metadata.

## Auto-investigation
**Investigated:** 2026-09-03

### Findings
- The current implementation is a small Chrome Manifest V3 package in `Autoscroll/`: `manifest.json`, `background.js`, `bookmarklet.js`, and PNG icons.
- `background.js` uses `chrome.action.onClicked` and `chrome.scripting.executeScript` with `activeTab` and `scripting`; Firefox supports WebExtensions but the manifest/background API shape and minimum supported version must be explicitly chosen and tested.
- `bookmarklet.js` is page-scoped and self-contained: it toggles a `setInterval` that calls `scrollTo(0, pageYOffset + 1000)` every 100ms and stops on upward wheel input. It has no overlay or stored state, so the Firefox port should preserve this behaviour.
- The repository has no Firefox package, automated browser test harness, or Mozilla metadata yet. The parent task already separates cross-browser testing and publishing, so this task should focus on the Firefox source/package and its browser compatibility decisions.
- The product spec currently lists Firefox and Safari as non-goals; supporting Firefox requires changing that product statement and documenting the supported Firefox version and any Firefox-specific restrictions.

### Scope
- Add a Firefox-specific WebExtension package or a clearly reproducible shared package strategy, including manifest, background injection code, shared/page script, icons, and package build instructions.
- Verify toolbar click start/stop, upward-wheel stop, downward-wheel non-stop, navigation reset, and safe failure on restricted pages against the chosen Firefox release/support floor.
- Add Mozilla Add-ons metadata needed for submission; detailed submission/signing execution belongs to the publishing child task.
- Estimated complexity: medium.
- This is not cleanly reducible to smaller implementation children without duplicating the package and compatibility decisions; testing and publishing remain separate sibling tasks.

### Proposed implementation
1. Choose and record the Firefox support floor and whether the package is Manifest V2 or Manifest V3, based on the APIs and release targets that must be supported.
2. Create the Firefox package layout and manifest, reusing `bookmarklet.js` if page-world behaviour is compatible and adapting the toolbar click/injection path where Firefox requires it.
3. Keep permissions least-privilege (`activeTab` plus the injection permission required by the selected Firefox manifest/API), and ensure restricted pages reject cleanly without breaking the background listener.
4. Add a reproducible unsigned development `.zip`/`.xpi` packaging command and Mozilla-facing metadata inputs, without uploading or signing automatically.
5. Run the separate cross-browser matrix, then update the spec/design or release docs with the tested Firefox version, limitations, and package structure.

### Questions for refinement
1. **Which Firefox support floor should the port target?** Choose a current stable Firefox release only, or include ESR; this changes manifest/API compatibility and test coverage.

   **Answer:**

2. **Should the Firefox package use Manifest V2 or Manifest V3?** MV2 may maximise legacy compatibility, while MV3 aligns with Chrome but has different background/injection constraints and minimum-version implications.

   **Answer:**

3. **Should Firefox share the Chrome package or ship as a separate package directory?** A shared package reduces drift, while a separate package makes browser-specific permissions, metadata, and release artefacts explicit.

   **Answer:**

### Documentation impact
- Update `_docs/spec.md` to replace the Firefox non-goal and document the supported Firefox release/ESR floor, toolbar behaviour, restricted-page limitation, and permission model.
- Update `_docs/design.md` only if Firefox toolbar icon rendering or browser-surface conventions differ from the existing icon treatment.
- Add Firefox packaging/submission details to the relevant publishing documentation, while leaving execution and account/signing work to the publishing child task.
- Update `_docs/usability-issues.md` only if the browser test reveals a predicted user-facing failure; no new issue is implied by this investigation alone.

### Related items
- Package Autoscroll as a Safari App Extension (`package-autoscroll-safari.md`) — complementary: separate browser implementation and packaging path.
- Test Autoscroll in Firefox and Safari (`cross-browser-test-autoscroll.md`) — prerequisite: validates the Firefox artifact against the agreed behaviour matrix.
- Prepare Firefox and Safari publishing (`publish-autoscroll-browser-versions.md`) — complementary: prepares Mozilla release materials after implementation and testing.
