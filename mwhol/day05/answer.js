const fs = require('fs')

const input = fs.readFileSync('input.txt').toString()
let array = input.split('\r\n\r\n')

// playing around with some horrific one liners lol
seeds = array[0].split(": ")[1].split(" ").map(Number)
maps = array.slice(1).map((x) => x.split('\r\n').slice(1).map((y) => y.split(" ").map(Number)))

let locationsArray = []

for (seed of seeds){
	let currentValue = seed
	for (map of maps) {
		let difference = 0
		let match = false
		for (range of map) {
			bottom = range[1]													// just for my ease in coding
			top = range[1] + range[2] -1
			distance = range[0] - range[1]
			if (currentValue >= bottom && currentValue<= top) {
				match = true
				difference = distance
				break
			}
		}
		currentValue += difference
	}
	locationsArray.push(currentValue)
}

console.log("Part One: ", Math.min(...locationsArray))							//... = spread => array becomes list of values


//Part two, i could do some recursiv stuff or I could 
//avoid that and go map of maps then seed of seeds, at each level
//I will have an array of [top, bottom], that can then be passed into the next map
//at each range, I will check to see if there is leftover range unmapped from the first match
//and then push it onto the array 

//Linear mappings means we need only to keep track of top and bottom
//but require recursive splitting as we go down the mappings


//not happy with this of grouping to pairs, should be functional
var seedsTwo = [], size = 2;
while (seeds.length > 0) seedsTwo.push(seeds.splice(0, size));
seedsTwo = seedsTwo.map((x) => [x[0], x[0]+x[1]-1])
// console.log(seedsTwo)

var sortedArray = maps.map((map) => map.sort(function(a, b) { return a[1] - b[1]} ))
// console.log(sortedArray)

// function mapping(seedBottom, seedTop, map) {
// 	let answers = []
// 	for (range of map) {
// 		rangeBottom = range[1]													// just for my ease in coding
// 		rangeTop = range[1] + range[2] - 1
// 		distance = range[0] - range[1]
// 		if (seedBottom <= rangeTop && seedTop >= rangeBottom) {					// if they overlap
// 			if (seedBottom >= rangeBottom && seedTop > rangeTop) {									// if clean overlap
// 				console.log(1)
// 				answers.push(seedBottom, rangeTop)
// 				let remaining = [rangeTop+1, seedTop]
// 			}
// 			if (seedBottom >= rangeBottom && seedTop <= rangeTop) {
// 				answers.push(seedBottom, seedTop)
// 				remaining = []
// 				break
// 			}
// 			if (seedBottom < rangeBottom && seedTop <= rangeTop) {


// 			}


// 			////
// 			if (seedBottom < rangeBottom) {										// if seed dips into unmapped region
// 				console.log(2)
// 				let answers = [seedBottom, rangeBottom-1, rangeBottom, ]
// 				let remaining = []
// 			}
// 			else {
// 				console.log(3)
// 				answers.push(seedBottom, seedTop)
// 				let remaining = []
// 			}
// 		}
// 		// I don't think we need this, we already know it overlaps from above
// 		// else if (seedTop >= rangeTop && seedBottom <= rangeTop) {
// 		// 	let bottom = seedBottom, top = rangeTop
// 		// 	let remainingBottom = rangeTop+1, remainingTop = seedTop
// 		// }
// 		else {
// 			let remaining = [seedBottom, seedTop]
// 		}
// 		//some appending thing here
// 	}
// 	return answers, remaining
// }

// mapping(seedsTwo[0][0], seedsTwo[0][1], maps[0])

// for (seed of seeds){
// 	let seedBottom = seed[0], seedTop = seed[1]
// 	for (map of maps) {
// 		let difference = 0
// 		let match = false
// 		for (range of map) {
// 			bottom = range[1]													// just for my ease in coding
// 			top = range[1] + range[2] -1
// 			distance = range[0] - range[1]
// 			if (currentValue >= bottom && currentValue<= top) {
// 				match = true
// 				difference = distance
// 				break
// 			}
// 		}
// 		currentValue += difference
// 	}
// 	locationsArray.push(currentValue)
// }


// seedsTwo = seedsTwo.map((x) => [x[0], x[0]+x[1]-1])

// console.log(seedsTwo)

locationsArrayTwo = []
let current_min_value = Infinity
console.log(seedsTwo.length)

for (set of seedsTwo) {
	console.log(set)
	console.log(current_min_value)
	for (let i = set[0]; i <= set[1]; i++) {
		let currentValue = i
		for (map of maps) {
			let difference = 0
			let match = false
			for (range of map) {
				bottom = range[1]													// just for my ease in coding
				top = range[1] + range[2] -1
				distance = range[0] - range[1]
				if (currentValue >= bottom && currentValue<= top) {
					match = true
					difference = distance
					break
				}
			}
			currentValue += difference
		}
	if (currentValue < current_min_value) {console.log(currentValue)}
	current_min_value = Math.min(current_min_value, currentValue)
	}
}


// console.log("Part Two: ", Math.min(...locationsArrayTwo))							//... = spread => array becomes list of values
console.log("Part Two: ", current_min_value)							//... = spread => array becomes list of values
