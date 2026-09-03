#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
out="$root/publish/autoscroll-firefox.xpi"
mkdir -p "$root/publish"
rm -f "$out"
(cd "$root/Firefox" && zip -q -r "$out" manifest.json background.js bookmarklet.js \
  icon-16.png icon-48.png icon-128.png -x "*.DS_Store")
printf '%s\n' "$out"
