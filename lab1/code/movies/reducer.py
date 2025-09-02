#!/usr/bin/env python3

import sys
from itertools import groupby
from operator import itemgetter
from functools import reduce

parsed = map(
    lambda line: (line[0], float(line[1])),
    map(lambda x: x.strip().split("\t"), sys.stdin),
)

for movie, group in groupby(parsed, key=itemgetter(0)):
    total, count = reduce(
        lambda acc, x: (acc[0] + x, acc[1] + 1), map(itemgetter(1), group), (0.0, 0)
    )
    print(f"{movie}\t{total / count}")
