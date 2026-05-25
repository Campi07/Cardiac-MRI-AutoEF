import MRISliderViewer
from "@/components/viewer/slider"

interface Props {
  params: Promise<{
    id: string
  }>
}

export default async function PatientPage({
  params
}: Props) {

  const { id } = await params

  return (

    <main className="min-h-screen bg-slate-100 p-8">

      <h1 className="mb-6 text-3xl font-bold">
        Patient {id}
      </h1>

      <MRISliderViewer
        patientId={Number(id)}
      />

    </main>
  )
}