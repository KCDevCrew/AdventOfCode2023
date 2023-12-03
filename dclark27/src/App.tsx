import { Day } from './day'
import { ComingSoon } from 'coming-soon'

function App() {
  const days = Array.from({ length: 25 }, (_, i) => i + 1)
  const completedDays = [1, 2]

  return (
    <main className="container mx-auto flex flex-col">
      <h1 className="py-10 text-5xl font-bold">
        🎄 dclark27: Advent of Code 2023
      </h1>
      <article>
        {days.map((day, index) => {
          if (completedDays.includes(index + 1)) {
            return <Day key={day} day={index + 1} />
          } else {
            return <ComingSoon key={day} day={index + 1} />
          }
        })}
      </article>
    </main>
  )
}

export default App
