const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '2023-1-input.txt');
const input = fs.readFileSync(filePath, 'utf8');

function sumNumbersInString(str) {
  let sum = 0;
  let lines = str.split("\n");
  for (let line of lines) {
    const numericLine = line.replace(/\D/g, '');

    // If the length is greater than or equal to 2, get the first and last characters
    if (numericLine.length >= 2) {
      const leftDigit = numericLine[0];
      const rightDigit = numericLine[numericLine.length - 1];
      const result = Number(leftDigit + rightDigit);

      sum += result;
      // if just 1, you use the same digit twice
    } else if (numericLine.length === 1) {
      const digit = numericLine[0];
      const result = Number(digit + digit);
      sum += result;
    } else {
      console.error('No numeric characters found for line:', line);
    }
  }
  return sum;
}

const result = sumNumbersInString(input);
console.log('Result:', result);
