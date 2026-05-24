from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import numpy as np
import nibabel as nib

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

import uuid
import os
from pathlib import Path


# =========================================================
# CONFIGURACIÓN BASE
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

GENERATED_DIR = BASE_DIR / "generated"
PREVIEWS_DIR = GENERATED_DIR / "previews"
PATIENTS_DIR = GENERATED_DIR / "patients"
TEMP_DIR = BASE_DIR / "temp"

# Crear carpetas automáticamente
PREVIEWS_DIR.mkdir(parents=True, exist_ok=True)
PATIENTS_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR.mkdir(parents=True, exist_ok=True)


# =========================================================
# FASTAPI
# =========================================================

app = FastAPI()

# Servir archivos estáticos
app.mount(
    "/generated",
    StaticFiles(directory=str(GENERATED_DIR)),
    name="generated"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# FAKE DATABASE
# =========================================================

patients = [
    {
        "id": 1,
        "name": "Patient001",
        "age": 56,
        "diagnosis": "Dilated Cardiomyopathy"
    },
    {
        "id": 2,
        "name": "Patient002",
        "age": 48,
        "diagnosis": "Normal"
    }
]


# =========================================================
# ROOT
# =========================================================

@app.get("/")
def root():
    return {
        "message": "Cardiac MRI AI Backend Running"
    }


# =========================================================
# GET PATIENTS
# =========================================================

@app.get("/patients")
def get_patients():
    return patients


# =========================================================
# UPLOAD MRI + GENERATE PREVIEW
# =========================================================

@app.post("/upload")
async def upload_mri(file: UploadFile = File(...)):

    try:

        unique_id = str(uuid.uuid4())

        # =========================
        # Guardar archivo temporal
        # =========================

        temp_nifti_path = TEMP_DIR / f"{unique_id}.nii.gz"

        contents = await file.read()

        with open(temp_nifti_path, "wb") as f:
            f.write(contents)

        # =========================
        # Cargar NIfTI
        # =========================

        nii_img = nib.load(str(temp_nifti_path))

        image_data = nii_img.get_fdata()

        # Rotaciones para correcta orientación
        image_data = np.rot90(image_data, k=-1, axes=(0, 1))
        image_data = np.fliplr(image_data)

        # Slice central
        middle_slice = image_data.shape[2] // 2

        # =========================
        # Generar preview PNG
        # =========================

        preview_filename = f"{unique_id}.png"

        preview_path = PREVIEWS_DIR / preview_filename

        plt.figure(figsize=(6, 6))

        plt.imshow(
            image_data[:, :, middle_slice],
            cmap="gray"
        )

        plt.axis("off")

        plt.savefig(
            preview_path,
            bbox_inches="tight",
            pad_inches=0
        )

        plt.close()

        # =========================
        # Eliminar archivo temporal
        # =========================

        os.remove(temp_nifti_path)

        return {
            "preview_url":
                f"http://127.0.0.1:8000/generated/previews/{preview_filename}"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================================================
# GENERATE MRI SLICES
# =========================================================

@app.get("/patients/{patient_id}/slices")
def get_patient_slices(patient_id: int):

    try:

        patient_name = f"patient{patient_id:03d}"

        nifti_path = (
            BASE_DIR.parent /
            "data" /
            patient_name /
            f"{patient_name}_frame01.nii.gz"
        )

        # Verificar existencia
        if not nifti_path.exists():

            raise HTTPException(
                status_code=404,
                detail="NIfTI file not found"
            )

        # =========================
        # Cargar MRI
        # =========================

        nii_img = nib.load(str(nifti_path))

        image_data = nii_img.get_fdata()

        # Orientación
        image_data = np.rot90(image_data, k=-1, axes=(0, 1))
        image_data = np.fliplr(image_data)

        # =========================
        # Carpeta del paciente
        # =========================

        patient_output_dir = PATIENTS_DIR / patient_name

        patient_output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        slice_urls = []

        # =========================
        # Generar slices
        # =========================

        for z in range(image_data.shape[2]):

            slice_filename = f"slice_{z}.png"

            slice_path = patient_output_dir / slice_filename

            # Generar solo si no existe
            if not slice_path.exists():

                plt.figure(figsize=(5, 5))

                plt.imshow(
                    image_data[:, :, z],
                    cmap="gray"
                )

                plt.axis("off")

                plt.savefig(
                    slice_path,
                    bbox_inches="tight",
                    pad_inches=0
                )

                plt.close()

            # URL pública
            slice_urls.append(
                f"http://127.0.0.1:8000/generated/patients/{patient_name}/{slice_filename}"
            )

        return {
            "patient": patient_name,
            "num_slices": len(slice_urls),
            "slices": slice_urls
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )