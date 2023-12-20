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
