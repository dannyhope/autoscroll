# Test Autoscroll in Firefox and Safari
**Readiness:** refined
**Partially refined:** 2026-09-03
**Roadmap:** now
**Parent:** `port-extension-to-safari-and-firefox.md`

## Human verification checklist

- **Run the Firefox matrix**
  Follow the protocol in [`_docs/cross-browser-test-matrix.md`](../../_docs/cross-browser-test-matrix.md) with the generated Firefox package and record the result of each row.
- **Complete Safari setup before testing**
  Build/install the Safari package once its Xcode project exists, then record the Safari rows and any platform-specific limitations.

No UI screenshot — this is a manual browser validation and documentation task.

Define and execute a cross-browser test matrix for installation and runtime behaviour: toolbar click starts scrolling, a second click stops, upward wheel input stops, downward input does not, navigation resets the page state, and unsupported/restricted pages fail safely. Record browser versions, package versions, and any behavioural differences.

**Done when:** Firefox and Safari installations have repeatable pass/fail evidence for the agreed matrix, with regressions and platform-specific limitations recorded.

## Auto-investigation
**Investigated:** 2026-09-03

### Findings
- The repository is currently a Chrome-only Manifest V3 package: `Autoscroll/manifest.json` uses Chrome `action`, `background.service_worker`, `activeTab`, and `scripting`.
- `Autoscroll/background.js` injects `bookmarklet.js` only after a toolbar click and silently catches injection failures, which covers restricted-page safety in Chrome but provides no observable evidence.
- `Autoscroll/bookmarklet.js` toggles a page-global interval (`1000px` every `100ms`), stops on upward wheel input (`deltaY < 0`), and ignores downward wheel input. It has no explicit navigation-reset logic; navigation naturally discards the injected page context.
- The product spec explicitly lists Firefox and Safari ports as non-goals, and documents Chrome-specific restricted pages. There is no Firefox or Safari package, browser-specific manifest, or existing automated cross-browser harness.
- Firefox and Safari do not provide a drop-in equivalent installation path for this Chrome package. A meaningful test requires first defining the port/package format and supported minimum browser versions, then testing those artifacts on real browser runtimes.

### Scope
- Likely files: new browser-specific manifests/build/package files under `Autoscroll/` or separate browser package directories; possibly adapted background/injection code; cross-browser test documentation/evidence; `_docs/spec.md` and likely `_docs/design.md` if the supported-product scope changes.
- Estimated complexity: large.
- Docs impact: the current spec's Firefox/Safari non-goal must be revised before implementation; design only needs changes if browser-specific controls or packaging affect the user-facing surface.
- This task is a validation workstream dependent on `port-extension-to-safari-and-firefox.md`; it cannot produce valid pass/fail installation evidence from the current Chrome-only artifact.

### Proposed implementation
1. Decide the supported Firefox and Safari extension technologies, minimum versions, installation/distribution paths, and whether parity is required or platform limitations are accepted.
2. Create or identify the browser-specific packages, preserving the existing no-popup/no-overlay behaviour and the current toggle, wheel, navigation, and safe-failure semantics where the platform permits.
3. Define a repeatable matrix covering toolbar start, second-click stop, upward-wheel stop, downward-wheel continuation, navigation reset, and restricted/unsupported pages. Include clean-install and reload cases.
4. Execute the matrix on pinned browser/OS versions, recording package hashes/versions, exact steps, pass/fail results, console or extension errors, and platform-specific limitations.
5. Update the spec, test evidence, and release/package documentation so the claimed support matches tested artifacts.
- Navigation reset should be tested as a fresh-document invariant, not assumed solely from the current Chrome implementation.
- Restricted-page behaviour needs an explicit expected result per browser because “silently does nothing” is currently only implemented/documented for Chrome.

### Questions for refinement
1. **Which Firefox and Safari delivery targets should be supported?** Options include Firefox desktop WebExtension plus Safari Web Extension Converter/ Safari App Extension packaging; specify minimum browser and macOS versions.

   **Answer:** most recent versions of macOS, firefox and safari. i dont know what the different kinds of extension are, make an educated guess

2. **Is cross-browser parity required before this test task is complete?** Choose full parity for all matrix rows, or allow documented platform-specific deviations where APIs or restricted-page rules differ.

   **Answer:** yes

3. **What evidence format and runtime coverage should be accepted?** For example, a checked-in Markdown matrix with browser versions and logs, plus manual real-browser runs, versus automated WebDriver/Web Extension tests supplemented by manual installation checks.

   **Answer:** manual real browser runs

### Documentation impact
- Update `_docs/spec.md` to replace the current Firefox/Safari non-goal with the agreed support boundary and browser-specific limitations.
- Update `_docs/design.md` only if packaging or browser differences change the user-facing toolbar/icon experience.
- Add the agreed test matrix and evidence location once targets and evidence standards are decided.

### Related items
- Port Autoscroll to Firefox (`port-autoscroll-firefox.md`) — prerequisite: supplies the Firefox artifact under test.
- Package Autoscroll as a Safari App Extension (`package-autoscroll-safari.md`) — prerequisite: supplies the Safari artifact under test.
- Prepare Firefox and Safari publishing (`publish-autoscroll-browser-versions.md`) — complementary: release materials should match the recorded test evidence.
