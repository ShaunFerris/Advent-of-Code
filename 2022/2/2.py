with open('input.txt', 'r') as f:
    data = f.readlines()

GUIDE_KEY = {'A': 'R', 'X': 'R', 'B': 'P', 'Y': 'P', 'C': 'S', 'Z': 'S'}
RPS_RULES = {'R': 'S','P': 'R', 'S': 'P'}
RPS_REVERSED = {v: k for k, v in RPS_RULES.items()}
SCORING = {'R': 1, 'P': 2, 'S': 3, 'W': 6, 'L': 0, 'D': 3}


def score_calc_A(opp, player):
    score = SCORING[player]
    if player == opp:
        score += SCORING['D']
    if RPS_RULES[player] == opp:
        score += SCORING['W']
    return score

def tournament_A(data):
    total_score = 0
    for match in data:
        match = match.split()
        opp, player, = GUIDE_KEY[match[0]], GUIDE_KEY[match[1]]
        total_score += score_calc_A(opp, player)
    return total_score

print(tournament_A(data))

def score_calc_B(opp, result):
    score = 0
    if result == 'X': #loss
        score += SCORING[RPS_RULES[opp]]
    elif result == 'Y': #draw
        score += SCORING[opp] + SCORING['D']
    elif result == 'Z': #win
        score += SCORING[RPS_REVERSED[opp]] + SCORING['W']
    return score

def tournament_B(data):
    total_score = 0
    for match in data:
        match = match.split()
        opp, result = GUIDE_KEY[match[0]], match[1]
        total_score += score_calc_B(opp, result)
    return total_score

print(tournament_B(data))