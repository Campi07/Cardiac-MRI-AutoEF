import Link from "next/link"

export default function Home() {

  return (

    <main className="min-h-screen flex items-center justify-center bg-slate-100">

      <div className="text-center">

        <h1 className="text-5xl font-bold mb-6">
          Cardiac MRI AI
        </h1>

        <Link
          href="/dashboard"
        >

          <button className="rounded-xl bg-blue-600 px-6 py-3 text-white">

            Open Dashboard

          </button>

        </Link>

      </div>

    </main>
  )
}