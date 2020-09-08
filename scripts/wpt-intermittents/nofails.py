#!/usr/bin/env python3

import sys
import csv


def main(argv):
    if len(argv) < 2:
        print(f"{argv[0]} frq.csv")
        return 1

    fi = open(argv[1], "r")
    rd = csv.reader(fi)

    ix = dict()
    for rw in rd:
        if rd.line_num == 1:
            ix.update({nm: i for i, nm in enumerate(rw)})
            continue

        if all(map(lambda x: int(x) == 0, rw[ix["fail"] :])):
            print(rw[0])

    fi.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
