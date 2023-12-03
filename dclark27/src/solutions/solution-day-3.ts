export const solution = (input: string): string => {
	const partNumbers: number[] = [];
	const matrix: string[][] = input.split('\n').map((line) => line.split(''));

	for (let row = 0; row < matrix.length; row++) {
		for (let column = 0; column < matrix[row].length; column++) {
			const lookLeft = false;
			const lookRight = false;
		}
	}

	return JSON.stringify(matrix);
};
