with open('input.txt', 'r') as f:
    rucksack_items = []
    for line in f:
        rucksack_items.append(line.strip())

def get_priority(characters):
        ascii = [ord(c) for c in characters]
        priorities = []
        for a in ascii:
            if a > 96:
                priorities.append(a - 96)
            elif a < 91:
                priorities.append(a - 38)
        return sum(priorities)


def rucksack_priorities(rucksack_items):
    total = 0
    for item in rucksack_items:
        compartment_1, compartment_2 = \
            set(item[: len(item) // 2]), set(item[len(item) // 2 :])
        duplicates = compartment_1.intersection(compartment_2)
        total += get_priority(duplicates)
    return total

print(rucksack_priorities(rucksack_items))

def badges(rucksack_items):
    pass