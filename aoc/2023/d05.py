import re
from collections import defaultdict
from aoc.util import load_input_lines


def p1(ls):
    seeds = map(int, ls[0].split(":")[1].strip().split())
    ms = []
    m = {}
    for l in ls[2:]:
        if len(l) == 0:
            ms.append(m)
            m = {}
        mat = re.match(r"(\d+) (\d+) (\d+)", l)
        if mat:
            r = list(map(int, mat.group(0).split()))
            m[r[0]] = r
            
    def mapper(x: int, m: dict):
        for i in sorted(m.keys()):
            if x < i:
                return x,
            # if x < m[i]
            # k
            

    # print(ms)

    # print(list(seeds))
    return None


def p2(ls):
    pass


ls = load_input_lines(2023, 5, "t")
# ls = load_input_lines(2023, 5)
print(p1(ls), p2(ls))
