const { readFileSync } = require('fs');
const input = readFileSync('./input.txt', 'utf-8').split('\n');

colorCounts = {
  red: 12,
  green: 13,
  blue: 14,
};

let sum = 0;
for (let line of input) {
  const [game, sets] = line.split(':');
  const gameNumber = parseInt(game.split(' ')[1]);

  let isValid = true;
  for (const set of sets.split(';')) {
    const setColors = set.split(',');
    for (const grouping of setColors) {
      const [_unusedSpace, colorCount, colorString] = grouping.split(' ');
      if (colorCounts[colorString] < parseInt(colorCount)) {
        isValid = false;
        break;
      }
    }
  }
  if (isValid) {
    sum += gameNumber;
  }
}
console.log(sum);
