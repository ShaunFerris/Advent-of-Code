from collections import Counter
from typing import List, Tuple, Dict

with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]

with open("subset.txt") as f:
    test_lines = [f.strip() for f in f.readlines()]


class Hand:
    # Lookup for tuple representations of handtypes, better hand higher value
    hand_types: Dict[Tuple, int] = {
        (5,): 7,  # five of a kind
        (1, 4): 6,  # four of a kind etc...
        (2, 3): 5,  # full house
        (1, 1, 3): 4,
        (1, 2, 2): 3,
        (1, 1, 1, 2): 2,
        (1, 1, 1, 1, 1): 1,
    }

    # Lookup for  rankings of individual cards for tie breaks
    card_types: Dict[str, int] = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
    }

    def __init__(self, hand: str):
        self.hand, self.bid = hand.split()
        self.bid = int(self.bid)
        self.hand_type = self.get_hand_type()

    def __gt__(self, other) -> bool:
        if self.hand_type > other.hand_type:
            return True
        elif self.hand_type == other.hand_type:
            for i in range(len(self.hand)):
                if self.hand[i] == other.hand[i]:
                    continue
                else:
                    return (
                        self.card_types[self.hand[i]] > self.card_types[other.hand[i]]
                    )
        else:
            return False

    def __eq__(self, other) -> bool:
        if self.hand_type == other.hand_type:
            return True
        else:
            return False

    def get_hand_type(self) -> int:
        return self.hand_types[tuple(sorted(Counter(self.hand).values()))]


class HandWithJoker(Hand):
    card_types = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "J": 1,
    }

    def get_hand_type(self) -> int:
        if "J" not in self.hand:
            return self.hand_types[tuple(sorted(Counter(self.hand).values()))]
        else:
            c = Counter(self.hand)
            jokers_count = c["J"]
            if c["J"] == 5:
                return self.hand_types[(5,)]
            del c["J"]
            highest_values = list(sorted(c.values(), reverse=True))
            for i in range(len(highest_values)):
                while jokers_count and highest_values[i] < 5:
                    highest_values[i] += 1
                    jokers_count -= 1
            return self.hand_types[tuple(sorted(highest_values))]


def solve(input_data: List[str], joker_rule: bool) -> int:
    if joker_rule:
        hands = [HandWithJoker(line) for line in input_data]
    else:
        hands = [Hand(line) for line in input_data]
    hands.sort()

    winnings = 0
    for index, hand in enumerate(hands):
        winnings += (index + 1) * hand.bid
    return winnings


print(f"Part One: {solve(lines, joker_rule=False)}")
print(f"Part Two: {solve(lines, joker_rule=True)}")
