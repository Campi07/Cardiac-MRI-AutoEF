from fastapi import (
    APIRouter,
    HTTPException
)

from app.services.nifti_service import load_nifti
from app.services.slice_service import generate_slice_png

from app.core.config import (
    BASE_DIR,
    PATIENTS_DIR
)

router = APIRouter()

@router.get("/patients/{patient_id}/slices")
def get_patient_slices(
    patient_id: int
):

    try:

        patient_name = f"patient{patient_id:03d}"

        nifti_path = (
            BASE_DIR.parent /
            "data" /
            patient_name /
            f"{patient_name}_frame01.nii.gz"
        )

        if not nifti_path.exists():

            raise HTTPException(
                status_code=404,
                detail="NIfTI not found"
            )

        image_data = load_nifti(
            str(nifti_path)
        )

        patient_output_dir = (
            PATIENTS_DIR / patient_name
        )

        patient_output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        slice_urls = []

        for z in range(image_data.shape[2]):

            slice_filename = f"slice_{z}.png"

            slice_path = (
                patient_output_dir /
                slice_filename
            )

            if not slice_path.exists():

                generate_slice_png(
                    image_data[:, :, z],
                    slice_path
                )

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