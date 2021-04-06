#!/usr/bin/env bash

set -eu

while true; do
  file=$(mach wpt-metadata-summary 2>/dev/null | \
         rg wptrunner.wptmanifest.parser.ParseError | \
         cut -d":" -f3 | \
         cut -d" " -f2)

  if [ -z "$file" ]; then
    echo "done"
    exit 0
  fi

  hg revert -r .^ "$file"
  subl "$file"

  read -p "$(basename "$file"): [b]reak / [C]ontinue / [d]elete? " bcd
  case $bcd in
    b ) break ;;
    d ) rm "$file" ;;
    * ) ;;
  esac
done
