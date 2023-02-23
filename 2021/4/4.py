#process testing dataset
with open('testinput.txt', 'r') as f:
    test_boards_data = [row.strip() for row in f.readlines()]
    test_numbers = [int(num) for num in test_boards_data.pop(0).split(',')]

#process real data
with open('testinput.txt', 'r') as f:
    boards_data = [row.strip() for row in f.readlines()]
    numbers = [int(num) for num in boards_data.pop(0).split(',')]

def boards_array(bd):
    n_boards = int(len(bd) / 6)
    winning_rows = {n: [] for n in range(1, n_boards + 1)}
    board_counter = 0
    for i in bd:
        if i == '':
            board_counter += 1
            continue
        else:
            winning_rows[board_counter].append([int(num) for num in i.split(' ') if num != ''])
    return winning_rows

print(boards_array(test_boards_data))