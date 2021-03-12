#!/usr/bin/env python3

import collections
import json
import sys
from dataclasses import dataclass
from mozci.push import Push, Status


def record(results, name, config, status):
    if name not in results:
        results[name] = {}

    if config not in results[name]:
        results[name][config] = collections.defaultdict(int)

    results[name][config][status] += 1


def main(argv):
    if len(argv) != 3:
        print(f"{sys.argv[0]} branch revs")
        return 1

    branch = argv[1]
    revs = argv[2].split(",")[0]

    # {
    #   (test, subtest): {
    #       config: {
    #           status: int
    #       }
    #   }
    # }
    results = collections.defaultdict(
        lambda: collections.defaultdict(lambda: collections.defaultdict(int))
    )

    push = Push(revs, branch)
    for (config, group), summary in push.config_group_summaries.items():
        if not ("-fis-" in config and group.startswith("testing/web-platform")):
            continue

        print(config, group)

        for task in summary.tasks:
            paths = [a for a in task.artifacts if a.endswith("wptreport.json")]
            for path in paths:
                run = task.get_artifact(path)

                for result in run["results"]:
                    name = (result["test"], "")
                    status = result["status"]
                    results[name][config][status] += 1

                    for subtest in result["subtests"]:
                        name = (result["test"], subtest["name"])
                        status = subtest["status"]
                        results[name][config][status] += 1

    # figure out what other statuses exists
    print("test,subtest,config,OK,PASS,SKIP,FAIL")
    for (test, subtest), configs in results.items():
        for config, statuses in configs.items():
            line = [
                test,
                subtest,
                config,
                *[str(statuses[k]) for k in ["OK", "PASS", "SKIP", "FAIL"]],
            ]
            print(",".join(line))

    return 0


if __name__ == "__main__":
    exit(main(sys.argv))
