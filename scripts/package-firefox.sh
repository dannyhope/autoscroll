#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
output="${1:-${repo_root}/publish/autoscroll-firefox.xpi}"
mkdir -p "$(dirname "$output")"
rm -f "$output"
(
  cd "$repo_root/Firefox"
  zip -q -r "$output" manifest.json background.js bookmarklet.js \
    icon-16.png icon-48.png icon-128.png -x '*.DS_Store'
)
printf 'Created %s\n' "$output"
