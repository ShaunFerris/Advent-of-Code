from typing import List, Tuple

with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]

with open("subset.txt") as f:
    test_lines = [f.strip() for f in f.readlines()]


PIPE_SYMBOLS = ["|", "-", "L", "J", "7", "F"]

PIPE_DIRECTIONS = {
    "|": ("N", "S"),
    "-": ("E", "W"),
    "L": ("N", "E"),
    "J": ("N", "W"),
    "7": ("W", "S"),
    "F": ("S", "E"),
}

MOVEMENTS = {
    "N": lambda x, y: (x, y - 1),
    "S": lambda x, y: (x, y + 1),
    "E": lambda x, y: (x + 1, y),
    "W": lambda x, y: (x - 1, y),
}


def get_map_matrix(input_data: List[str]) -> List[List[str]]:
    return [list(line) for line in input_data]


def get_starting_coord(map_matrix: List[List[str]]) -> Tuple[int]:
    for y, line in enumerate(map_matrix):
        for x, char in enumerate(line):
            if char == "S":
                return (x, y)


def map_loop(input_data: List[str]) -> List[Tuple[int]]:
    """
    Takes the raw input data and generates the map matrix.
    Find the starting coord in the map matrix, then follow the loop and add the
    coords of each point to the output.
    """
    map_matrix = get_map_matrix(input_data)
    starting_coord = get_starting_coord(map_matrix)
    for direction, operation in MOVEMENTS.items():
        check_coords = operation(*starting_coord)
        check_x, check_y = check_coords
        if map_matrix[check_y][check_x] not in PIPE_SYMBOLS:
            continue
        else:
            pass
