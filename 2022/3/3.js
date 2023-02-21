const fs = require('fs');

const inputFilePath = 'input.txt';
const rucksack_items = fs.readFileSync(inputFilePath, 'utf-8').trim().split('\n');

function get_priority(characters) {
    let ascii = [];
    for (let i = 0; i < characters.length; i++) {
        ascii.push(characters.charCodeAt(i));
    }
    let priorities = [];
    for (let i = 0; i < ascii.length; i++) {
        let a = ascii[i];
        if (a > 96) {
            priorities.push(a - 96);
        } else if (a < 91) {
            priorities.push(a - 38);
        }
    }
    return priorities.reduce((acc, val) => acc + val, 0);
}

function rucksack_priorities(rucksack_items) {
    let total = 0;
    for (let i = 0; i < rucksack_items.length; i++) {
        let item = rucksack_items[i];
        let mid = Math.floor(item.length / 2);
        let compartment_1 = new Set(item.substring(0, mid));
        let compartment_2 = new Set(item.substring(mid));
        let duplicates = new Set([...compartment_1].filter(x => compartment_2.has(x)));
        total += get_priority(duplicates);
    }
    return total;
}

console.log(rucksack_priorities(rucksack_items));

function badges(rucksack_items, group_size = 3) {
    let total = 0;
    let group = [];
    for (let i = 0; i < rucksack_items.length; i++) {
        let elf = rucksack_items[i];
        if (group.length < group_size) {
            group.push(new Set(elf));
        }
        if (group.length === group_size) {
            let badge = new Set([...group[0]].filter(x => group[1].has(x) && group[2].has(x)));
            total += get_priority(badge);
            group = [];
        }
    }
    return total;
}

console.log(badges(rucksack_items));
