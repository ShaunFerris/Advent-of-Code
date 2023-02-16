const fs = require('fs');

//Test data
const testBitStrings = fs.readFileSync('test.txt', 'utf8').split('\n').map(str => str.trim()).filter(str => str !== '');

//Actual data
const bitStrings = fs.readFileSync('input.txt', 'utf8').split('\n').map(str => str.trim()).filter(str => str !== '');

function mostCommon(lst) {
  return lst.reduce((a, b, i, arr) => (arr.filter(v => v===a).length >= arr.filter(v => v===b).length ? a : b), null);
}

function gammaRate(data) {
  let bitMap = data[0].split('').map(() => []);
  for (const bitString of data) {
    for (const [indx, bit] of bitString.split('').entries()) {
      bitMap[indx].push(bit);
    }
  }
  const gammaString = bitMap.map(mostCommon).join('');
  const gammaNumber = parseInt(gammaString, 2);
  return [gammaString, gammaNumber];
}

function epsilonRate(data) {
  const mirror = gammaRate(data)[0].split('').map(bit => bit === '1' ? '0' : '1').join('');
  const epsilonNumber = parseInt(mirror, 2);
  return [mirror, epsilonNumber];
}

function oxygenRating(data) {
  let oxygenData = [...data];
  let count = 0;
  while (oxygenData.length > 1) {
    let zeros = 0, ones = 0;
    for (const bitString of oxygenData) {
      if (bitString[count] === '0') {
        zeros += 1;
      } else if (bitString[count] === '1') {
        ones += 1;
      }
    }
    if (zeros > ones) {
      oxygenData = oxygenData.filter(bitString => bitString[count] === '0');
    } else {
      oxygenData = oxygenData.filter(bitString => bitString[count] === '1');
    }
    count += 1;
  }
  const oxygenNumber = parseInt(oxygenData[0], 2);
  return [oxygenData, oxygenNumber];
}

function co2Rating(data) {
  let co2Data = [...data];
  let count = 0;
  while (co2Data.length > 1) {
    let zeros = 0, ones = 0;
    for (const bitString of co2Data) {
      if (bitString[count] === '0') {
        zeros += 1;
      } else if (bitString[count] === '1') {
        ones += 1;
      }
    }
    if (zeros > ones) {
      co2Data = co2Data.filter(bitString => bitString[count] === '1');
    } else {
      co2Data = co2Data.filter(bitString => bitString[count] === '0');
    }
    count += 1;
  }
  const co2Number = parseInt(co2Data[0], 2);
  return [co2Data, co2Number];
}

const gam = gammaRate(testBitStrings);
const ep = epsilonRate(testBitStrings);
console.log(gam, ep, gam[1] * ep[1]);

const o = oxygenRating(bitStrings)[1];
const c = co2Rating(bitStrings)[1];
console.log(o * c);