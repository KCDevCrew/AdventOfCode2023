const fs = require('fs')

const input = fs.readFileSync('input.txt').toString()
let array = input.split('\r\n')
array = array.map((x) => x.split(': ')[1].split(/\s+/).slice(1).map(Number))

times = array[0]
distances = array[1]
let answers = []

for (let i = 0; i < times.length; i++) {
	time = times[i]
	distance = distances[i]
	a = (time + (Math.sqrt(time**2 - (4*distance))))/2
	b = (time - (Math.sqrt(time**2 - (4*distance))))/2
	let count = Math.floor(a-0.00001) - Math.floor(b+0.00001) // I know there's a better way to make it non-inclusive but this is so fast...
	answers.push(count)
}

console.log("Part One: ", answers.reduce((prod, num) => prod * num))

time = Number(times.join(''))
distance = Number(distances.join(''))
a = (time + (Math.sqrt(time**2 - (4*distance))))/2
b = (time - (Math.sqrt(time**2 - (4*distance))))/2
let count = Math.floor(a-0.00001) - Math.floor(b+0.00001)

console.log("Part Two: ", count)
