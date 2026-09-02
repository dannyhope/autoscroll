#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DOMAIN="$(tr -d '[:space:]' < "$ROOT/.local-domain")"
PORT="$(tr -d '[:space:]' < "$ROOT/.dev-port")"

[[ "$DOMAIN" == "autoscroll.local" ]] || { printf 'error: expected autoscroll.local, got %s\n' "$DOMAIN" >&2; exit 1; }
[[ "$PORT" =~ ^[0-9]+$ ]] || { printf 'error: invalid development port: %s\n' "$PORT" >&2; exit 1; }

"$SCRIPT_DIR/ensure-local-domain.sh"
printf '%s is configured for local tooling; this project has no HTTP server to check\n' "$DOMAIN"
