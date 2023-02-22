const fs = require('fs');
const input = fs.readFileSync('input.txt', 'utf-8').split('\n');

function getSequence(elf) {
    const sections = elf.split('-').map(Number);
    return Array.from({ length: sections[1] - sections[0] + 1 }, (_, i) => i + sections[0]);
}

function isSubsequence(seqA, seqB) {
    if (seqA.length < seqB.length) {
        [seqA, seqB] = [seqB, seqA];
    }
    seqA = new Set(seqA);
    seqB = new Set(seqB);
    return seqB.size === new Set([...seqA].filter(x => seqB.has(x))).size;
}

function countFullOverlaps(elfAssignments) {
    let count = 0;
    for (const pair of elfAssignments) {
        const [elf1, elf2] = pair.split(',');
        const [seq1, seq2] = [getSequence(elf1), getSequence(elf2)];
        if (isSubsequence(seq1, seq2)) {
            count++;
        }
    }
    return count;
}

console.log(countFullOverlaps(input));

// Problem part 2

function countInclusions(elfAssignments) {
    let count = 0;
    for (const pair of elfAssignments) {
        const [elf1, elf2] = pair.split(',');
        const [seq1, seq2] = [getSequence(elf1), getSequence(elf2)];
        for (const area of seq1) {
            if (seq2.includes(area)) {
                count++;
                break;
            }
        }
    }
    return count;
}

console.log(countInclusions(input));
