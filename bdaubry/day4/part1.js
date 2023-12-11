#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) throw err;
  const content = data;
  processFile(content);
});

const processFile = (c) => {
  const lines = c.split(/\r\n/g);
  const cards = [];
  const gameMap = new Map();
  let points = 0;

  lines.forEach((l) => {
    cards.push(l.replace(/^Card \d+\:/g, '').trim());
  });

  cards.forEach((l, idx) => {
    const numSplit = l.split('|');
    const gameObj = {
      winningNumbers: numSplit[0].split(' ').filter((n) => n !== ''),
      playNumbers: numSplit[1].split(' ').filter((n) => n !== ''),
      points: 0
    };
    gameObj.playNumbers.forEach((n) => {
      gameObj.winningNumbers.forEach((w) => {
        if (w === n && gameObj.points === 0) {
          gameObj.points = 1;
        } else if (w === n) {
          gameObj.points = gameObj.points * 2;
        }
      })
    })
    gameMap.set(idx, gameObj);
  });

  gameMap.forEach((g) => {
    points += g.points;
  });

  console.log(`Total points: ${points}`)

}