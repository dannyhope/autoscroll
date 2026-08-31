#!/usr/bin/env bash
# Maintain the project's loopback hostname in the macOS hosts file.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
HOSTS_FILE="${DANNIFY_HOSTS_FILE:-/etc/hosts}"

if [[ -n "${DANNIFY_PROJECT_SLUG:-}" ]]; then
	PROJECT_SLUG="$DANNIFY_PROJECT_SLUG"
else
	PROJECT_SLUG="$(basename "$ROOT" | LC_ALL=C tr '[:upper:]' '[:lower:]' | LC_ALL=C sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')"
fi

DOMAIN_FILE="$ROOT/.local-domain"
if [[ -z "${DANNIFY_LOCAL_DOMAIN:-}" && -r "$DOMAIN_FILE" ]]; then
	DOMAIN="$(tr -d '[:space:]' < "$DOMAIN_FILE")"
else
	DOMAIN="${DANNIFY_LOCAL_DOMAIN:-${PROJECT_SLUG}.local}"
fi
MARKER="# dannify-local-domain:${PROJECT_SLUG}"

if [[ ! "$PROJECT_SLUG" =~ ^[a-z0-9]([a-z0-9-]*[a-z0-9])?$ ]]; then
	printf 'error: invalid project slug: %s\n' "$PROJECT_SLUG" >&2
	exit 1
fi

if [[ ! "$DOMAIN" =~ ^[a-z0-9]([a-z0-9-]*[a-z0-9])?\.(local|test)$ ]]; then
	printf 'error: local domain must be a valid .local or .test hostname: %s\n' "$DOMAIN" >&2
	exit 1
fi

if [[ ! -r "$HOSTS_FILE" ]]; then
	printf 'error: cannot read hosts file: %s\n' "$HOSTS_FILE" >&2
	exit 1
fi

if awk -v domain="$DOMAIN" -v marker="$MARKER" '
	$1 ~ /^#/ { next }
	{
		for (i = 2; i <= NF && $i !~ /^#/; i++) {
			if ($i == domain) {
				if ($1 == "127.0.0.1" && index($0, marker) > 0) {
					managed = 1
				} else if ($1 == "127.0.0.1") {
					existing_loopback = 1
				} else {
					conflict = 1
				}
			}
		}
	}
	END {
		if (conflict) exit 2
		if (managed || existing_loopback) exit 0
		exit 1
	}
' "$HOSTS_FILE"; then
	printf '%s already resolves to 127.0.0.1\n' "$DOMAIN"
	exit 0
else
	STATUS=$?
	if [[ "$STATUS" -eq 2 ]]; then
		printf 'error: %s already has a conflicting hosts entry\n' "$DOMAIN" >&2
		exit 1
	fi
fi

TEMP_FILE="$(mktemp "${TMPDIR:-/tmp}/dannify-hosts.XXXXXX")"
trap 'rm -f "$TEMP_FILE"' EXIT

awk -v marker="$MARKER" 'index($0, marker) == 0 { print }' "$HOSTS_FILE" >"$TEMP_FILE"
printf '127.0.0.1\t%s\t%s\n' "$DOMAIN" "$MARKER" >>"$TEMP_FILE"

if [[ "$HOSTS_FILE" == "/etc/hosts" ]]; then
	sudo /usr/bin/install -o root -g wheel -m 644 "$TEMP_FILE" "$HOSTS_FILE"
	sudo /usr/bin/dscacheutil -flushcache
	sudo /usr/bin/killall -HUP mDNSResponder >/dev/null 2>&1 || true
else
	/usr/bin/install -m 644 "$TEMP_FILE" "$HOSTS_FILE"
fi

printf 'Added %s -> 127.0.0.1 to %s\n' "$DOMAIN" "$HOSTS_FILE"
