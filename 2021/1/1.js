const fs = require('fs');

// Reading testing data
const testMeasurements = fs.readFileSync('test.txt', 'utf8')
    .split('\n')
    .map(line => parseInt(line));

// Reading actual data
const measurements = fs.readFileSync('input.txt', 'utf8')
    .split('\n')
    .map(line => parseInt(line));

function oneDataPointDelta(measurements) {
    let depthDelta = { increase: 0, decrease: 0 };
    let currentDepth = 0;

    for (let i = 0; i < measurements.length; i++) {
        const measurement = measurements[i];

        if (currentDepth === 0) {
            currentDepth = measurement;
            continue;
        } else if (measurement > currentDepth) {
            depthDelta.increase++;
            currentDepth = measurement;
        } else if (measurement < currentDepth) {
            depthDelta.decrease++;
            currentDepth = measurement;
        }
    }

    return depthDelta;
}

function tresDataPointDelta(measurements) {
    const windowSums = [];

    for (let i = 2; i < measurements.length; i++) {
        windowSums.push(measurements[i - 2] + measurements[i - 1] + measurements[i]);
    }

    return oneDataPointDelta(windowSums);
}

console.log(tresDataPointDelta(measurements));
