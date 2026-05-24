"use client" // Añadimos esto porque ahora la página tendrá interactividad

import { useState } from "react"
import Navbar from "@/components/Navbar"
import UploadBox from "@/components/UploadBox"
import MRIPreview from "@/components/MRIPreview"
import ResultsPanel from "@/components/ResultsPanel"
import PatientList from "@/components/PatientList"
import MRISliderViewer from "@/components/slider"

export default function Home() {
  // EL CEREBRO: Aquí guardamos la memoria de la aplicación
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const [selectedPatient, setSelectedPatient] = useState<any | null>(null)
  const [previewUrl, setPreviewUrl] = useState<string | null>(null)

  return (
    <main className="min-h-screen bg-slate-100">
      <Navbar />
      <div className="mx-auto grid max-w-7xl grid-cols-1 gap-6 p-8 lg:grid-cols-2">
        
        {/* Le pasamos la función para que UploadBox pueda guardar el archivo en el cerebro */}
        <UploadBox
  onFileUpload={setSelectedFile}
  onPreviewGenerated={setPreviewUrl}
/>

        {/* Le pasamos el archivo y el paciente al visor para que sepa qué renderizar */}
        <MRIPreview file={selectedFile} patient={selectedPatient} previewUrl={previewUrl}/>

        <div className="lg:col-span-2">
          {/* El panel de resultados reaccionará a lo que estemos analizando */}
          <ResultsPanel patient={selectedPatient} />
        </div>

        <div className="lg:col-span-2 mx-auto w-full max-w-6xl p-8">
          {/* Le pasamos la función para que al hacer clic en un paciente, se guarde en el cerebro */}
          <PatientList onSelectPatient={setSelectedPatient} />
        </div>

        <div className="lg:col-span-2 mx-auto w-full max-w-6xl p-8">
                {selectedPatient && (
                <MRISliderViewer patientId={selectedPatient.id} />
                  )}
          </div>

      </div>
    </main>
  )
}