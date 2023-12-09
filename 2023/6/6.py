import re

with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]


def process_race_data(raw_data):
    return re.findall("\d+", raw_data[1])


print(process_race_data(lines))
