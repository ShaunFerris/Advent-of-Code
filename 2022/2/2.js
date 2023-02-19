const fs = require('fs');

const data = fs.readFileSync('input.txt', 'utf8').split('\n');

const GUIDE_KEY = {'A': 'R', 'X': 'R', 'B': 'P', 'Y': 'P', 'C': 'S', 'Z': 'S'};
const RPS_RULES = {'R': 'S','P': 'R', 'S': 'P'};
const RPS_REVERSED = Object.fromEntries(Object.entries(RPS_RULES).map(([k, v]) => [v, k]));
const SCORING = {'R': 1, 'P': 2, 'S': 3, 'W': 6, 'L': 0, 'D': 3};

function score_calc_A(opp, player) {
    let score = SCORING[player];
    if (player === opp) {
        score += SCORING['D'];
    }
    if (RPS_RULES[player] === opp) {
        score += SCORING['W'];
    }
    return score;
}

function tournament_A(data) {
    let total_score = 0;
    for (let match of data) {
        match = match.trim().split(' ');
        const opp = GUIDE_KEY[match[0]];
        const player = GUIDE_KEY[match[1]];
        total_score += score_calc_A(opp, player);
    }
    return total_score;
}

console.log(tournament_A(data));

function score_calc_B(opp, result) {
    let score = 0;
    if (result === 'X') {
        score += SCORING[RPS_RULES[opp]];
    } else if (result === 'Y') {
        score += SCORING[opp] + SCORING['D'];
    } else if (result === 'Z') {
        score += SCORING[RPS_REVERSED[opp]] + SCORING['W'];
    }
    return score;
}

function tournament_B(data) {
    let total_score = 0;
    for (let match of data) {
        match = match.trim().split(' ');
        const opp = GUIDE_KEY[match[0]];
        const result = match[1];
        total_score += score_calc_B(opp, result);
    }
    return total_score;
}

console.log(tournament_B(data));
