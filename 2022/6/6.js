function bufferScan(buffer) {
  let count = 0;
  let SOPAddress = 0;
  for (let index = 0; index < buffer.length; index++) {
    if (count === 4) {
      break;
    }
    const slice = buffer.slice(index, index + 4);
    for (const c of slice) {
      if (slice.split(c).length - 1 > 1) {
        count = 0;
        break;
      } else {
        count += 1;
      }
      if (count === 4) {
        SOPAddress = buffer.indexOf(slice) + 4;
        break;
      }
    }
  }
  return SOPAddress;
}

function bufferScanMessage(buffer) {
  let count = 0;
  let SOMAddress = 0;
  for (let index = 0; index < buffer.length; index++) {
    if (count === 14) {
      break;
    }
    const slice = buffer.slice(index, index + 14);
    for (const c of slice) {
      if (slice.split(c).length - 1 > 1) {
        count = 0;
        break;
      } else {
        count += 1;
      }
      if (count === 14) {
        SOMAddress = buffer.indexOf(slice) + 14;
        break;
      }
    }
  }
  return SOMAddress;
}

const fs = require("fs");
const buffer = fs.readFileSync("input.txt", "utf-8");
console.log(bufferScan(buffer));
console.log(bufferScanMessage(buffer));
