const fs = require('fs');

const data = fs.readFileSync('input.txt', 'utf8').split('\n');

function calorie_counter(lines, number_of_elves = 1) {
    let elves = [];
    let curr_elf = 0;
    for (let i = 0; i < lines.length; i++) {
        const cal = lines[i];
        if (cal !== '') {
            curr_elf += parseInt(cal);
        } else {
            elves.push(curr_elf);
            curr_elf = 0;
        }
    }
    elves = elves.sort((a, b) => b - a);
    const output_elves = [];
    for (let i = 0; i < number_of_elves; i++) {
        output_elves.push(elves[i]);
    }
    if (number_of_elves === 1) {
        return output_elves[0];
    } else {
        return output_elves.reduce((total, current) => total + current, 0);
    }
}

console.log(calorie_counter(data, 3));
