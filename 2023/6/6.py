import re
from typing import List, Tuple

with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]


def process_race_data(raw_data: List[str]) -> List[Tuple[int]]:
    time_line, distance_line = raw_data
    times = re.findall("\d+", time_line)
    distances = re.findall("\d+", distance_line)
    processed = []
    for i in range(len(times)):
        processed.append((times[i], distances[i]))
    return processed


print(process_race_data(lines))
