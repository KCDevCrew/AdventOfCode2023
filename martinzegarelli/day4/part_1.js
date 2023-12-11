const { readFileSync } = require('fs');
const input = readFileSync('./input.txt', 'utf-8').split('\n');

let sum = 0;
for (let line of input) {
  const [winningString, actualString] = line
    .replace(/Card \d*:\s* /, '')
    .split(/\s*\|\s*/);
  const winningArray = winningString.split(/\s+/);
  const actualArray = actualString.split(/\s+/);
  const winners = actualArray.filter((value) => winningArray.includes(value));
  sum += winners.length > 0 ? 2 ** (winners.length - 1) : 0;
}

console.log(sum);
