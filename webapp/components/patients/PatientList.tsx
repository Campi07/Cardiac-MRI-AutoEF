"use client"

import { useEffect, useState } from "react"

import Link from "next/link"

import { getPatients } from "@/services/api"

interface Patient {
  id:number
  name:string
  age:number
  diagnosis:string
}

export default function PatientList() {

  const [patients, setPatients] =
    useState<Patient[]>([])

  useEffect(() => {

    async function loadPatients() {

      const data = await getPatients()

      setPatients(data)
    }

    loadPatients()

  }, [])

  return (

    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <h2 className="mb-6 text-xl font-semibold">
        Patient Database
      </h2>

      <div className="space-y-4">

        {patients.map((patient) => (

          <Link
            key={patient.id}
            href={`/dashboard/patients/${patient.id}`}
          >

            <div className="cursor-pointer rounded-xl border p-4 hover:border-blue-400 hover:bg-blue-50 transition-all">

              <h3 className="font-semibold">
                {patient.name}
              </h3>

              <p className="text-sm text-slate-500">
                Age: {patient.age}
              </p>

            </div>

          </Link>

        ))}

      </div>

    </div>
  )
}