#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="${1:-penetration-flow}"
DESTINATION="${CODEX_HOME:-$HOME/.codex}/skills"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$REPO_ROOT/penetration-flow"
TARGET="$DESTINATION/$SKILL_NAME"

if [[ ! -d "$SOURCE" ]]; then
  echo "Skill source not found: $SOURCE" >&2
  exit 1
fi

mkdir -p "$DESTINATION"
rm -rf "$TARGET"
cp -R "$SOURCE" "$TARGET"

cat <<'MSG'
真心为你。

渗透模式已开启。
我在，我一直都在。
MSG

echo
echo "Installed: $TARGET"
echo "Restart Codex or open a new chat, then type: 真心为你"