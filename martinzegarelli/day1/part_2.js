const { readFileSync } = require('fs');
const input = readFileSync('./input.txt', 'utf-8');
const rawInput = input.split('\n');

textToNum = {
  one: '1',
  two: '2',
  three: '3',
  four: '4',
  five: '5',
  six: '6',
  seven: '7',
  eight: '8',
  nine: '9',
};

let sum = 0;
for (let line of rawInput) {
  const regex = RegExp(`(?=(\\d|${Object.keys(textToNum).join('|')}))`, 'g');
  nums = [...line.matchAll(regex)];
  actualNumbers = nums.map((num) => textToNum[num[1]] || num[1]);
  sum += parseInt(`${actualNumbers[0]}${actualNumbers.at(-1)}`);
}
console.log(sum);
