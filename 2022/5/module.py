import re

def parse_instructions(line):
    pieces = line.split()
    quant, start, end = int(pieces[1]), int(pieces[3]), int(pieces[5])
    return(quant, start, end)

def move_crate(line, crate_map):
    quant, start, end = parse_instructions(line)
    for _ in range(quant):
        try:
            crate = crate_map[start].pop(-1)
            crate_map[end].append(crate)
        except:
            continue
    return crate_map

def construct_map(input):
    file = open(input)
    data = [re.sub(r'\n', '', i) for i in file.readlines()]
    crate_map1 = {k + 1 : [] for k in range(9)}
    map_data = data[0 : 8]
    for i in map_data:
        crate_names = (i[1: :4])
        for index, c in enumerate(crate_names):
            if c != ' ':
                crate_map1[index + 1].append(c)

    for list in crate_map1.values():
        list = list.reverse()
    return crate_map1

def arrange_crates(input):
    crate_map = construct_map(input)
    file = open(input)
    data = [i.strip() for i in file.readlines()]
    instructions = data[10 :]
    for line in instructions:
        move_crate(line, crate_map)
    return crate_map

def top_crates(crate_map):
    crates_at_top = ''
    for v in crate_map.values():
        crates_at_top += v[-1]
    return crates_at_top

def move_multi(line, crate_map):
    quant, start, end = parse_instructions(line)
    crate_group = (crate_map[start])[(quant * -1):]
    del (crate_map[start])[(quant * -1):]
    for _ in crate_group:
        crate_map[end].append(_)
    return crate_map

def multi_arrange_crates(input):
    crate_map = construct_map(input)
    file = open(input)
    data = [i.strip() for i in file.readlines()]
    instructions = data[10 :]
    for line in instructions:
        move_multi(line, crate_map)
    return crate_map