with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]


test_lines = lines[0:3:1]
example = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def get_symbol_coords(input_data):
    symbol_key = ["*", "%", "$", "@", "#", "=", "/", "+", "-", "&"]
    coords = []
    for line_index, line in enumerate(input_data):
        for char_index, char in enumerate(line):
            if char in symbol_key:
                coords.append((line_index, char_index))
    return coords


def get_edges(symbol_coord):
    line, position = int(symbol_coord[0]), int(symbol_coord[1])
    edges = []
    for i in range((line - 1), (line + 2)):
        for j in range((position - 1), (position + 2)):
            if i == line and j == position:
                continue
            elif i >= 0 and j >= 0:
                edges.append((i, j))
    return edges


def resolve_number(input_data, edge_coord):
    line, position = int(edge_coord[0]), int(edge_coord[1])
    target = input_data[line]
    number = ""
    if target[position].isdigit():
        for i in target[position::-1]:
            if i.isdigit():
                number = i + number
            else:
                break
        for i in target[position + 1 :]:
            if i.isdigit():
                number += i
            else:
                break
    return number


def search_edges(input_data, edge_list):
    hit_numbers = []
    last_hit = None
    for coord in edge_list:
        if coord[0] < len(input_data):
            hit = resolve_number(input_data, coord)
            if hit != last_hit:
                last_hit = hit
                if hit.isdigit():
                    hit_numbers.append(int(hit))
    return hit_numbers


def solve(input_data):
    total = 0
    symbol_coords = get_symbol_coords(input_data)
    for symbol in symbol_coords:
        edge_list = get_edges(symbol)
        nums = search_edges(input_data, edge_list)
        total += sum(nums)
    return total


print(f"Part One: {solve(lines)}")
