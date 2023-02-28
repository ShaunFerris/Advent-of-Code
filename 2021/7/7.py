test = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

with open('input.txt', 'r') as f:
    positions = [int(p) for p in f.read().split(',')]

def map_positions(posi_list):
    '''Takes the list of submarine positions and organises it into
    a dictionary of each possible position, from 0 to the max, with
    the values for each being the number of subs at that position.'''

    return {posi: posi_list.count(posi) for posi in range(0, max(posi_list) + 1)}

def calc_convergence(map):
    '''Takes the mapped positions of all the subs and iterates
    through, calculating the fuel that would be spent to move all subs
    to the current position. Returns which position to converge on for
    the lowest fuel consumption.'''

    destination_by_fuel_cost = {}
    for destination in map.keys():
        for start, count in map.items():
            if start == destination:
                continue
            else:
                distance = abs(start - destination)
                fuel_cost = distance * count
                destination_by_fuel_cost[destination] = destination_by_fuel_cost.get(destination, 0) + fuel_cost
    return destination_by_fuel_cost

map = map_positions(positions)
convergence = calc_convergence(map)
print(min(convergence.values()))