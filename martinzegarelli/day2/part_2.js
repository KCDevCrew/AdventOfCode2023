const { readFileSync } = require('fs');
const input = readFileSync('./input.txt', 'utf-8').split('\n');

let sum = 0;
for (let line of input) {
  const colorCounts = {
    red: 0,
    green: 0,
    blue: 0,
  };
  const [_game, sets] = line.split(':');

  for (const set of sets.split(';')) {
    const setColors = set.split(',');
    for (const grouping of setColors) {
      const [_unusedSpace, colorCount, colorString] = grouping.split(' ');
      const colorCountNumber = parseInt(colorCount);
      if (colorCounts[colorString] < colorCountNumber) {
        colorCounts[colorString] = colorCountNumber;
      }
    }
  }
  const gamePower = colorCounts.red * colorCounts.green * colorCounts.blue;
  sum += gamePower;
}
console.log(sum);
