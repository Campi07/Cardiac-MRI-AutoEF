"use client"

import { useEffect, useState } from "react"

interface Patient {
  id: number
  name: string
  age: number
  diagnosis: string
}

export default function PatientList() {

  const [patients, setPatients] = useState<Patient[]>([])

  useEffect(() => {

    fetch("http://127.0.0.1:8000/patients")
      .then((response) => response.json())
      .then((data) => {
        setPatients(data)
      })

  }, [])

  return (

    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <h2 className="mb-6 text-xl font-semibold text-slate-700">
        Patients
      </h2>

      <div className="space-y-4">

        {patients.map((patient) => (

          <div
            key={patient.id}
            className="rounded-xl border p-4 hover:bg-slate-50"
          >

            <h3 className="font-semibold text-slate-800">
              {patient.name}
            </h3>

            <p className="text-slate-500">
              Age: {patient.age}
            </p>

            <p className="text-slate-500">
              Diagnosis: {patient.diagnosis}
            </p>

          </div>

        ))}

      </div>

    </div>
  )
}