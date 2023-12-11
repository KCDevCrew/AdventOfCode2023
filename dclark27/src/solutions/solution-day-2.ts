const bag = {
	red: 12,
	green: 13,
	blue: 14,
};

type Game = {
	green: number;
	blue: number;
	red: number;
	id: number;
	possible: boolean;
};

export const solution = (input: string): string => {
	const games = input.split('\n');
	const gameArr: Game[] = [];

	for (let i = 0; i < games.length; i++) {
		const game: Game = {
			possible: true,
			red: 0,
			blue: 0,
			green: 0,
			id: 0,
		};
		// const gameTitle = games[i].match(/Game ([1-9]|[1-9][0-9]|100):/g)?.pop()
		const gameStr = games[i].replace(/Game ([1-9]|[1-9][0-9]|100): /g, '');
		const gameId = i + 1;

		if (gameId) {
			game.id = gameId;
			const rolls = gameStr.split(';');
			for (let j = 0; j < rolls.length; j++) {
				const redDice = rolls[j].match(/([1-9]|[1-9][0-9]|100) red/g)?.pop();
				const blueDice = rolls[j].match(/([1-9]|[1-9][0-9]|100) blue/g)?.pop();
				const greenDice = rolls[j]
					.match(/([1-9]|[1-9][0-9]|100) green/g)
					?.pop();
				if (redDice) {
					const redStr = redDice.match(/([1-9]|[1-9][0-9]|100) red/g)?.pop();
					if (redStr) {
						const redTotal = parseInt(redStr);
						game.possible = game.possible
							? bag.red >= redTotal
								? true
								: false
							: false;
						game.red = redTotal > game.red ? redTotal : game.red;
					}
				}
				if (blueDice) {
					const blueStr = blueDice.match(/([1-9]|[1-9][0-9]|100) blue/g)?.pop();
					if (blueStr) {
						const blueTotal = parseInt(blueStr);
						game.possible = game.possible
							? bag.blue >= blueTotal
								? true
								: false
							: false;
						game.blue = blueTotal > game.blue ? blueTotal : game.blue;
					}
				}
				if (greenDice) {
					const greenStr = greenDice
						.match(/([1-9]|[1-9][0-9]|100) green/g)
						?.pop();
					if (greenStr) {
						const greenTotal = parseInt(greenStr);
						game.possible = game.possible
							? bag.green >= greenTotal
								? true
								: false
							: false;
						game.green = greenTotal > game.green ? greenTotal : game.green;
					}
				}
			}
		}
		gameArr.push(game);
	}

	let possibleGameTotal = 0;
	let powerSet = 0;

	gameArr.forEach((game) => {
		if (game.possible) {
			possibleGameTotal += game.id;
		}
		const greenOverZero = game.green > 0 ? game.green : 1;
		const blueOverZero = game.blue > 0 ? game.blue : 1;
		const redOverZero = game.red > 0 ? game.red : 1;

		powerSet += greenOverZero * blueOverZero * redOverZero;
	});

	return 'part 1: ' + possibleGameTotal + '\n' + 'part 2: ' + powerSet;
};
