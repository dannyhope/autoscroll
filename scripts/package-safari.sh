#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PROJECT="$ROOT/Safari/AutoscrollSafari.xcodeproj"
BUILD="$ROOT/Safari/build"
OUTPUT="$ROOT/publish/autoscroll-safari-development.zip"

if [[ ! -d "$PROJECT" ]]; then
  echo "Missing $PROJECT"
  echo "Create the Xcode macOS app and Safari Extension targets first; see Safari/README.md."
  exit 1
fi

rm -rf "$BUILD"
xcodebuild \
  -project "$PROJECT" \
  -scheme AutoscrollSafari \
  -configuration Debug \
  -derivedDataPath "$BUILD" \
  CODE_SIGNING_ALLOWED=NO \
  build

APP="$(find "$BUILD/Build/Products/Debug" -maxdepth 1 -name '*.app' -print -quit)"
if [[ -z "$APP" ]]; then
  echo "Build succeeded but no app was produced."
  exit 1
fi

rm -f "$OUTPUT"
ditto -c -k --sequesterRsrc --keepParent "$APP" "$OUTPUT"
echo "Wrote $OUTPUT"
