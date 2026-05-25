"use client"

import { uploadMRI } from "@/services/api"

export default function UploadBox({

  onFileUpload,
  onPreviewGenerated

}:{
  onFileUpload:(file:File)=>void
  onPreviewGenerated:(url:string)=>void
}) {

  const handleFileChange = async (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {

    const file = event.target.files?.[0]

    if (!file) return

    onFileUpload(file)

    try {

      const data = await uploadMRI(file)

      onPreviewGenerated(
        data.preview_url
      )

    } catch(error) {

      console.error(error)
    }
  }

  return (

    <div className="rounded-2xl border-2 border-dashed border-slate-300 bg-white p-10 text-center shadow-sm">

      <h2 className="mb-4 text-xl font-semibold text-slate-700">
        Upload Cardiac MRI
      </h2>

      <p className="mb-6 text-slate-500">
        Drag and drop .nii or .nii.gz files
      </p>

      <label className="cursor-pointer rounded-xl bg-slate-800 px-6 py-3 text-white hover:bg-slate-700 transition-all">

        Select MRI File

        <input
          type="file"
          accept=".nii,.nii.gz"
          className="hidden"
          onChange={handleFileChange}
        />

      </label>

    </div>
  )
}