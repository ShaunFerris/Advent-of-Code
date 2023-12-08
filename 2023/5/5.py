from typing import List, Tuple

with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]

with open("subset.txt") as f:
    test_lines = [f.strip() for f in f.readlines()]


def pull_seeds(almanac: List[str]) -> Tuple[List[int], List[str]]:
    # pull seeds and process them, return seeds and almanac without seeds for further processing
    seeds_string = almanac.pop(0)
    proccesed_seeds = [int(seed) for seed in seeds_string.split(":")[1].split()]
    return proccesed_seeds, almanac


def process_almanac(seedless_almanac: List[str]):
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


processed_test = pull_seeds(test_lines)[1]
print(process_almanac(processed_test))
