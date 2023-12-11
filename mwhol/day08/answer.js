const fs = require('fs')

const input = fs.readFileSync('input.txt').toString().replaceAll('(', '').replaceAll(')', '')
let array = input.split('\r\n\r\n')
let instructions = array[0]
let hands = array[1].split('\r\n').map((x) => [x.split(/ = /)[0], x.split(/ = /)[1].split(", ")])

hands = Object.fromEntries(hands)

// console.log(instructions)
// console.log(hands)

let current_point = 'AAA'
let step_counter = 0

while (current_point !== 'ZZZ') {
	const instruction = instructions[step_counter % instructions.length]
	if (instruction === 'R') {
		current_point = hands[current_point][1]
	}
	else {
		current_point = hands[current_point][0]		
	}
	// console.log(current_point)
	step_counter++
}

console.log("Part One: ", step_counter)

let points = Object.keys(hands)
let current_points = points.filter((point) => point[2]==='A')
step_counter = 0
complete_status = false
let next_point = ''
let lcm_array = new Array(6).fill(0)

console.log(current_points)
console.log('AAAAAA'===current_points.map((x) => x[2]).join(''))

while (!complete_status) {
	for (let i = 0; i < current_points.length; i++) {
		const instruction = instructions[step_counter % instructions.length]
		if (instruction === 'R') {
			next_point = hands[current_points[i]][1]
			current_points[i] = next_point
		}
		else {
			next_point = hands[current_points[i]][0]
			current_points[i] = next_point
		}
		// Cheated a little bit here, read on the reddit that there's distinct loops 
		// for each point, can just calculate the loops and then use least common multiple
		// since bruteforcing wasn't working, just kludged the logic in here
		if (next_point[2]==='Z' && lcm_array[i]===0) {
			lcm_array[i] = step_counter
			console.log("point: ", i, " | step: ", step_counter+1)
		}
	}
	step_counter++
	let last_letter_of_points = current_points.map((x) => x[2]).join('')
	complete_status = (lcm_array.filter(x => x === 0).length === 0)
	// complete_status = ('ZZZZZZ'===last_letter_of_points)
}

var gcd = function (a, b) {
    return a ? gcd(b % a, a) : b
}


function lcm(a, b) {
	return (a * b) / gcd(a, b)
}

var n = 1
for (var i=0; i<lcm_array.length; ++i) {
	n = lcm(lcm_array[i], n);
}


//hmm not working, did it in google sheets, need to look into 
//why this lcm isn't working, prbably the gcd
console.log("Part Two: ", n)
