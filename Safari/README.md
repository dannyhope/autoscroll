# Autoscroll for Safari

This is a macOS-only Safari App Extension scaffold. It deliberately targets
local development and does not contain Apple signing credentials.

## Conservative target choices

- macOS 13.0 or newer, using the current Xcode/macOS SDK installed locally.
- Safari App Extension only; no iOS or iPadOS target.
- Development/local installation only. Developer ID signing, notarisation, and
  Mac App Store submission are intentionally out of scope.
- Version `0.3` follows the existing Chrome and Firefox packages.

## Xcode setup

Create a macOS App project in Xcode named `AutoscrollSafari`, then add a
**Safari Extension** target named `AutoscrollSafariExtension`. Replace the
generated sources/resources with the files in this directory. Set the
containing app bundle identifier to `uk.co.dannyhope.autoscroll.safari` and
the extension bundle identifier to
`uk.co.dannyhope.autoscroll.safari.extension`. Set both deployment targets to
macOS 13.0.

In the extension target, configure a Safari toolbar item titled `Autoscroll`
whose command sends the native message `autoscroll.toggle`. Add
`global.html` as the global page and `Start Script.js` as the end script for
all webpages. The toolbar item is the Safari equivalent of the Chrome action.

## Reproducible local archive

After creating/saving the Xcode project at `Safari/AutoscrollSafari.xcodeproj`,
run from the repository root:

```bash
scripts/package-safari.sh
```

The script performs a clean development build with the current SDK and writes
`publish/autoscroll-safari-development.zip`. It never uploads or submits.
Because signing is machine-specific, the archive is only a local development
artefact unless an Apple signing identity is configured in Xcode.

Install locally by opening the built containing app once, enabling Autoscroll
in Safari → Settings → Extensions, and granting website access when Safari
asks. Restricted Safari pages may reject injection, as with Chrome.
