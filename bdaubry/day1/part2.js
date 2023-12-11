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
    let result;
    result = parseInt(line[0]+line[line.length-1]);
    lines.splice(idx, 1, result);
  });
  let sum = 0;
  lines.forEach((l) => {
    sum += l;
  });
  console.log(`result: ${sum}`);
  return sum;
};

const processLines = (str) => {
  const t = [];
  str
    .toString()
    .split(/\r\n/)
    .forEach((ln) => {
      let newLn = replaceNumbers(ln);
      let newStr = '';
      for (let c = 0; c < newLn.length; c++ ) {
        if (!isNaN(parseFloat(newLn[c]))) {
          newStr = newStr + newLn[c].toString();
        }
      }
      t.push(newStr);
    });
  return t;
};

const replaceNumbers = (string) => {
  let returnStr = string;
  let newString = '';
  const regex = /one|two|three|four|five|six|seven|eight|nine/g;
  const stringsToReplace = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];

  while (returnStr.search(regex) !== -1) {
    const firstIndex = returnStr.search(regex);
    stringsToReplace.forEach((substr, idx) => {
      if (returnStr.includes(substr) && returnStr.search(substr) === firstIndex) {
        let substrReplace = (idx + 1).toString();
        newString += substrReplace;
        returnStr = returnStr.replace(substr.substring(0, substr.length-1), substrReplace);
      }
    });
  }
  return returnStr;
}