#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) throw err;
  const content = data;
  processFile(content);
});

const processFile = (c) => {
  const lines = processLines(c);
  lines.forEach((line, idx) => {
    if (!isNaN(line)) {
      if (line.length === 1) {
        lines.splice(idx, 1, parseInt(line+line));
      } else {
        lines.splice(idx, 1, parseInt(line[0]+line[line.length-1]));
      }
    };
  });
  const result = lines.reduce((runningSum, addition) => runningSum + addition, 0);
  console.log(`result: ${result}`);
  return result;
};

const processLines = (str) => {
  const t = [];
  str
    .toString()
    .split(/\r\n/)
    .forEach((ln) => {
      let n = '';
      for (let c=0; c<ln.length; c++ ) {
        if (!isNaN(parseFloat(ln[c])) && isFinite(ln[c])) {
          n = n + ln[c].toString();
        }
      }
      t.push(n);
    });
  return t;
}
