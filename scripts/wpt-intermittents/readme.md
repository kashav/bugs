### wpt-frequencies

```sh
$ URL="https://searchfox.org/mozilla-central/search?q=%28if%7Cand%29+fission.*%3A+%5C%5B&path=web-platform%2F**%2F*.ini&regexp=true"
$ ../searchfox/fetch-search-paths "$URL" | ./parse-file-names | ./query.py > frequencies.csv
```
