from typing import Tuple, List, Dict

with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]

example = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


def process_card(card_line: str) -> Dict[str, List[int]]:
    return {
        "game_id": int(card_line.split(":")[0].split(" ")[-1]),
        "winning": [int(i) for i in card_line.split(":")[1].split("|")[0].split()],
        "held": [int(i) for i in card_line.split(":")[1].split("|")[1].split()],
    }


def total_score_of_card(card_line: str) -> int:
    total = 0
    processed = process_card(card_line)
    for i in processed["held"]:
        if i in processed["winning"]:
            if total == 0:
                total += 1
            else:
                total *= 2
    return total


def solve(input_data: List[str]) -> int:
    out = 0
    for line in input_data:
        out += total_score_of_card(line)
    return out


print(f"Part One: {solve(lines)}")


def wins_by_id(card_line: str) -> Tuple[int, int]:
    game_id, winning, held = process_card(card_line).values()
    number_of_wins = len(set(winning).intersection(set(held)))
    return (game_id, number_of_wins)


def solve_duplicating_cards(input_data: List[str]) -> int:
    counter = {process_card(card)["game_id"]: 1 for card in input_data}
    for card in input_data:
        game_id, number_of_wins = wins_by_id(card)
        for _ in range(counter[game_id]):
            for i in range(game_id + 1, game_id + number_of_wins + 1):
                counter[i] += 1
    return sum(counter.values())


print(f"Part Two: {solve_duplicating_cards(lines)}")
