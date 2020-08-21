#!/usr/bin/env python3

import grequests
import sys

QUERY = """{
  "from": "unittest",
  "select": [
    {"name": "runs", "value": "result.test", "aggregate": "count"},
    {"name": "ok", "value": "result.ok", "aggregate": "count"},
    {"name": "pass", "value": "result.stats.pass", "aggregate": "count"},
    {"name": "fail", "value": "result.stats.fail", "aggregate": "count"},
    {"name": "notrun", "value": "result.stats.notrun", "aggregate": "count"},
    {"name": "timeout", "value": "result.stats.timeout", "aggregate": "count"},
    {"name": "crash", "value": "result.crash", "aggregate": "count"}
  ],
  "groupby": ["result.test", "build.platform", "build.type"],
  "limit": 1000,
  "where": {"and": [
    {"in": {"repo.branch.name": ["autoland", "mozilla-central"]}},
    {"gte": ["repo.push.date", {"date": "today-6month"}]},
    {"lte": ["repo.push.date", {"date": "eod"}]},
    {"regex": {"result.test": ".*%s.*"}},
    {"regex": {"run.key": ".*fis.*"}}
  ]}
}"""

URL = "http://activedata.allizom.org/query"

def query(testname):
    return QUERY % testname

def main(argv):
    qs = map(lambda l: grequests.post(URL, data=query(l.strip())), sys.stdin)
    rs = grequests.map(qs, size=5)

    did_print_headers = False

    for r in rs:
        json = r.json()

        if not did_print_headers:
            print(",".join(map(lambda s: s.replace(".", "_"), json['header'])))
            did_print_headers = True

        for row in json['data']:
            print(",".join(map(str, row)))

if __name__ == "__main__":
    sys.exit(main(sys.argv))
