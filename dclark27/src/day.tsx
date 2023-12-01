import { useEffect, useState } from 'react'

export const Day = (props: { day: number }) => {
  const { day } = props
  const [inputLoaded, setInputLoaded] = useState(false)
  const [input, setInput] = useState('')
  const [result, setResult] = useState('')

  useEffect(() => {
    const loadInput = async () => {
      const input = await import(`./inputs/day-${day}`)
      setInput(input.input)
      setInputLoaded(true)
    }
    if (!inputLoaded) {
      loadInput()
    } else {
      runSolution()
    }
  })

  const runSolution = async () => {
    const { solution } = await import(`./solutions/solution-day-${props.day}`)
    const result = solution(input)
    setResult(result)
  }

  return (
    <div className="flex flex-col items-start gap-2 py-8">
      <h2 className="text-2xl font-extrabold tracking-tight text-gray-900 sm:text-3xl">
        Day {day}
      </h2>
      <div className="mt-4 flex w-full items-center justify-between gap-6">
        <div className="flex w-1/2 flex-col gap-2">
          <label htmlFor={`input-${day}`} className="text-xs font-bold">
            Input
          </label>
          <textarea
            id={`input-${day}`}
            name={`input-${day}`}
            rows={8}
            className="rounded-md border-2 border-gray-300 p-2"
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
        </div>
        <div className="flex w-1/2 flex-col gap-2">
          <label htmlFor={`result-${day}`} className="text-xs font-bold">
            Result
          </label>
          <textarea
            readOnly
            rows={8}
            id={`result-${day}`}
            name={`result-${day}`}
            className="rounded-md border-2 border-gray-300 p-2"
            value={result}
          />
        </div>
      </div>
      <button className="rounded-md border p-2 text-xs" onClick={runSolution}>
        Run Day {day}
      </button>
    </div>
  )
}
