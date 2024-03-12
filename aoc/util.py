import os
from typing import List


def load_input_lines(year: int, day: int, post: str = "") -> List[str]:
    with open(os.path.join("res", "inputs", str(year), f"{day:02d}{post}.txt")) as f:
        return f.read().splitlines()
