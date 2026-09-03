# Package Autoscroll as a Safari App Extension
**Readiness:** built
**Partially refined:** 2026-09-03
**Roadmap:** now
**Parent:** `port-extension-to-safari-and-firefox.md`

Create the Safari App Extension and its host/container project, translating the toolbar command and page-script injection while preserving the existing no-overlay experience. Establish the selected platform/version target, signing/build configuration, and reproducible archive/export instructions.

**Done when:** A signed or explicitly development-scoped Safari package installs and passes the agreed behaviour matrix, with the chosen Apple distribution route documented.

## Auto-investigation
**Investigated:** 2026-09-03

### Findings
- The repository currently contains only a Chrome Manifest V3 package under `Autoscroll/`: `manifest.json`, `background.js`, `bookmarklet.js`, and PNG icons. There is no Xcode project, Safari App Extension target, host app, entitlements file, or archive/export script.
- The current background path depends on `chrome.action.onClicked` and `chrome.scripting.executeScript`; Safari packaging cannot be treated as a repackaged Chrome directory. The Safari extension needs a containing macOS app and Safari-specific extension APIs/message flow for the toolbar command and page injection.
- `bookmarklet.js` is self-contained page-world logic and should be reusable only after verifying Safari content-script/event semantics. It toggles a page-global interval, scrolls 1000px every 100ms, and stops on upward wheel input; it adds no overlay or stored state.
- The product spec currently lists Safari as a non-goal, so selecting Safari support requires updating `_docs/spec.md`; `_docs/design.md` likely only needs a note if Safari’s toolbar/icon conventions alter the documented two-arrow treatment.
- The parent task separates cross-browser testing and publishing. This task should establish the Safari project/package and reproducible build/export path, while behavioural evidence and Apple submission execution remain separate concerns.

### Scope
- Create an Xcode containing macOS app plus Safari App Extension target, with the extension source, shared/page script strategy, icons, bundle identifiers, entitlements, deployment target, and signing configuration.
- Decide and document the supported macOS/Safari floor and whether the output is development-only, Developer ID, or Mac App Store distribution; these choices affect project settings, signing, archive/export configuration, and install instructions.
- Add a reproducible archive/export/package command or documented Xcode procedure, without uploading to Apple.
- Estimated complexity: large.
- Docs impact: `_docs/spec.md`, likely `_docs/design.md`, and Safari-specific packaging/release documentation.

### Proposed implementation
1. Choose the macOS-only versus macOS plus iOS/iPadOS target, minimum supported versions, bundle identifiers, and Apple distribution route before scaffolding the project.
2. Create the containing app and Safari App Extension targets in Xcode, configure signing/entitlements and the selected deployment target, and include the existing icon treatment in the appropriate Safari extension assets.
3. Implement Safari toolbar-command handling and page-script injection using Safari APIs, preserving click-to-toggle, upward-wheel stop, navigation reset, restricted-page failure, and no-overlay behaviour.
4. Add a deterministic archive/export/package workflow and development installation instructions; keep credentials, notarisation, and App Store submission outside automated local packaging.
5. Run the sibling cross-browser behaviour matrix, then record tested versions, limitations, package structure, and the chosen Apple publishing route in the product/release docs.

### Questions for refinement
1. **Which Apple platforms and minimum versions should Safari support?** Choose macOS Safari only, or macOS plus iOS/iPadOS; the latter requires additional targets and testing.

   **Answer:** Answer 1

2. **What Safari distribution target is required?** Choose unsigned local development, Developer ID/direct distribution, or Mac App Store; signing, notarisation, and export configuration differ substantially.

   **Answer:** Answer 2

3. **Which macOS and Safari support floor should be tested?** Choose a current release only or include an older supported macOS/Safari version; this determines deployment targets and the behaviour matrix.

   **Answer:** Answer 3

4. **Should Safari share the Chrome version and release cadence?** A shared policy affects bundle versions, update documentation, and release coordination across packages.

   **Answer:** Answer 4

### Documentation impact
- Update `_docs/spec.md` to replace the Safari non-goal with the selected platform/version support, Safari toolbar behaviour, restrictions, and any Safari-specific limitations.
- Update `_docs/design.md` if Safari’s extension toolbar/icon surface requires a documented visual adaptation; otherwise retain the existing quiet, no-overlay treatment.
- Add or extend Safari packaging/release documentation with project structure, reproducible archive/export steps, installation scope, and signing prerequisites.
- Update `_docs/usability-issues.md` only if cross-browser testing identifies a predicted user-facing failure; none is implied by this investigation alone.

### Related items
- Port Autoscroll to Firefox (`port-autoscroll-firefox.md`) — complementary: separate browser implementation and packaging path.
- Test Autoscroll in Firefox and Safari (`cross-browser-test-autoscroll.md`) — prerequisite: validates the Safari artifact against the agreed behaviour matrix.
- Prepare Firefox and Safari publishing (`publish-autoscroll-browser-versions.md`) — complementary: prepares Apple release materials after packaging and testing.


## Human verification checklist
1. Review the implementation and documentation in the repository.
2. For Safari, create/configure the Xcode project, then run `scripts/package-safari.sh`; the current scaffold is development-scoped and not signed.
3. For Firefox, run `scripts/package-firefox.sh`, install the generated XPI as a temporary add-on, and verify toolbar toggle, upward-wheel stop, navigation reset, and restricted pages.

Self-check: relevant package scripts passed syntax validation and `git diff --check` passed.
Commit: e59c8174758713e20dfca545461340967b20e966
