from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import uuid
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/")
def root():
    return {"message": "Backend running"}

@app.get("/patients")
def get_patients():
    return patients


@app.post("/upload")
async def upload_mri(file: UploadFile = File(...)):

    unique_id = str(uuid.uuid4())

    temp_nifti_path = f"temp_{unique_id}.nii.gz"
    preview_path = f"preview_{unique_id}.png"

    contents = await file.read()

    with open(temp_nifti_path, "wb") as f:
        f.write(contents)

    nii_img = nib.load(temp_nifti_path)

    image_data = nii_img.get_fdata()

    image_data = np.rot90(image_data, k=-1, axes=(0, 1))
    image_data = np.fliplr(image_data)

    corte = image_data.shape[2] // 2

    plt.figure(figsize=(6, 6))
    plt.imshow(image_data[:, :, corte], cmap="gray")
    plt.axis("off")

    plt.savefig(preview_path, bbox_inches="tight", pad_inches=0)

    plt.close()

    os.remove(temp_nifti_path)

    return {
        "preview_url": f"http://localhost:8000/preview/{preview_path}"
    }


@app.get("/preview/{image_name}")
def get_preview(image_name: str):

    return FileResponse(image_name)