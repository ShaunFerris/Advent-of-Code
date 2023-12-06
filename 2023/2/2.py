with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]

test_key = {"red": 12, "green": 13, "blue": 14}
test_game = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"


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


print(f"Part One: {sum_of_legal_games(lines, test_key)}")


def min_by_color(game):
    color_map = {"blue": 0, "red": 0, "green": 0}
    for item in amounts_by_game(game):
        if int(item.split()[0]) > color_map[item.split()[-1]]:
            color_map[item.split()[-1]] = int(item.split()[0])
    return color_map


def power_of_game(game):
    out = 1
    for i in min_by_color(game).values():
        out *= i
    return out


def sum_of_game_powers(input_data):
    sum = 0
    for game in input_data:
        sum += power_of_game(game)
    return sum


print(f"Part Two: {sum_of_game_powers(lines)}")
