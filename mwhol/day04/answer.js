const fs = require('fs')

const input = fs.readFileSync('input.txt').toString()
const array = input.split('\r\n')
const cardCounter = new Array(array.length).fill(1)

let totalPoints = 0
let points = 0
for (let i = 0; i < array.length; i++) {
  let line = array[i].split(': ')[1]
  line = line.split(' | ')
  const winNumbers = line[0].split(/\s+/)
  const myNumbers = line[1].split(/\s+/)
  const matches = [winNumbers, myNumbers].reduce((a, b) => a.filter(c => b.includes(c)))
  if (matches.length > 0) {
    points = Math.pow(2, matches.length - 1)
    // Part Two - adding to our card counting array
    for (let j = 0; j < cardCounter[i]; j++) {
      for (let k = 1; k <= matches.length; k++) {
        cardCounter[i + k] += 1
      }
    }
  }
  totalPoints += points
  points = 0
}

console.log('Part One; ', totalPoints)
console.log('Part Two: ', cardCounter.reduce((sum, num) => sum + num))
