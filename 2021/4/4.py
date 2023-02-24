from copy import deepcopy

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

def winning_seqs(bd):
    '''Combines the column and row parsing functions to build a dictionary of all the winning
    sequences by board.'''

    rows = rows_by_board(bd)
    cols = columns_by_board(rows)
    for board, rws in rows.items():
        for rw in rws:
            cols[board].append(rw)
    winners = cols
    return winners

def board_states(ws):
    '''Creates a copy of the winning sets dictionary with 0's in place of the board numbers.
    Intention is to have these switched to 1's to mark called numbers, and indicate the winning
    board without working directly in the organised board data dict from winning sets.'''

    states = deepcopy(ws)
    for seqs in states.values():
        for seq in seqs:
            for i in range(len(seq)):
                seq[i] = 0
    return states

def check_number(called_num, winning_seqs, board_states):
    '''This takes a called bingo number, the winning sequences dictionary,
    and the board state tracking dictionary. It marks the position of the called number,
    and returns the marked state tracking dict.'''

    for board, seqs in winning_seqs.items():
        for index_1, seq in enumerate(seqs):
            for index_2, num in enumerate(seq):
                if num == called_num:
                    board_states[board][index_1][index_2] = 1
    return board_states


processed_data = winning_seqs(test_boards_data)
print(processed_data)
tracker = board_states(processed_data)
print('\n', tracker)
print('\n', check_number(22, processed_data, tracker))