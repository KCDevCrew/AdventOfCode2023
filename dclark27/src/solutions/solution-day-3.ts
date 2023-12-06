function isNumeric(value: string) {
	return /^-?\d+$/.test(value);
}

type NumberMap = {
	number: number;
	symbolBelow: boolean;
	symbolAbove: boolean;
	symbolLeft: boolean;
	symbolRight: boolean;
	symbolTopLeft: boolean;
	symbolTopRight: boolean;
	symbolBottomLeft: boolean;
	symbolBottomRight: boolean;
};
export const solution = (input: string): string => {
	const partNumbers: string[] = [];
	const numberMaps: NumberMap[] = [];
	const matrix: string[][] = input.split('\n').map((line) => line.split(''));

	for (let row = 0; row < matrix.length; row++) {
		let currNumber = [];
		for (let column = 0; column < matrix[row].length; column++) {
			const numberMap: NumberMap = {
				number: 0,
				symbolBelow: false,
				symbolAbove: false,
				symbolLeft: false,
				symbolRight: false,
				symbolTopLeft: false,
				symbolTopRight: false,
				symbolBottomLeft: false,
				symbolBottomRight: false,
			};
			const curr = matrix[row][column];
			const next = matrix[row][column + 1];

			if (isNumeric(curr) && next) {
				currNumber.push(curr);
			} else if (currNumber.length > 0) {
				if (!next) {
					currNumber.push(curr);
					column++;
				}
				numberMap.number = parseInt(currNumber.join(''));
				partNumbers.push(currNumber.join(''));

				// Check left
				if (
					matrix[row][column - currNumber.length - 1] &&
					matrix[row][column - currNumber.length - 1] !== '.'
				) {
					numberMap.symbolLeft = true;
				}

				// Check right
				if (matrix[row][column] && matrix[row][column] !== '.') {
					numberMap.symbolRight = true;
				}

				// Check bottom and top
				for (let word = 0; word < currNumber.length; word++) {
					// look up
					if (matrix[row - 1] && matrix[row - 1][column - word - 1]) {
						const curr = matrix[row - 1][column - word - 1];
						if (curr !== '.' && !isNumeric(curr)) {
							numberMap.symbolAbove = true;
						}
					}

					// look down
					if (matrix[row + 1] && matrix[row + 1][column - word - 1]) {
						const curr = matrix[row + 1][column - word - 1];
						if (curr !== '.' && !isNumeric(curr)) {
							numberMap.symbolBelow = true;
						}
					}
				}

				// look diagonal down left
				if (
					matrix[row + 1] &&
					matrix[row + 1][column - currNumber.length - 1]
				) {
					const curr = matrix[row + 1][column - currNumber.length - 1];
					if (curr !== '.' && !isNumeric(curr)) {
						numberMap.symbolBottomLeft = true;
					}
				}

				// look diagonal down right
				if (matrix[row + 1] && matrix[row + 1][column]) {
					const curr = matrix[row + 1][column];
					if (curr !== '.' && !isNumeric(curr)) {
						numberMap.symbolBottomRight = true;
					}
				}

				// look diagonal up left
				if (
					matrix[row - 1] &&
					matrix[row - 1][column - currNumber.length - 1]
				) {
					const curr = matrix[row - 1][column - currNumber.length - 1];
					if (curr !== '.' && !isNumeric(curr)) {
						numberMap.symbolTopLeft = true;
					}
				}

				// look diagonal up right
				if (matrix[row - 1] && matrix[row - 1][column]) {
					const curr = matrix[row - 1][column];
					if (curr !== '.' && !isNumeric(curr)) {
						numberMap.symbolTopRight = true;
					}
				}

				numberMaps.push(numberMap);
				currNumber = [];
			}
		}
	}

	let sum = 0;
	numberMaps.forEach((map) => {
		if (
			map.symbolAbove ||
			map.symbolBelow ||
			map.symbolBottomLeft ||
			map.symbolBottomRight ||
			map.symbolLeft ||
			map.symbolRight ||
			map.symbolTopLeft ||
			map.symbolTopRight
		) {
			sum += map.number;
		}
	});

	return '' + sum;
	// return JSON.stringify(numberMaps, null, 2);
};
