import { Day } from './day'
import { ComingSoon } from 'coming-soon'

function App() {
  const days = Array.from({ length: 25 }, (_, i) => i + 1)
  const completedDays = [1]
  return (
    <div className="relative bg-white">
      <div className="h-screen">
        <div className="relative mx-auto max-w-7xl px-4 sm:static sm:px-6 lg:px-8">
          <span>dclark27: Advent of Code 2023</span>
          {days.map((day, index) => {
            if (completedDays.includes(index + 1)) {
              return <Day key={day} day={index + 1} />
            } else {
              return <ComingSoon key={day} day={index + 1} />
            }
          })}
        </div>
      </div>
    </div>
  )
}

export default App
