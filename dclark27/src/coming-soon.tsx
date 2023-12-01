export const ComingSoon = (props: { day: number }) => {
  return (
    <div className="flex flex-col items-start gap-2 py-8">
      <h2 className="text-2xl font-extrabold tracking-tight text-gray-900 sm:text-3xl">
        Day {props.day}
      </h2>
      <div className="mt-4 flex w-full items-center justify-between gap-6">
        <div className="flex w-1/2 flex-col gap-2">Coming son</div>
        <div className="flex w-1/2 flex-col gap-2">Coming son</div>
      </div>
    </div>
  )
}
