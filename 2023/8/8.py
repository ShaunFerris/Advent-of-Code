from typing import List, Tuple, Dict
from math import lcm
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
            ("").join(re.findall(r"[A-Z1-9]", item))
            for item in processed_line[1].split(",")
        )
        for processed_line in (line.split("=") for line in raw_nav_map)
    }

    return (navigation_instructions, nav_map)


def chart_course(input_data: List[str]) -> int:
    """
    Calculate the number of steps from node AAA to node ZZZ following the instructions in the
    provided navigation loop
    Arg: Raw input data as a list of lines
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


def simulataneous_chart_course(input_data: List[str]) -> int:
    """
    Calculate the number of steps taken when all courses starting from nodes that end in "A" are
    followed simultaneously until all courses are on a node ending in "Z"
    Arg: Raw input data
    Returns: Number of steps taken between nodes
    """
    nav_instructions, nav_map = process_nav_map(input_data=input_data)
    nav_loop = NavigationLoop(nav_instructions)
    instruction_key = {"R": 1, "L": 0}
    step_count = 0
    current_nodes = [node for node in nav_map.keys() if node[-1] == "A"]
    steps_to_hit = {
        index: 0 for index, node in enumerate(current_nodes) if node[-1] == "A"
    }
    for instruction in nav_loop:
        current_nodes = [
            nav_map[node][instruction_key[instruction]] for node in current_nodes
        ]
        step_count += 1
        for idx, node in enumerate(current_nodes):
            if node[-1] == "Z":
                steps_to_hit[idx] = (
                    step_count if steps_to_hit[idx] == 0 else steps_to_hit[idx]
                )
        if all(step_count != 0 for step_count in steps_to_hit.values()):
            break
    return lcm(*steps_to_hit.values())


print(f"Part Two:{simulataneous_chart_course(lines)}")
