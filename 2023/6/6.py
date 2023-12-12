import re
from typing import List, Tuple
from functools import reduce

with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]

with open("subset.txt") as f:
    test_lines = [f.strip() for f in f.readlines()]


def process_race_data(raw_data: List[str]) -> List[Tuple[int]]:
    time_line, distance_line = raw_data
    times = re.findall("\d+", time_line)
    distances = re.findall("\d+", distance_line)
    processed = []
    for i in range(len(times)):
        processed.append((int(times[i]), int(distances[i])))
    return processed


def get_number_of_wins(race: Tuple[int]) -> int:
    wins = 0
    time, record_distance = race
    for i in range(1, time + 1):
        speed = i
        travel_time = time - i
        distance = travel_time * speed
        if distance > record_distance:
            wins += 1
    return wins


def product_of_winning_strats(raw_data: List[str]) -> List[Tuple[int]]:
    processed_race_data = process_race_data(raw_data)
    winning_strats_by_race = []
    for race in processed_race_data:
        winning_strats_by_race.append(get_number_of_wins(race))
    return reduce(lambda a, b: a * b, winning_strats_by_race)


print(f"Part One: {product_of_winning_strats(lines)}")


def process_single_race_data(raw_data: List[str]) -> Tuple[int]:
    time_line, distance_line = raw_data
    time = ("").join(re.findall("\d+", time_line))
    distance = ("").join(re.findall("\d+", distance_line))
    return (int(time), int(distance))


processed = process_single_race_data(lines)
print(processed)
print(f"Part Two: {get_number_of_wins(processed)}")
