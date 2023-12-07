with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]


test_lines = lines[0:3:1]


def get_symbol_coords(input_data):
    symbol_key = ["*", "%", "$", "@", "#", "=", "/"]
    coords = []
    for line_index, line in enumerate(input_data):
        for char_index, char in enumerate(line):
            if char in symbol_key:
                coords.append((line_index, char_index))
    return coords


print(get_symbol_coords(test_lines))


test_snippet = "...2345........"


def resolve_number(snippet, index):
    number = ""
    if snippet[index].isdigit():
        for i in snippet[index::-1]:
            if i.isdigit():
                number = i + number
        for i in snippet[index + 1 :]:
            if i.isdigit():
                number += i
    return number


print(resolve_number(test_snippet, 5))


"""
If a given edge around the symbol coordinate in on the same line then we know that it terminates
at thee symbol so it can be resolved. 

For lines above and below the symbol coord we should iterate left to right and only resolve
and append the number if it was preceeded by a period
"""

test_snippet_2 = ["...1234...", ".......#.."]


def get_edges(symbol_coord):
    line, position = int(symbol_coord[0]), int(symbol_coord[1])
    edges = []
    for i in range((line - 1), (line + 1)):
        for j in range((position - 1), (position + 1)):
            print(i, j)
            if i > 0 and j > 0:
                edges.append((i, j))
    return edges


# print(get_edges(("1", "1")))


def get_adjacency(input_data):
    symbol_coords_list = get_symbol_coords(input_data)
    symbol_adjacencies = {symbol_coord: [] for symbol_coord in symbol_coords_list}
    for i in symbol_coords_list:
        curr_line, curr_position = i[0], i[1]
        # check three grid positions in line above if not first line
        if int(curr_line) > 0:
            if input_data[curr_line - 1][curr_position - 1].isdigit():
                symbol_adjacencies[i].append((curr_line - 1, curr_position - 1))
    return symbol_adjacencies


# print(get_adjacency(test_lines))
