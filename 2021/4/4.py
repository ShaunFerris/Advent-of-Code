#process testing dataset
with open('testinput.txt', 'r') as f:
    test_boards_data = [row.strip() for row in f.readlines()]
    test_numbers = [int(num) for num in test_boards_data.pop(0).split(',')]

#process real data
with open('testinput.txt', 'r') as f:
    boards_data = [row.strip() for row in f.readlines()]
    numbers = [int(num) for num in boards_data.pop(0).split(',')]

def rows_by_board(bd):
    ''''Takes the boards data and processes it into a dictionary where keys are
    numbered bingo boards and values are lists of the rows, processed to be lists
    of integers. Each board has 5 rows.'''

    n_boards = int(len(bd) / 6)
    rows = {n: [] for n in range(1, n_boards + 1)}
    board_counter = 0
    for i in bd:
        if i == '':
            board_counter += 1
            continue
        else:
            rows[board_counter].append([int(num) for num in i.split(' ') if num != ''])
    return rows

def columns_by_board(rows):
    '''Takes the output of rows_by_board and calculates the corresponding vertical
    columns for each bingo board.'''

    columns = {n: [] for n in range(1, len(rows) + 1)}
    for board, rws in rows.items():
        for rw in rws:
            if rw == rws[0]:
                for top_num in rw:
                    columns[board].append([top_num])
            else:
                for index, num in enumerate(rw):
                    columns[board][index].append(num)
    return columns

rows = rows_by_board(test_boards_data)
cols = columns_by_board(rows)
print(f'Rows are:\n{rows}\nColumns are:\n{cols}')