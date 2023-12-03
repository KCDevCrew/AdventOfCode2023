#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) throw err;
  const content = data;
  processFile(content);
});

const processFile = (c) => {
  const requested = {red: 12, green: 13, blue: 14}
  const gameMap = new Map();
  const lines = c.toString().split(/\r\n/);
  let gameObject = {};
  lines.forEach((line) => {
    const gameNumber = parseInt(line.split(':')[0].replace(/Game/i, '').trim());
    const gameData = line.split(':')[1].split(';');
    let red = 0;
    let blue = 0;
    let green = 0;

    gameData.forEach((pull) => {
      if (pull.includes('red')) {
        const startIndex = pull.indexOf('red') - 3;
        const redCount = parseInt(pull.substring(startIndex, pull.indexOf('red')).trim());
        if (redCount > red) {
          red = redCount;
        };
      }
      if (pull.includes('green')) {
        const startIndex = pull.indexOf('green') - 3;
        const greenCount = parseInt(pull.substring(startIndex, pull.indexOf('green')).trim());
        if (greenCount > green) {
          green = greenCount;
        }
      }
      if (pull.includes('blue')) {
        const startIndex = pull.indexOf('blue') - 3;
        const blueCount = parseInt(pull.substring(startIndex, pull.indexOf('blue')).trim());
        if (blueCount > blue) {
          blue = blueCount;
        }
      }
    })

    gameObject = { red: red, blue: blue, green: green };
    gameMap.set(gameNumber, gameObject);
  });

  gameMap.forEach((value, key) => {
    gameMap.set(key, {...value, power: value.red * value.blue * value.green})
  })
  console.log(gameMap);
  let sum = 0;
  gameMap.forEach(game => sum += game.power);
  console.log(`answer: ${sum}`);
  return sum;
};