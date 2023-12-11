var fs = require('fs');

let input = fs.readFileSync('input.txt').toString()
var array = input.split("\r\n")

function string_to_only_numerals(string) {
  var numsStr = string.replace(/[^0-9]/g, '');
  return numsStr
}

function to_first_last_number(string) {
	let char_one = string.charAt(0);
	let char_two = string.charAt(string.length - 1);
	let chars = char_one + char_two
	return parseInt(chars)
}

part_one_array = array.map(string_to_only_numerals)
part_one_array = part_one_array.map(to_first_last_number)
part_one_answer = part_one_array.reduce((sum, num) => sum + num)

console.log("Part One: ", part_one_answer)

////////////////////////////////////

const replace_map_object = {
        'one': 'one1one',
        'two': 'two2two',
        'three': 'three3three',
        'four': 'four4four',
        'five': 'five5five',
        'six': 'six6six',
        'seven': 'seven7seven',
        'eight': 'eight8eight',
        'nine': 'nine9nine'
    }

replace_map = new Map(Object.entries(replace_map_object))

function strnum_to_just_num(string) {
	let fixed_string = string
	for (let [key, value] of replace_map.entries()) {
		// Note: replace != replaceAll 
		fixed_string = fixed_string.replaceAll(key, value)
	}
	return fixed_string
}

part_two_array = array.map(strnum_to_just_num)
part_two_array = part_two_array.map(string_to_only_numerals)
part_two_array = part_two_array.map(to_first_last_number)
part_two_answer = part_two_array.reduce((sum, num) => sum + num)

console.log("Part Two: ", part_two_answer)