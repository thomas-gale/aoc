import re
from collections import defaultdict
from aoc.util import load_input_lines


def p1_2(ls):
    nums = defaultdict(dict)
    syms = defaultdict(dict)
    for i, l in enumerate(ls):
        for m in re.finditer(r"\d+", l):
            nums[i][m.start()] = m
        for m in re.finditer(r"[^.\d]+", l):
            syms[i][m.start()] = m

    sum_p1 = 0
    sum_p2 = 0
    gears = defaultdict(list)
    for s_rowi, s_row in syms.items():
        # Check the current, previous, and next rows for adjacent numbers
        for n_rowi in range(s_rowi - 1, s_rowi + 2):
            if n_rowi in nums:
                for _, num in nums[n_rowi].items():
                    for _, sym in s_row.items():
                        sym_start, sym_end = sym.span()
                        num_start, num_end = num.span()
                        # Skip if the number is not adjacent to the symbol
                        if (sym_start + 1 < num_start) or (sym_end - 1 > num_end):
                            continue
                        if sym.group() == "*":
                            gears[(s_rowi, sym_start, sym.group())].append(
                                int(num.group())
                            )
                        sum_p1 += int(num.group())
    for gear in gears.values():
        if len(gear) == 2:
            sum_p2 += gear[0] * gear[1]

    print(sum_p1)
    print(sum_p2)


ls = load_input_lines(2023, 3)
p1_2(ls)
