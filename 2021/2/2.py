#Test data
with open('test.txt', 'r') as f:
    test_instructions = [i.strip() for i in f.readlines()]

#Actual data
with open('input.txt', 'r') as f:
    instructions = [i.strip() for i in f.readlines()]

def xy_displacement(instructions):
    depth = 0
    position = 0
    for action in instructions:
        action = action.split()
        if action[0] == 'forward':
            position += int(action[1])
        elif action[0] == 'up':
            depth -= int(action[1])
        elif action[0] == 'down':
            depth += int(action[1])
    return depth, position, depth * position

print(xy_displacement(instructions))