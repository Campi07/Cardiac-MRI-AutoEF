"use client"

import { useState } from "react"

import Navbar from "@/components/layout/Navbar"

import UploadBox from "@/components/upload/UploadBox"

import MRIPreview from "@/components/viewer/MRIPreview"

import PatientList from "@/components/patients/PatientList"

export default function Dashboard() {

  const [selectedFile, setSelectedFile] =
    useState<File | null>(null)

  const [previewUrl, setPreviewUrl] =
    useState<string | null>(null)

  return (

    <main className="min-h-screen bg-slate-100">

      <Navbar />

      <div className="mx-auto grid max-w-7xl grid-cols-1 gap-6 p-8 lg:grid-cols-2">

        <UploadBox
          onFileUpload={setSelectedFile}
          onPreviewGenerated={setPreviewUrl}
        />

        <MRIPreview
          file={selectedFile}
          patient={null}
          previewUrl={previewUrl}
        />

        <div className="lg:col-span-2">

          <PatientList />

        </div>

      </div>

    </main>
  )
}