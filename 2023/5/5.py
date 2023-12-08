from typing import List, Tuple, Dict

with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]

with open("subset.txt") as f:
    test_lines = [f.strip() for f in f.readlines()]


def pull_seeds(almanac: List[str]) -> Tuple[List[int], List[str]]:
    # pull seeds and process them, return seeds and almanac without seeds for further processing
    seeds_string = almanac.pop(0)
    proccesed_seeds = [int(seed) for seed in seeds_string.split(":")[1].split()]
    return proccesed_seeds, almanac


def process_almanac(seedless_almanac: List[str]) -> Dict[str, List[List]]:
    processed_almanac = {}
    for index, entry in enumerate(seedless_almanac):
        if seedless_almanac[index - 1] == "":
            processed_almanac[entry] = []
            for i in range(index + 1, len(seedless_almanac)):
                if seedless_almanac[i] == "":
                    break
                else:
                    processed_almanac[entry].append(seedless_almanac[i].split())
    return processed_almanac


def find_location(seed: int, processed_almanac: Dict[str, List[List]]) -> int:
    next = seed
    for map in processed_almanac.values():
        for index, entry in enumerate(map):
            dest_start, source_start, range_length = (
                int(entry[0]),
                int(entry[1]),
                int(entry[2]),
            )
            if (
                next not in range(source_start, source_start + range_length)
                and index == len(map) - 1
            ):
                next = next
                break
            if next not in range(source_start, source_start + range_length):
                continue
            else:
                next = dest_start + (next - source_start)
                break
    return next


def get_all_seed_locations(almanac: List[str]):
    seed_locations = []
    seeds, seedless_almanac = pull_seeds(almanac)
    processed_almanac = process_almanac(seedless_almanac)
    for seed in seeds:
        seed_locations.append(find_location(seed, processed_almanac))
    return seed_locations


print(f"Part One: {min(get_all_seed_locations(lines))}")
