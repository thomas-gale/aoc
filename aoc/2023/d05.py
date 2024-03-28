from collections import defaultdict
from itertools import chain
import re
from aoc.util import load_input_lines


def get_maps(ls):
    """
    Maps of source to (destination and length)
    """
    ms = []
    m = {}
    for l in ls[2:]:
        if len(l) == 0:
            ms.append(m)
            m = {}
        mat = re.match(r"(\d+) (\d+) (\d+)", l)
        if mat:
            r = list(map(int, mat.group(0).split()))
            m[r[1]] = (r[0], r[2])
    ms.append(m)
    return ms


def mapper(x: int, m: dict):
    for i in sorted(m.keys()):
        if x >= i and x < i + m[i][1]:
            return m[i][0] + x - i
    return x


def p1(ls):
    seeds = map(int, ls[0].split(":")[1].strip().split())
    ms = get_maps(ls)
    locs = []
    for x in seeds:
        for m in ms:
            x = mapper(x, m)
        locs.append(x)
    return sorted(locs)[0]


def p2(ls):
    seeds = list(map(int, ls[0].split(":")[1].strip().split()))
    seeds = zip(seeds[::2], seeds[1::2])
    seeds = list(chain(*[list(range(x, x + y)) for x, y in seeds]))
    print(list(seeds))
    ms = get_maps(ls)
    locs = []
    # Brute force too slow
    for x in seeds:
        for m in ms:
            x = mapper(x, m)
        locs.append(x)
    return sorted(locs)[0]


ls = load_input_lines(2023, 5, "t")
# ls = load_input_lines(2023, 5)
print(p1(ls), p2(ls))
