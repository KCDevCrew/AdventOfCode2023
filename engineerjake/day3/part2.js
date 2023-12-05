const clc = require('cli-color')
const fs = require('fs')
const data = fs.readFileSync(process.argv[2], 'utf8').split('\n')

// Not a digit, not a period, must be a symbol!

const numbers = [] // { v: '', row: null, colS: null, colE: null }
const gears = [] // { v: '', row: null, col: null, parts: [] }

const validDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
const isDigit = (char) => {  
  return validDigits.includes(char)
}

const lineLength = (data[0]) ? data[0].length : 0

for (let row = 0; row < data.length; row++) {
  const line = data[row]
  let cNum = { v: '', row: null, colS: null, colE: null }

  for (let col = 0; col < lineLength; col++) {
    const char = line[col]
    if (isDigit(char)) { // it's a digit!
      if (cNum.row === null) cNum.row = row
      if (cNum.colS === null) cNum.colS = col
      cNum.v += char
    } else { // not a digit
      if (cNum.v !== '') { // cNum is open, close it out!
        const completedNumber = {
          v: parseInt(cNum.v),
          row: cNum.row,
          colS: cNum.colS,
          colE: ((col - 1) > 0) ? col - 1 : lineLength,
        }
        // Calculate the range to use later...
        completedNumber.w_range = [
          ((completedNumber.colS - 1) >= 0) ? completedNumber.colS - 1 : completedNumber.colS,
          ((completedNumber.colE + 1) < lineLength) ? completedNumber.colE + 1 : completedNumber.colE,
        ]
        completedNumber.h_range = [
          ((completedNumber.row - 1) >= 0) ? completedNumber.row - 1 : completedNumber.row,
          ((completedNumber.row + 1) < data.length) ? completedNumber.row + 1 : completedNumber.row,
        ]

        numbers.push(completedNumber)

        // Reset cNum
        cNum = { v: '', row: null, colS: null, colE: null }
      }

      if (char === '*') {
        // We have a potential gear!
        gears.push({ v: char, row, col, parts: [] })
      }
    }
  }

  // If we're at the end and cNum hasn't been closed out,
  // then it's a line that ends in a number, close it out!
  if (cNum.v !== '') {
    const completedNumber = {
      v: parseInt(cNum.v),
      row: cNum.row,
      colS: cNum.colS,
      colE: lineLength - 1
    }

    completedNumber.w_range = [
      ((completedNumber.colS - 1) >= 0) ? completedNumber.colS - 1 : completedNumber.colS,
      ((completedNumber.colE + 1) < lineLength) ? completedNumber.colE + 1 : completedNumber.colE,
    ]

    completedNumber.h_range = [
      ((completedNumber.row - 1) >= 0) ? completedNumber.row - 1 : completedNumber.row,
      ((completedNumber.row + 1) < data.length) ? completedNumber.row + 1 : completedNumber.row,
    ]

    numbers.push(completedNumber)
    // no need to reset cNum, it gets reset at the beginning of the loop.
  }
}

for (const num of numbers) {
  // Look for a gear near by
  const gear = gears.find(g => {
    return (
      (g.row >= num.h_range[0] && g.row <= num.h_range[1]) &&
      (g.col >= num.w_range[0] && g.col <= num.w_range[1])
    )
  })

  if (gear) {
    num.hit = true
    num.ignored = true
    gear.parts.push(num)
    gear.hit = (gear.parts.length === 2)
    if (gear.parts.length === 2) {
      gear.parts[0].ignored = false
      gear.parts[1].ignored = false
      gear.ratio = gear.parts[0].v * gear.parts[1].v
    }
  }
}

const ans = gears.reduce((acc, gear) => {
  if (gear.ratio) acc += gear.ratio
  return acc
}, 0)

// Color coded output of analysis.
// Numbers added are GREEN
// Numbers ignored are GRAYish
// Gears hit are RED
// Gears ignored are YELLOW
for (let row = 0; row < data.length; row++) {
  const line = data[row]
  let cNum = { v: '', row: null, colS: null, colE: null }

  let lineOutput = ''
  for (let col = 0; col < lineLength; col++) {
    const char = line[col]
    if (isDigit(char)) { // it's a digit!
      if (cNum.row === null) cNum.row = row
      if (cNum.colS === null) cNum.colS = col
      cNum.v += char
    } else { // not a digit
      // if cNum is open, close it out!
      if (cNum.v !== '') {
        // Determine if the number was hit or not
        const num = numbers.find(n => {
          return (n.row === row && n.colS === cNum.colS)
        })

        lineOutput += (num.hit)
          ? (num.ignored) ? clc.yellowBright(cNum.v) : clc.greenBright(cNum.v)
          : clc.blackBright(cNum.v)

        // Reset cNum
        cNum = { v: '', row: null, colS: null, colE: null }
      }

      if (char === '*') {
        // Determine if the symbol was hit or not
        const gear = gears.find(s => {
          return (s.row === row && s.col === col)
        })

        lineOutput += (gear.hit) ? clc.redBright(char) : clc.yellowBright(char)
      } else {
        lineOutput += clc.blackBright(char)
      }
    }
  }

  if (cNum.v !== '') {
    lineOutput += clc.greenBright(cNum.v)
    // no need to reset cNum, it gets reset at the beginning of the loop.
  }

  console.log(lineOutput)
}

console.log('Answer:', ans) // 87263515