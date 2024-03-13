from collections import Counter
from functools import reduce
from operator import mul
from aoc.util import load_input_lines


def p1_2(ls):
    bag = Counter(
        {
            "red": 12,
            "green": 13,
            "blue": 14,
        }
    )
    sum_1 = 0
    sum_2 = 0
    for l in ls:
        g, samples = l.strip().split(":")
        union = Counter()
        for s in samples.strip().split(";"):
            union |= Counter(
                {
                    c.strip().split(" ")[1]: int(c.strip().split(" ")[0])
                    for c in s.split(",")
                }
            )
        if union < bag:
            sum_1 += int(g.strip().split(" ")[-1])
        sum_2 += reduce(mul, union.values(), 1)
    print(sum_1)
    print(sum_2)


ls = load_input_lines(2023, 2)
p1_2(ls)
