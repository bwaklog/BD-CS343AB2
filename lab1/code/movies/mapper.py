#!/usr/bin/env python3

import sys

_ = list(
    map(
        lambda line: print(f"{line[0]}\t{int(line[1])}"),
        map(lambda x: x.strip().split(","), sys.stdin),
    )
)
