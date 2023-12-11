const fs = require('fs')

const input = fs.readFileSync('input.txt').toString()
let array = input.split('\r\n')
array = array.map((x) => x.split(' '))
console.log(array)


for hand in array