# Port the Autoscroll extension to Safari and Firefox
**Readiness:** built
**Partially refined:** 2026-09-03
**Type:** parent
**Children:**
- `port-autoscroll-firefox.md` — Port Autoscroll to Firefox
- `package-autoscroll-safari.md` — Package Autoscroll as a Safari App Extension
- `cross-browser-test-autoscroll.md` — Test Autoscroll in Firefox and Safari
- `publish-autoscroll-browser-versions.md` — Prepare Firefox and Safari publishing
**Done when:** All child tasks are complete (built/closed).

## Task

Create and publish compatible Safari and Firefox versions of the Autoscroll
browser extension.

## Notes

- Review the current Chrome Manifest V3 implementation and identify the
  cross-browser compatibility changes.
- Preserve the existing behaviour: click the toolbar icon to start scrolling;
  scroll up to stop.
- Prepare the required Safari App Extension packaging and Firefox add-on
  packaging.
- Test installation and behaviour in both browsers before publishing.

## Auto-investigation
**Investigated:** 2026-09-03

### Findings
- The current loadable package is a small Chrome Manifest V3 extension: `Autoscroll/manifest.json`, `background.js`, and `bookmarklet.js`.
- `background.js` listens to `chrome.action.onClicked` and injects `bookmarklet.js` with `chrome.scripting.executeScript` into only the clicked tab. It silently ignores restricted pages.
- `bookmarklet.js` toggles a page-global interval, scrolling 1000px every 100ms; upward wheel input stops it. Clicking the toolbar icon injects the script again, which toggles the existing state.
- The product docs explicitly make Firefox and Safari ports non-goals today, so the port must update `_docs/spec.md` and likely `_docs/design.md` if toolbar/icon packaging or browser surfaces differ.
- `publish/LISTING.md` is Chrome Web Store-specific. Safari distribution uses an Xcode Safari App Extension target and Apple signing/distribution; Firefox uses a separate add-on package and Mozilla Add-ons review/signing. These are distinct release paths, not one shared upload.
- No test harness currently exists. Behavioural validation will need browser-specific installation tests plus checks for restricted pages, navigation reset, repeated clicks, and upward-wheel stopping.

### Scope
- Firefox: likely add a Firefox-compatible manifest/background implementation, preserving the toolbar action and least-privilege tab access; verify API compatibility and package as an unsigned development add-on and/or signed `.xpi`.
- Safari: create an Xcode-hosted Safari App Extension target/container, map the toolbar command and script injection to Safari APIs, add signing/build configuration, and decide supported macOS/Safari versions.
- Shared script: audit `bookmarklet.js` for Safari/Firefox page-world and event semantics; retain the current no-overlay behaviour.
- Packaging/publishing: add reproducible Firefox packaging and Safari archive/export instructions/assets without auto-uploading; update listing/privacy/support copy where browser-specific requirements differ.
- Tests/docs: add a repeatable cross-browser test matrix and update `_docs/spec.md`, `_docs/design.md`, and relevant publish documentation.
- Estimated complexity: large.

### Proposed implementation
1. Define the support matrix and release architecture, keeping Firefox as a WebExtension package and Safari as an Xcode Safari App Extension rather than assuming Chrome’s MV3 package is directly portable.
2. Implement and package the Firefox version, including manifest permissions/API differences and toolbar click injection.
3. Scaffold the Safari App Extension/container in Xcode, implement the equivalent toolbar command and page script injection, and configure signing/archive outputs.
4. Build a shared cross-browser test matrix covering start/stop toggling, upward wheel stop, navigation, restricted/internal pages, and install/update behaviour.
5. Run installation and behaviour tests in both browsers, then prepare separate Mozilla and Apple publishing metadata/checklists.
6. Update product and design docs so the supported browser surfaces, packaging constraints, permissions, and release process are reconstructable.

### Questions for refinement
1. **Which Safari platforms and minimum versions should be supported?** Safari App Extension implementation and Xcode deployment settings differ between macOS-only and macOS plus iOS/iPadOS.

   **Answer:** Answer 1

2. **Should Firefox be Manifest V2-compatible or Manifest V3-only?** This affects background execution, API availability, and the minimum Firefox version.

   **Answer:** Answer 2

3. **What Safari distribution target is required?** Mac App Store, direct Developer ID distribution, or an unsigned/local build have different signing, review, and packaging work.

   **Answer:** Answer 3

4. **Should the two ports share a version number and release cadence with Chrome?** A shared version policy affects manifests, package names, store metadata, and update handling.

   **Answer:** Answer 4

5. **Who owns browser-store accounts and signing credentials?** Publishing can be prepared in-repo, but Mozilla submission/signing and Apple certificates/App Store Connect access may require operator access.

   **Answer:** Answer 5

### Documentation impact
- Update `_docs/spec.md` to replace the Firefox/Safari non-goal with the chosen support matrix, browser-specific behaviour/limitations, and permissions.
- Update `_docs/design.md` if Safari/Firefox toolbar icon treatment or platform conventions require documented visual differences.
- Extend or add publishing documentation alongside `publish/LISTING.md` for Mozilla Add-ons and Safari/Xcode release artefacts.
- Add the installation/test matrix to the appropriate `_docs/` document and create/update `_docs/usability-issues.md` if testing exposes predicted user failures.

### Related items
- _(parent will fill)_


## Human verification checklist
1. Review the implementation and documentation in the repository.
2. For Safari, create/configure the Xcode project, then run `scripts/package-safari.sh`; the current scaffold is development-scoped and not signed.
3. For Firefox, run `scripts/package-firefox.sh`, install the generated XPI as a temporary add-on, and verify toolbar toggle, upward-wheel stop, navigation reset, and restricted pages.

Self-check: relevant package scripts passed syntax validation and `git diff --check` passed.
Commit: Child Firefox task committed as e2bd44227f34f16f16243a524be43e8f30cfa4cc; Safari packaging committed as e59c8174758713e20dfca545461340967b20e966.
