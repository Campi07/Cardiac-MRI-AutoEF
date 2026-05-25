export default function ResultsPanel() {
  return (

    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <h2 className="mb-6 text-xl font-semibold text-slate-700">
        Clinical Results
      </h2>

      <div className="grid grid-cols-2 gap-4">

        <div className="rounded-xl bg-slate-100 p-4">
          <p className="text-sm text-slate-500">Ejection Fraction</p>
          <h3 className="text-2xl font-bold text-slate-800">-- %</h3>
        </div>

        <div className="rounded-xl bg-slate-100 p-4">
          <p className="text-sm text-slate-500">Dice Score</p>
          <h3 className="text-2xl font-bold text-slate-800">--</h3>
        </div>

        <div className="rounded-xl bg-slate-100 p-4">
          <p className="text-sm text-slate-500">EDV</p>
          <h3 className="text-2xl font-bold text-slate-800">-- mL</h3>
        </div>

        <div className="rounded-xl bg-slate-100 p-4">
          <p className="text-sm text-slate-500">ESV</p>
          <h3 className="text-2xl font-bold text-slate-800">-- mL</h3>
        </div>

      </div>

    </div>
  )
}