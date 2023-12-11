interface Game {
	input: string;
	instances: number;
}

const solution_part_1 = (games: Game[]): string => {
	let score = 0;
	games.forEach((game) => {
		const { instances, input } = game;
		let currGameScore = 0;
		const gameTitle: string = input.substring(0, input.lastIndexOf(':'));
		const winningNumbers: string[] = input
			.substring(input.lastIndexOf(':') + 2, input.lastIndexOf('|') - 1)
			.split(' ');
		const currNumbers = input
			.substring(input.lastIndexOf('|') + 2, input.length)
			.split(' ')
			.filter((number) => number !== '');
		let winningCounter = 0;

		currNumbers.forEach((currNumber) => {
			if (winningCounter === 0 && winningNumbers.includes(currNumber)) {
				currGameScore += 1;
				winningCounter++;
			} else {
				if (winningNumbers.includes(currNumber)) {
					const addedScore = Math.pow(2, winningCounter - 1);
					currGameScore += addedScore;
					winningCounter++;
				}
			}
		});
		console.log('adding ' + currGameScore + 'from ' + gameTitle);
		score += currGameScore * instances;
	});

	return '' + score;
};

export const solution = (input: string): string => {
	const games: string[] = input.split('\n');
	const gameTally: Game[] = games.map((game) => ({
		instances: 1,
		input: game,
	}));

	gameTally.forEach((game, gameIndex) => {
		const { input, instances } = game;

		const winningNumbers: string[] = input
			.substring(input.lastIndexOf(':') + 2, input.lastIndexOf('|') - 1)
			.split(' ');
		const currNumbers = input
			.substring(input.lastIndexOf('|') + 2, input.length)
			.split(' ')
			.filter((number) => number !== '');

		let wins = 0;
		winningNumbers.forEach((winningNumber) => {
			if (currNumbers.includes(winningNumber)) {
				wins++;
			}
		});

		if (wins > 0) {
			for (let i = gameIndex + 1; i < wins + gameIndex + 1; i++) {
				if (i < gameTally.length) {
					gameTally[i].instances++;
				}
			}
		}

		if (instances > 1) {
			for (let i = gameIndex + 1; i < wins + gameIndex + 1; i++) {
				gameTally[i].instances += instances - 1;
			}
		}
		console.log(`ending ${gameIndex} with`, gameTally);
	});

	const newGames: string[] = [];

	gameTally.forEach((game) => {
		const { input, instances } = game;

		for (let i = 0; i < instances; i++) {
			newGames.push(input);
		}
	});

	let totalScratchCards = 0;

	gameTally.forEach((game) => {
		totalScratchCards += game.instances;
	});

	return '' + totalScratchCards;
};
