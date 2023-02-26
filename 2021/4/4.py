from copy import deepcopy

#process testing dataset
with open('testinput.txt', 'r') as f:
    test_boards_data = [row.strip() for row in f.readlines()]
    test_numbers = [int(num) for num in test_boards_data.pop(0).split(',')]

#process real data
with open('input.txt', 'r') as f:
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

def play_game(numbers, board_data):
    '''Plays the bingo game until the first winning board is found, returns a version of the 
    winning sequence dictionary with the winning sequence removed,
    and the final number that was called as a tuple.'''
    
    processed_data = winning_seqs(board_data)
    tracker = board_states(processed_data)
    for index_1, num in enumerate(numbers):
        tracker = check_number(num, processed_data, tracker)
        for board, seqs in tracker.items():
            for index_2, seq in enumerate(seqs):
                if sum(seq) == 5:
                    winner = processed_data[board][index_2]
                    called_seq = numbers[:index_1]
                    return winner, num, called_seq

def find_winning_score(numbers, board_data):
    '''Main function for problem part one. Takes the boards data and numbers and
    plays the game, then calculates the score from the winnning board by summing
    the unmarked numbers and multiplying by the final number called.'''

    winning_seq, final_num, called_seq = play_game(numbers, board_data)
    original_boards = rows_by_board(board_data)
    #import pdb
    #pdb.set_trace()
    for board, seqs in original_boards.items():
        if winning_seq in seqs:
            original_boards[board].remove(winning_seq)
            winning_sum = 0
            for seq in seqs:
                for num in seq:
                    winning_sum += num if num not in called_seq else 0
            return winning_sum * final_num


print(find_winning_score(numbers, boards_data))