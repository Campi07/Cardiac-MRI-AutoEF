export default function MRIPreview({
  file,
  patient,
  previewUrl
}: {
  file: File | null
  patient: any | null
  previewUrl: string | null
}) {

  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <h2 className="mb-4 text-xl font-semibold text-slate-700">
        MRI Preview
      </h2>

      <div className="flex h-96 items-center justify-center rounded-xl bg-slate-100 p-4">

        {previewUrl ? (

          <img
            src={previewUrl}
            alt="MRI Preview"
            className="h-full rounded-xl object-contain"
          />

        ) : file ? (

          <p className="text-emerald-600 font-medium">
            Processing MRI: <br /> {file.name}
          </p>

        ) : patient ? (

          <p className="text-blue-600 font-medium">
            Loading study for: {patient.name}
          </p>

        ) : (

          <p className="text-slate-400">
            Select a patient or upload MRI
          </p>

        )}

      </div>

    </div>
  )
}