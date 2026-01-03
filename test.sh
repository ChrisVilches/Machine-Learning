#!/usr/bin/env bash

# Get all tracked files
files=$(git ls-files '*.md' '*.qmd')

# Safety: empty repo
[ -z "$files" ] && exit 0

if git ls-files -z '*.md' '*.qmd' | xargs -0 grep -n '````'; then
  echo "❌ Error: Found four consecutive backticks"
  exit 1
fi

exit 0
