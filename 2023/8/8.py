from typing import List, Tuple, Dict
import re

with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]

with open("subset.txt") as f:
    test_lines = [f.strip() for f in f.readlines()]


class NavigationLoop:
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


def process_nav_map(input_data: List[str]) -> Tuple[str, Dict[str, Tuple[str]]]:
    """
    Process the input data. Arg: raw input data as a list of lines.
    Returns: a tuple with the navigation instruction string at idx 0 and a dict that maps nodes
    to child nodes at idx 1
    """
    navigation_instructions = input_data[0]
    raw_nav_map = input_data[2:]
    nav_map = {
        processed_line[0].strip(): tuple(
            ("").join(re.findall(r"[A-Z]", item))
            for item in processed_line[1].split(",")
        )
        for processed_line in (line.split("=") for line in raw_nav_map)
    }

    return (navigation_instructions, nav_map)


def chart_course(input_data: List[str]) -> int:
    """
    Calculate the number of steps from node AAA to node ZZZ following the instructions in the
    provided navigation loop
    Arg: raw input data as a list of lines
    Returns: Number of steps between nodes as an int
    """
    nav_instructions, nav_map = process_nav_map(input_data=input_data)
    nav_loop = NavigationLoop(nav_instructions)
    instruction_key = {"R": 1, "L": 0}
    current_node = "AAA"
    step_count = 0
    for instruction in nav_loop:
        current_node = nav_map[current_node][instruction_key[instruction]]
        step_count += 1
        if current_node == "ZZZ":
            break
    return step_count


print(f"Part One: {chart_course(lines)}")
