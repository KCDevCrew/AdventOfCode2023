var fs = require('fs');

function game_string_to_game_object(string) {
	game_array = string.split(',')
	game_array = game_array.map(game_str => game_str.trim().split(' ').reverse())
	game_object = new Map(game_array)
	return game_object
}


function lines_to_objects(string) {
	const split_one = string.split(':')
	let game_num = split_one[0].split(' ')[1]
	let games = split_one[1].split(';')
	games = games.map(game_string_to_game_object)
	game_and_details = new Map(Object.entries({
		"game_num": game_num,
		"games": games
	}))
	return game_and_details
}


function max_value_from_games(game_object, key) {
	max_val = 0
	games = game_object.get('games')
	for (let i = 0; i < games.length; i++) {
    	max_val = Math.max(max_val, games[i].get(key) || 0)
	}
	return max_val
}

let input = fs.readFileSync('input.txt').toString()
var array = input.split("\r\n")
array = array.map(lines_to_objects)

running_sum = 0
running_cubes = 0
for (let i = 0; i < array.length; i++) {
	blue_max = max_value_from_games(array[i], 'blue')
	green_max = max_value_from_games(array[i], 'green')
	red_max = max_value_from_games(array[i], 'red')
	if (red_max <= 12 && green_max <= 13 && blue_max <= 14) {
		running_sum += (i+1)
	}
	cube_product = blue_max * green_max * red_max
	running_cubes += cube_product
}

console.log("Part One: ", running_sum)

console.log("Part Two: ", running_cubes)