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
        (4, 1): 6,  # four of a kind etc...
        (3, 2): 5,  # full house
        (3, 1, 1): 4,
        (2, 2, 1): 3,
        (2, 1, 1, 1): 2,
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
        self.hand_type = self.get_hand_type(hand)

    def process_hand(line: str) -> Tuple[str, int]:
        return (line.split()[0], int(line.split()[1]))

    def get_hand_type(self, processed_hand: Tuple[str, int]) -> int:
        return self.hand_types[tuple(Counter(processed_hand[0]).values())]
