"use client"

import { useEffect, useState } from "react"

interface Props {
  patientId: number | null
}

export default function AnimationViewer({
  patientId
}: Props) {

  const [frames, setFrames] = useState<string[]>([])
  const [currentFrame, setCurrentFrame] = useState(0)

  // Obtener frames desde FastAPI
  useEffect(() => {

    if (!patientId) return

    fetch(
      `http://127.0.0.1:8000/patients/${patientId}/animation`
    )
      .then((res) => res.json())
      .then((data) => {

        setFrames(data.frames)

        setCurrentFrame(0)

      })

  }, [patientId])

  // Reproducir animación
  useEffect(() => {

    if (frames.length === 0) return

    const interval = setInterval(() => {

      setCurrentFrame((prev) =>
        (prev + 1) % frames.length
      )

    }, 150)

    return () => clearInterval(interval)

  }, [frames])

  return (

    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <h2 className="mb-4 text-xl font-semibold">
        Cardiac Motion Viewer
      </h2>

      {frames.length > 0 ? (

        <img
          src={frames[currentFrame]}
          alt="Cardiac Animation"
          className="mx-auto rounded-xl"
        />

      ) : (

        <div className="flex h-64 items-center justify-center rounded-xl bg-slate-100">

          <p className="text-slate-400">
            Select a patient
          </p>

        </div>

      )}

    </div>

  )
}