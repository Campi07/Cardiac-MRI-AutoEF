"use client"

import { useEffect, useState } from "react"

import {
  getGroundTruth
} from "@/services/api"

interface Props {
  patientId: number
}

export default function GroundTruthViewer({
  patientId
}: Props) {

  const [mriSlices, setMriSlices] =
    useState<string[]>([])

  const [gtSlices, setGtSlices] =
    useState<string[]>([])

  const [currentSlice, setCurrentSlice] =
    useState(0)

useEffect(() => {

  if (!patientId) return

  async function loadData() {

    const data =
      await getGroundTruth(patientId)

    setMriSlices(data.mri)

    setGtSlices(data.groundtruth)

    setCurrentSlice(0)
  }

  loadData()

}, [patientId])

  return (

    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <h2 className="mb-6 text-xl font-semibold">
        MRI vs Ground Truth
      </h2>

      {
        mriSlices.length > 0 &&
        gtSlices.length > 0 && (

          <>
            <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">

              <div>

                <h3 className="mb-3 text-center font-medium text-slate-700">
                  MRI Original
                </h3>

                <img
                  src={mriSlices[currentSlice]}
                  alt="MRI Slice"
                  className="mx-auto rounded-xl"
                />

              </div>

              <div>

                <h3 className="mb-3 text-center font-medium text-slate-700">
                  Ground Truth
                </h3>

                <img
                  src={gtSlices[currentSlice]}
                  alt="Ground Truth Slice"
                  className="mx-auto rounded-xl"
                />

              </div>

            </div>

            <input
              type="range"
              min={0}
              max={mriSlices.length - 1}
              value={currentSlice}
              onChange={(e) =>
                setCurrentSlice(
                  Number(e.target.value)
                )
              }
              className="mt-8 w-full"
            />

            <p className="mt-2 text-center text-slate-500">

              Slice {currentSlice}

            </p>

          </>

        )
      }

    </div>

  )

}