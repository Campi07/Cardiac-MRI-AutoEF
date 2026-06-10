from fastapi import APIRouter
from pathlib import Path

router = APIRouter()

DATASET_DIR = (
    Path(__file__).resolve().parent.parent.parent.parent
    / "data"
    / "training"
)

@router.get("/patients")
def get_patients():

    patients = []

    patient_folders = sorted(
        DATASET_DIR.glob("patient*")
    )

    for folder in patient_folders:

        patient_id = int(
            folder.name.replace("patient", "")
        )

        patients.append({

            "id": patient_id,

            "name": folder.name,

            "has_4d": (
                folder /
                f"{folder.name}_4d.nii.gz"
            ).exists()

        })

    return patients