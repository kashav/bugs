#!/usr/bin/bash

set -eo pipefail

if [ -z "$1" ]; then
  echo "usage: $0 file"
  exit 1
fi

RE="(box|description|divbutton|divitem|divspring|divtabstop|hbox|html:div|html:img|html:input|html:label|html:span|html:strong|image|menupopup|menuseparator|moz-input-div|observes|stack|toolbar|tooltip|vdiv)"
sed -r s/"$RE"/div/g "$@" | \
  tidy -indent -output tidy-"$@"
