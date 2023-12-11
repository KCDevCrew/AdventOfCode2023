const stringNumbers = [
	'one',
	'two',
	'three',
	'four',
	'five',
	'six',
	'seven',
	'eight',
	'nine',
];

export const solution = (input: string): string => {
	const entries = input.split('\n');
	let total: number = 0;
	const numberOnlyEntry: string[] = [];
	entries.forEach((entry) => {
		const entryResult: string[] = [];
		for (let i = 0; i < entry.length; i++) {
			const isIndexNumber = parseInt(entry[i]);
			if (isIndexNumber > 0) {
				entryResult.push(entry[i]);
			}
			stringNumbers.forEach((stringNumber, index) => {
				const testString = entry.slice(i, stringNumber.length + i);
				if (testString === stringNumber) {
					entryResult.push('' + (index + 1));
				}
			});
		}
		numberOnlyEntry.push(entryResult.join(''));
	});

	numberOnlyEntry.forEach((entry) => {
		const arr = entry.split('');
		const right = arr.pop();
		const left = arr.shift();
		const resultDigits = [left ?? right, right ?? left].join('');
		total += Number(resultDigits);
	});

	numberOnlyEntry.push('' + total);

	return '' + total;
};
