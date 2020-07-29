#!/usr/bin/env python3

import pprint
import sys


INIT = "Init"
PROCESS = "ProcessIncomingMessages"
DESTROY = "Destroy"

def main():
    lines = sys.stdin.readlines()
    data = {}

    for i, line in enumerate(lines):
        msg, addr, *_ = line.split()

        if msg == INIT:
            data[addr] = {
                "addr": addr,
                "init": i,
                "refs": (),
                "dtor": -1,
            }

        if msg == DESTROY:
            data[addr]["dtor"] = i

        if msg == PROCESS:
            data[addr]["refs"] += i,


    pprint.pprint(data)
    return 0


if __name__ == '__main__':
    sys.exit(main())
