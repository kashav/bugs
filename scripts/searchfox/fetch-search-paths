#!/usr/bin/bash

set -e

if [ -z "$1" ]; then
  echo "usage: $0 url"
  exit 1
fi

curl -sSL -H 'Accept: application/json' "$1" \
  | jq --raw-output '[.test."Textual Occurrences"[].path][]'
