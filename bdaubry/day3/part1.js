#!/usr/bin/node
const fs = require('fs');

fs.readFile('./bdaubry/day3/example.txt', 'utf-8', (err, data) => {
  if (err) throw err;
  const content = data;
  processFile(content);
});

const processFile = (c) => {
  // v.search(/\*|\#|\$|\+/g
  const mat = [];
  const rows = c.split(/\r\n/g);
  rows.forEach((row, idx) => {
    mat.push(row.split(''));
  });
  const numbers = [];

  for (let row = 0; row < mat.length; row++) {
    let numStr = '';
    let start = 0;
    for (let col = 0; col < mat[row].length; col++) {
      if (!isNaN(parseInt(mat[row][col]))) {
        numStr += mat[row][col];
      } else {
        if (numStr !== '') {
          numbers.push({numStr: numStr, row: row, start: start, end: col - 1});
          numStr = '';
          start = col;
        }
        start++;
      }
    }
  }
  console.log(numbers);

  for (let row = 0; row < mat.length; row++) {
    for (let col = 0; col < mat[row].length; col++) {
      if (mat[row][col].search(/\$|\#|\*|\+/g) !== -1) {
        console.log(`symbol at row: ${row} col: ${col}`);

        const result = numbers.filter(() => {
          for (let x = -1; x <= 1; x++) {
            for (let y = -1; y <= 1; y++) {
              return !isNaN(parseInt(mat[row + x][row + y]));
            }
          }
        });
        console.log(result);
        }
        
    }
  }


}


