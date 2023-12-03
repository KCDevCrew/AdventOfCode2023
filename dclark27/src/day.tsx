import { Button } from '@/components/ui/button';
import { Label } from '@/components/ui/label';
import { Textarea } from '@/components/ui/textarea';
import { useEffect, useState } from 'react';

export const Day = (props: { day: number }) => {
	const { day } = props;
	const [inputLoaded, setInputLoaded] = useState(false);
	const [input, setInput] = useState('');
	const [result, setResult] = useState('');

	useEffect(() => {
		const loadInput = async () => {
			const input = await import(`./inputs/day-${day}`);
			setInput(input.input);
			setInputLoaded(true);
		};
		if (!inputLoaded) {
			loadInput();
		}
	});

	const runSolution = async () => {
		const { solution } = await import(`./solutions/solution-day-${props.day}`);
		const result = solution(input);
		setResult(result);
	};

	return (
		<div className='flex flex-col items-start gap-2 py-8'>
			<h2 className='text-2xl font-extrabold tracking-tight text-gray-900 sm:text-3xl'>
				Day {day}
			</h2>
			<div className='mt-4 flex w-full items-center justify-between gap-6'>
				<div className='grid w-full gap-1.5'>
					<Label htmlFor={`input-${day}`}>Input</Label>
					<Textarea
						id={`input-${day}`}
						name={`input-${day}`}
						rows={8}
						value={input}
						onChange={(e) => setInput(e.target.value)}
					/>
				</div>
				<div className='grid w-full gap-1.5'>
					<Label htmlFor={`result-${day}`}>Result</Label>
					<Textarea
						readOnly
						rows={8}
						id={`result-${day}`}
						name={`result-${day}`}
						value={result}
					/>
				</div>
			</div>
			<Button onClick={runSolution}>Run Day {day}</Button>
		</div>
	);
};
