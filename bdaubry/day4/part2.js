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
      wins: 0,
      stock: 1,
    };
    gameMap.set(idx, gameObj);
  });

  const result = calculateGames(gameMap);
  console.log(result);
}

const calculateGames = (map) => {
  // calculate wins
  map.forEach((g, key) => {
    g.playNumbers.forEach((n) => {
      g.winningNumbers.forEach((w) => {
        if (w === n){
          g.wins++;
        }
      })
    });
  });

  // iterate through games
  for (let game = 0; game < map.size; game++) {
    let gameObj = map.get(game);
    // iterate through wins and apply to next games
    for (let next = 1; next <= gameObj.wins; next++) {
      let updateObj = map.get(next + game);
      console.log(`adding to ${next}, new: ${updateObj.stock + gameObj.stock} (${gameObj.stock})`);
      if (updateObj) {
        updateObj.stock += gameObj.stock;
      }
    }
  }

  let totalTix = 0;
  map.forEach((g) => {
    totalTix += g.stock;
  });
  console.log(map);
  return totalTix;
}
