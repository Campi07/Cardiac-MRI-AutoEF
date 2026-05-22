export default function UploadBox() {
  return (

    <div className="rounded-2xl border-2 border-dashed border-slate-300 bg-white p-10 text-center shadow-sm">

      <h2 className="mb-4 text-xl font-semibold text-slate-700">
        Upload Cardiac MRI
      </h2>

      <p className="mb-6 text-slate-500">
        Drag and drop .nii or .nii.gz files
      </p>

      <button className="rounded-xl bg-slate-800 px-6 py-3 text-white hover:bg-slate-700">
        Select MRI File
      </button>

    </div>
  )
}