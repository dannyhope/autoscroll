# Prepare Firefox and Safari publishing
**Readiness:** auto-refined
**Roadmap:** later
**Parent:** `port-extension-to-safari-and-firefox.md`

Prepare browser-specific store and distribution artefacts after the implementations are stable: Mozilla Add-ons metadata/package and submission checklist, plus the chosen Safari signing/archive/App Store or direct-distribution materials. Keep privacy and support copy aligned with the actual permissions and platform behaviour, and do not auto-upload.

**Done when:** Firefox and Safari release packages, listing copy, privacy/support links, and manual submission steps are complete and internally consistent.

## Auto-investigation
**Investigated:** 2026-09-03

### Findings
- The repository currently ships only a Chrome Manifest V3 package under `Autoscroll/`, with `activeTab` and `scripting` permissions, a service-worker click handler, and the shared page-scrolling script.
- There are no Firefox or Safari release packages, browser-store metadata, signing configuration, or browser-specific publishing checklists yet.
- Firefox publishing follows Mozilla Add-ons packaging, metadata, signing, and review requirements; Safari publishing depends on the separate Xcode Safari App Extension/container and the Apple distribution route selected by the sibling packaging task.
- Existing privacy/support copy is Chrome-specific in places: `privacy-policy.html` describes Chrome storage and permissions, while `publish/LISTING.md` and `publish/index.html` are Chrome Web Store materials. Browser-specific copy must match the implemented permissions and behaviour rather than being copied unchanged.
- The parent task is already split into Firefox implementation, Safari packaging, and cross-browser testing. This task should prepare release materials after those outputs and tested support versions exist; it should not duplicate implementation or testing.

### Scope
- Add Firefox listing metadata, privacy/support links, package submission checklist, and reproducible packaging/upload guidance.
- Add Safari listing/distribution materials appropriate to the chosen macOS/Safari target and Apple route, including archive/export/signing prerequisites without auto-upload.
- Reconcile browser-specific privacy statements, permissions, version numbers, screenshots/assets, and support links with the completed ports and test evidence.
- Estimated complexity: medium, contingent on the sibling implementation and packaging decisions.
- Docs impact: update `_docs/spec.md` and `_docs/design.md` only where the final supported browser surfaces or limitations differ; add or extend publishing documentation for Mozilla and Apple release paths.

### Proposed implementation
1. Consume the final Firefox and Safari package structures, support floors, permission models, version policy, and tested limitations from the sibling tasks.
2. Prepare separate Mozilla Add-ons metadata and a manual submission checklist, including package validation/signing expectations and the correct privacy/support URLs.
3. Prepare Safari archive/export/distribution notes and listing/support copy for the selected Apple route; keep certificates, notarisation, App Store Connect, and submission actions manual.
4. Produce or adapt only browser-appropriate screenshots and icons, ensuring copy and assets show the real toolbar control and no invented overlay.
5. Validate all release materials against the cross-browser test matrix and the product privacy policy, then document what is ready and what requires operator credentials. Do not upload automatically.

### Questions for refinement
1. **Which Firefox and Safari versions and package versions should the release materials target?** Use the support floors and shared/separate version policy decided by the implementation and Safari packaging tasks; publishing copy cannot be final until these are fixed.

   **Answer:**

2. **Which Apple distribution route should the Safari materials support?** Mac App Store, Developer ID/direct distribution, or development-only export changes the required archive, signing, notarisation, and submission checklist.

   **Answer:**

3. **Which public support and privacy URL should every browser listing use?** Reuse the existing Danny Hope hop if it covers all browser versions, or create a browser-specific hop only if the content or destination genuinely differs.

   **Answer:**

4. **Who will provide Mozilla and Apple account/signing access at submission time?** The repository can prepare artefacts and checklists, but store submission, signing, notarisation, and review actions require the relevant operator accounts or credentials.

   **Answer:**

### Documentation impact
- Update `_docs/spec.md` with the final supported browsers, versions, permissions, and platform-specific limitations before publishing.
- Update `_docs/design.md` only if Firefox or Safari toolbar/icon conventions require a documented visual adaptation.
- Add browser-specific release documentation/checklists alongside `publish/LISTING.md` or in a clearly named publishing document, keeping Chrome instructions intact.
- Update `privacy-policy.html` and hosted policy copy if the final cross-browser behaviour or permissions make the current Chrome-specific wording incomplete.

### Related items
- Port Autoscroll to Firefox (`port-autoscroll-firefox.md`) — prerequisite: provides the Firefox package and support decisions.
- Package Autoscroll as a Safari App Extension (`package-autoscroll-safari.md`) — prerequisite: provides the Safari project and distribution decisions.
- Test Autoscroll in Firefox and Safari (`cross-browser-test-autoscroll.md`) — prerequisite: provides verified versions, behaviour evidence, and limitations.
