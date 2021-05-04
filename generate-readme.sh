#!/usr/bin/env bash

echo -e "### bugs\n"

find * -maxdepth 0 -regextype posix-extended -regex '[0-9]{7}' |
  xargs -I{} echo "- [{}]({}) ([bugzilla](https://bugzilla.mozilla.org/show_bug.cgi?id={}), [github](https://github.com/kashav/bugs/tree/master/{}))"
