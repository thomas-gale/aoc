import re
from aoc.util import load_input_lines


def p1(ls):
    sum = 0
    for l in ls:
        digits = [int(c) for c in l if c.isdigit()]
        sum += digits[0] * 10 + digits[-1]
    print(sum)


nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def p2(ls):
    sum = 0
    for l in ls:
        # Get digit matches and locations (same as part 1)
        digits = {i: int(c) for i, c in enumerate(l) if c.isdigit()}

        # Get string num matches and locations
        for n in nums.keys():
            for m in re.finditer(n, l):
                digits[m.span()[0]] = nums[n]

        sk = sorted(digits.keys())
        sum += digits[sk[0]] * 10 + digits[sk[-1]]

    print(sum)


ls = load_input_lines(2023, 1)
p1(ls)
p2(ls)
