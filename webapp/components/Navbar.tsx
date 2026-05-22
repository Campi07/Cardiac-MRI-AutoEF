export default function Navbar() {
  return (
    <nav className="w-full border-b bg-white px-8 py-4 shadow-sm">
      <div className="flex items-center justify-between">

        <h1 className="text-2xl font-semibold text-slate-800">
          Cardiac MRI AI
        </h1>

        <div className="flex gap-6 text-slate-600">
          <button>Dashboard</button>
          <button>Upload</button>
          <button>Results</button>
        </div>

      </div>
    </nav>
  )
}