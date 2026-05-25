const API_URL = "http://127.0.0.1:8000"

//desde aca se va a cargar toda la informacion, solo se llamaria una funcion entonces, para usar el mismo fetch

export async function getPatients() {

  const response = await fetch(
    `${API_URL}/patients`
  )

  return response.json()
}

export async function getPatientSlices(
  patientId:number
) {

  const response = await fetch(
    `${API_URL}/patients/${patientId}/slices`
  )

  return response.json()
}

export async function uploadMRI(
  file: File
) {

  const formData = new FormData()

  formData.append("file", file)

  const response = await fetch(
    `${API_URL}/upload`,
    {
      method:"POST",
      body: formData
    }
  )

  return response.json()
}