"use client"

export default function UploadBox({
  onFileUpload,
  onPreviewGenerated
}: {
  onFileUpload: (file: File) => void
  onPreviewGenerated: (url: string) => void
}) {

  const handleFileChange = async (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {

    const file = event.target.files?.[0]

    if (!file) return

    onFileUpload(file)

    const formData = new FormData()

    formData.append("file", file)

    try {

      const response = await fetch(
        "http://localhost:8000/upload",
        {
          method: "POST",
          body: formData
        }
      )

      const data = await response.json()

      onPreviewGenerated(data.preview_url)

    } catch (error) {

      console.error("Upload error:", error)

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

      <label className="cursor-pointer rounded-xl bg-slate-800 px-6 py-3 text-white hover:bg-slate-700">

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