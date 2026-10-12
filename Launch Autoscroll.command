#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"

if command -v cursor >/dev/null 2>&1; then
  open -a Cursor "$ROOT"
else
  open -a "Visual Studio Code" "$ROOT"
fi

if [[ -d "$ROOT/Safari/AutoscrollSafari.xcodeproj" ]]; then
  open "$ROOT/Safari/AutoscrollSafari.xcodeproj"
fi

open "chrome://extensions/"

