const { readFileSync } = require('fs');
const input = readFileSync('./input.txt', 'utf-8').split('\n');

const cardCounts = {};
let sum = 0;
for (let line of input) {
  const [cardNumberString, winningString, actualString] = line
    .replace(/Card\s*/, '')
    .split(/\:\s*|\s*\|\s*/);
  const cardNumber = parseInt(cardNumberString);
  cardCounts[cardNumber] = cardCounts[cardNumber]
    ? cardCounts[cardNumber] + 1
    : 1;
  const winningArray = winningString.split(/\s+/);
  const actualArray = actualString.split(/\s+/);
  const winners = actualArray.filter((value) => winningArray.includes(value));
  let newCardNumber = cardNumber;
  for (const winner of winners) {
    newCardNumber += 1;
    cardCounts[newCardNumber] = cardCounts[newCardNumber]
      ? cardCounts[newCardNumber] + 1 * cardCounts[cardNumber]
      : 1 * cardCounts[cardNumber];
  }
}

console.log(
  Object.values(cardCounts).reduce((partialSum, a) => partialSum + a, 0)
);
