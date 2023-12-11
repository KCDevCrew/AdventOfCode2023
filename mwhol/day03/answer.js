const fs = require('fs')

const input = fs.readFileSync('input.txt').toString()
let array = input.split('\r\n')
array = array.map(x => x.split(''))

const rowLength = array[0].length
const buffer = Array(rowLength).fill('.')

function isNumeric (n) {
  // https://stackoverflow.com/questions/175739/how-can-i-check-if-a-string-is-a-valid-number
  return !isNaN(parseFloat(n)) && isFinite(n)
}

function isPeriod (x) {
  return (x.indexOf('.') !== -1)
}

function isSymbol (x) {
  return (!isNumeric(x) && !isPeriod(x))
}

function isGear (x) {
  return (x.indexOf('*') !== -1)
}

// Building our buffer.
array.push(Array.from(buffer)) // ugly way to avoid appending by reference
array.unshift(Array.from(buffer))
for (let i = 0; i < array.length; i++) {
  array[i].push('.')
  array[i].unshift('.')
}

let numStr = ''
let touchesSymbol = false
let touchesGear = false
const partOneRelevantNums = []
const partTwoMap = new Map([])
let gearCoords = []
const rangeChecks = [-1, 0, 1]

console.log(typeof (rangeChecks[0]))

//loop through every element of grid
for (let i = 1; i < array.length - 1; i++) {
  for (let j = 1; j < array[i].length - 1; j++) {
    if (isNumeric(array[i][j])) {
      numStr += array[i][j]
      // checking if we touch a symbol (or gear)
      for (const x of rangeChecks) { // of and in are not the same
        for (const y of rangeChecks) {
          const newi = i + x
          const newj = j + y
          if (isSymbol(array[newi][newj])) {
            touchesSymbol = true
          }
          if (isGear(array[newi][newj])) {
            touchesGear = true
            gearCoords.push(newi + ',' + newj)
            gearCoords = [...new Set(gearCoords)]
          }
        }
      }

      // when we're on the last number
      if (!isNumeric(array[i][j + 1])) {
        const num = parseInt(numStr)
        // Part One
        if (touchesSymbol) {
          partOneRelevantNums.push(num)
        }
        // Part Two
        // Basically building a map, keys are gear coordinates
        // values are lists of numbers they touch
        if (touchesGear) {
          for (const gear of gearCoords) {
            if (partTwoMap.has(gear)) {
              const tempList = partTwoMap.get(gear)
              tempList.push(num)
              partTwoMap.set(gear, tempList)
            } else {
              partTwoMap.set(gear, [num])
            }
          }
        }
        numStr = ''
        touchesSymbol = false
        touchesGear = false
        gearCoords = []
      }
    }
  }
}

const partOneAnswer = partOneRelevantNums.reduce((sum, num) => sum + num)

console.log('Part One: ', partOneAnswer)

let partTwoAnswer = 0
for (const [key, value] of partTwoMap) {
  if (value.length === 2) {
    partTwoAnswer += value.reduce((prod, num) => prod * num)
  }
}

console.log('Part Two: ', partTwoAnswer)
