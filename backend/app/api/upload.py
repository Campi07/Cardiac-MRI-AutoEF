from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

import uuid
import os

from app.core.config import (
    TEMP_DIR,
    PREVIEWS_DIR
)

from app.services.nifti_service import load_nifti
from app.services.slice_service import generate_slice_png

router = APIRouter()

@router.post("/upload")
async def upload_mri(
    file: UploadFile = File(...)
):

    try:

        unique_id = str(uuid.uuid4())

        temp_nifti_path = (
            TEMP_DIR / f"{unique_id}.nii.gz"
        )

        contents = await file.read()

        with open(temp_nifti_path, "wb") as f:
            f.write(contents)

        image_data = load_nifti(
            str(temp_nifti_path)
        )

        middle_slice = image_data.shape[2] // 2

        preview_filename = f"{unique_id}.png"

        preview_path = (
            PREVIEWS_DIR / preview_filename
        )

        generate_slice_png(
            image_data[:, :, middle_slice],
            preview_path
        )

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