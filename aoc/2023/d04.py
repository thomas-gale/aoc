import re
from collections import defaultdict
from aoc.util import load_input_lines


def p1(ls):
    score = 0
    for l in ls:
        nums, wins = map(str.split, l.split("|"))
        intersection = set(nums) & set(wins)
        if len(intersection) > 0:
            score += 2 ** (len(intersection) - 1)
    return score


def p2(ls):
    cards = [1] * len(ls)
    for i, l in enumerate(ls):
        nums, wins = map(str.split, l.split("|"))
        n = len(set(nums) & set(wins))
        for j in range(i + 1, min(i + 1 + n, len(ls))):
            cards[j] += cards[i]
    return sum(cards)


# ls = load_input_lines(2023, 4, "t")
ls = load_input_lines(2023, 4)
print(p1(ls), p2(ls))
