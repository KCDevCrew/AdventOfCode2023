const clc = require('cli-color')
const fs = require('fs')
const data = fs.readFileSync(process.argv[2], 'utf8').split('\n')

const ans = data.reduce((acc, card) => {
  let lineOutput = '';
  const [cardName, numbers] = card.split(/: |, /)

  lineOutput += cardName + ': '

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
  // console.log(cardName, winningNumbers, cardNumbers)
  const numbersAnalyzed = []
  const cardScore = cardNumbers.reduce((acc, n) => {
    const isWinningNumber = winningNumbers.includes(n)

    // Re-add leading space if number is single digit
    // for better display of numbers...
    let nS = n.toString()
    if (nS.length === 1) nS = ' ' + nS

    numbersAnalyzed.push(
      isWinningNumber
        ? clc.green(`(${nS})`)
        : clc.blackBright(` ${nS} `)
    )

    if (!isWinningNumber) return acc

    if (acc === 0) {
      acc = 1
      return acc
    } else {
      return acc *= 2
    }
  }, 0)

  lineOutput += numbersAnalyzed.join(' ')

  acc += cardScore

  console.log(lineOutput, ' -- SCORE: ', cardScore)

  return acc
}, 0)

console.log(ans) // 26443