const fs = require('fs');

// Reading testing data
const testInstructions = fs.readFileSync('test.txt', 'utf8')
    .split('\n')
    .map(line => line.trim());

// Reading actual data
const instructions = fs.readFileSync('input.txt', 'utf8')
    .split('\n')
    .map(line => line.trim());

function xyDisplacement(instructions) {
    let depth = 0;
    let position = 0;

    for (let i = 0; i < instructions.length; i++) {
        const action = instructions[i].split();

        if (action[0] === 'forward') {
            position += parseInt(action[1]);
        } else if (action[0] === 'up') {
            depth -= parseInt(action[1]);
        } else if (action[0] === 'down') {
            depth += parseInt(action[1]);
        }
    }

    return [depth, position, depth * position];
}

console.log(xyDisplacement(instructions));

function aimXyDisplacement(instructions) {
    let aim = 0;
    let depth = 0;
    let position = 0;

    for (let i = 0; i < instructions.length; i++) {
        const action = instructions[i].split();

        if (action[0] === 'up') {
            aim -= parseInt(action[1]);
        } else if (action[0] === 'down') {
            aim += parseInt(action[1]);
        } else if (action[0] === 'forward') {
            position += parseInt(action[1]);
            depth += aim * parseInt(action[1]);
        }
    }

    return [depth, position, depth * position];
}

console.log(aimXyDisplacement(instructions));
