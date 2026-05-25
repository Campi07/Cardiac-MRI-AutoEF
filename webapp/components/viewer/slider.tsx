"use client"

import { useEffect, useState } from "react"

import {
  getPatientSlices
} from "@/services/api"

interface Props {
  patientId:number
}

export default function MRISliderViewer({
  patientId
}:Props) {

  const [slices, setSlices] =
    useState<string[]>([])

  const [currentSlice, setCurrentSlice] =
    useState(0)

  useEffect(() => {

    async function loadSlices() {

      const data =
        await getPatientSlices(patientId)

      setSlices(data.slices)
    }

    loadSlices()

  }, [patientId])

  return (

    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <h2 className="mb-4 text-xl font-semibold">
        MRI Viewer
      </h2>

      {slices.length > 0 && (

        <>

          <img
            src={slices[currentSlice]}
            className="mx-auto rounded-xl"
          />

          <input
            type="range"
            min={0}
            max={slices.length - 1}
            value={currentSlice}
            onChange={(e)=>
              setCurrentSlice(
                Number(e.target.value)
              )
            }
            className="mt-6 w-full"
          />

        </>

      )}

    </div>
  )
}