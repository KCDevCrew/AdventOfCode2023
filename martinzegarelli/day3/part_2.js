const { readFileSync } = require('fs');
const input = readFileSync('./input.txt', 'utf-8').split('\n');

function findAdjacentNumbers(input, row, column) {
  let adjacentNumbers = [],
    startingRow = row > 0 ? row - 1 : row,
    startingColumn = column > 0 ? column - 1 : column;
  for (const currentRow of [startingRow, startingRow + 1, startingRow + 2]) {
    for (const currentColumn of [
      startingColumn,
      startingColumn + 1,
      startingColumn + 2,
    ]) {
      currentNumberString = input[currentRow][currentColumn];
      if (currentNumberString.match(/\d/)) {
        backSteps = 1;
        while (true) {
          const backIndex = currentColumn - backSteps;
          if (backIndex < 0) {
            break;
          }
          const backChar = input[currentRow][backIndex];
          if (!backChar.match(/\d/)) {
            break;
          }
          currentNumberString = backChar + currentNumberString;
          backSteps += 1;
        }
        forwardSteps = 1;
        while (true) {
          const forwardIndex = currentColumn + forwardSteps;
          if (forwardIndex >= input[currentRow].length) {
            break;
          }
          const forwardChar = input[currentRow][forwardIndex];
          if (!forwardChar.match(/\d/)) {
            break;
          }
          currentNumberString = currentNumberString + forwardChar;
          forwardSteps += 1;
        }
        adjacentNumbers.push(parseInt(currentNumberString));
      }
    }
  }

  return [...new Set(adjacentNumbers)];
}

let sumOfGearRatios = 0;
lineNumber = -1;
for (let line of input) {
  let columnNumber = -1;
  lineNumber += 1;
  for (let char of line) {
    columnNumber += 1;
    if (char === '*') {
      const adjacentNumbers = findAdjacentNumbers(
        input,
        lineNumber,
        columnNumber
      );
      if (adjacentNumbers.length === 2) {
        sumOfGearRatios += adjacentNumbers[0] * adjacentNumbers[1];
      }
    }
  }
}

console.log(sumOfGearRatios);
