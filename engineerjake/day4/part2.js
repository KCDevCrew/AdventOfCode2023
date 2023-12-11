const clc = require('cli-color')
const fs = require('fs')
const data = fs.readFileSync(process.argv[2], 'utf8').split('\n')

const cards = data.map(line => {
  const [cardName, numbers] = line.split(/: |, /)
  const [winningNumbers, cardNumbers] = numbers
    .split(' | ')
    .map(nS => nS.split(' ')
      .reduce((acc, n) => {
        if (n.length === 0) return acc
          acc.push(parseInt(n))
          return acc
        }, []
      )
    )

  return {
    name: cardName,
    matchingNumbers: cardNumbers.reduce((acc, n) => {
      acc += winningNumbers.includes(n) ? 1 : 0
      return acc
    }, 0),
    instances: 1
  }
})

for (let i = 0; i < cards.length; i++) {
  const card = cards[i]
  for (let instance = 0; instance < card.instances; instance++) {
    for (let j = 0; j < card.matchingNumbers; j++) {
      if (cards[i + j + 1]) cards[i + j + 1].instances++
    }
  }
}

const ans = cards.reduce((acc, card) => acc += card.instances, 0)
console.log('Answer:', ans) // 6284877