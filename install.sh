#!/usr/bin/env bash
# Install hackathon-skill into detected agent harness skill dirs.
# Usage: ./install.sh [--target claude|codex|cursor|gemini|all]  (default: all detected)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
SKILL_SRC="$ROOT/skills/hackathon"

target="${2:-all}"
installed=()

install_into() {
  local dir="$1" name="$2"
  mkdir -p "$dir"
  # skills are directory-scoped: copy the SKILL.md + scripts + references together
  dest="$dir/hackathon"
  rm -rf "$dest" 2>/dev/null || true
  mkdir -p "$dest"
  cp "$SKILL_SRC/SKILL.md" "$dest/SKILL.md"
  cp -R "$ROOT/scripts" "$dest/scripts"
  cp -R "$ROOT/references" "$dest/references"
  cp -R "$ROOT/templates" "$dest/templates"
  installed+=("$name -> $dest")
}

[ "$target" = "all" ] || [ "$target" = "claude" ] && [ -d "$HOME/.claude" ] && install_into "$HOME/.claude/skills" "claude"
[ "$target" = "all" ] || [ "$target" = "claude" ] && [ -d "$PWD/.claude" ] && install_into "$PWD/.claude/skills" "claude(project)"
{ [ "$target" = "all" ] || [ "$target" = "codex" ]; } && [ -d "$HOME/.codex" ] && install_into "$HOME/.codex/skills" "codex"
{ [ "$target" = "all" ] || [ "$target" = "cursor" ]; } && [ -d "$HOME/.cursor" ] && install_into "$HOME/.cursor/skills" "cursor"
{ [ "$target" = "all" ] || [ "$target" = "gemini" ]; } && [ -d "$HOME/.gemini" ] && install_into "$HOME/.gemini/skills" "gemini"
{ [ "$target" = "all" ] || [ "$target" = "devin" ]; } && [ -d "$HOME/.config/devin" ] && install_into "$HOME/.config/devin/skills" "devin"

if [ ${#installed[@]} -eq 0 ]; then
  echo "no harness skill dirs found; install manually:"
  echo "  mkdir -p ~/.claude/skills/hackathon && cp -R skills/hackathon/SKILL.md scripts references templates ~/.claude/skills/hackathon/"
  exit 1
fi
printf 'installed: %s\n' "${installed[@]}"
