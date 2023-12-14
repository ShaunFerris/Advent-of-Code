from typing import List, Tuple
import re

with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]

with open("subset.txt") as f:
    test_lines = [f.strip() for f in f.readlines()]


class navigation_loop:
    def __init__(self, navigation_instructions: str):
        self.instructions = navigation_instructions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_instruction = self.instructions[self.index]

        if self.index + 1 > len(self.instructions) - 1:
            self.index = 0
        else:
            self.index += 1
        return current_instruction


test_instructions = test_lines[0]


def process_nav_map(input_data: List[str]):
    """
    Process the input data. Arg: raw input data as a list of lines.
    Returns: a tuple with the navigation instruction string at idx 0 and a dict that maps nodes
    to child nodes at idx 1
    """
    navigation_instructions = input_data[0]
    raw_nav_map = input_data[2:]
    nav_map = {
        processed_line[0]: tuple(
            ("").join(re.findall(r"[A-Z]", item))
            for item in processed_line[1].split(",")
        )
        for processed_line in (line.split("=") for line in raw_nav_map)
    }

    return (navigation_instructions, nav_map)


print(process_nav_map(test_lines))
