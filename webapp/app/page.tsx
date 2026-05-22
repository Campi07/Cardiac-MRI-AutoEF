import Navbar from "@/components/Navbar"
import UploadBox from "@/components/UploadBox"
import MRIPreview from "@/components/MRIPreview"
import ResultsPanel from "@/components/ResultsPanel"
import PatientList from "@/components/PatientList"


export default function Home() {

  return (

    <main className="min-h-screen bg-slate-100">

      <Navbar />

      <div className="mx-auto grid max-w-7xl grid-cols-1 gap-6 p-8 lg:grid-cols-2">

        <UploadBox />

        <MRIPreview />

        <div className="lg:col-span-2">
          <ResultsPanel />
        </div>

              <div className="mx-auto max-w-6xl p-8">

        <PatientList />

      </div>

      </div>

    </main>
  )
}