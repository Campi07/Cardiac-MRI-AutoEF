from fastapi import (
    APIRouter,
    HTTPException
)

import numpy as np
from pathlib import Path

from app.services.nifti_service import load_nifti
from app.services.slice_service import generate_slice_png

from app.core.config import (
    BASE_DIR,
    PATIENTS_DIR
)

router = APIRouter()


@router.get("/patients/{patient_id}/animation")
def get_patient_animation(
    patient_id: int
):

    try:

        patient_name = f"patient{patient_id:03d}"

        nifti_path = (
            BASE_DIR.parent /
            "data" /
            "training" /
            patient_name /
            f"{patient_name}_4d.nii.gz"
        )

        if not nifti_path.exists():

            raise HTTPException(
                status_code=404,
                detail="4D MRI not found"
            )

        # =====================
        # Cargar MRI 4D
        # =====================

        data = load_nifti(nifti_path)


        _, _, z_dim, total_frames = data.shape

        middle_slice = z_dim // 2

        # =====================
        # Carpeta salida
        # =====================

        animation_dir = (
            PATIENTS_DIR /
            patient_name /
            "animation"
        )

        animation_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        frame_urls = []

        # =====================
        # Generar frames
        # =====================

        for t in range(total_frames):

            frame_filename = f"frame_{t:03d}.png"

            frame_path = (
                animation_dir /
                frame_filename
            )

            if not frame_path.exists():

                generate_slice_png(
                    image=data[:, :, middle_slice, t],
                    output_path=frame_path
                )

            frame_urls.append(
                f"http://127.0.0.1:8000/generated/patients/"
                f"{patient_name}/animation/{frame_filename}"
            )

        return {

            "patient": patient_name,

            "num_frames": total_frames,

            "middle_slice": middle_slice,

            "frames": frame_urls

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )