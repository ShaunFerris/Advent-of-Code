with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]

test_key = {"red": 12, "green": 13, "blue": 14}


def get_game_id(game):
    return game.split(":")[0].split()[1]


def amounts_by_game(game):
    rounds = [item.split(",") for item in game.split(":")[1].split(";")]
    raw = [item for sublist in rounds for item in sublist]
    return raw


def is_legal(game, key):
    for item in amounts_by_game(game):
        if int(item.split()[0]) > key[item.split()[-1]]:
            return False
    return True


def sum_of_legal_games(input_data, key):
    sum = 0
    for game in input_data:
        if is_legal(game, key):
            sum += int(get_game_id(game))
    return sum


print(sum_of_legal_games(lines, test_key))
