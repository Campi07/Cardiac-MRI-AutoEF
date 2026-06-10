from fastapi import (
    APIRouter,
    HTTPException
)

from app.services.nifti_service import (
    load_nifti
)

from app.services.slice_service import (
    generate_slice_png
)

from app.core.config import (
    BASE_DIR,
    PATIENTS_DIR
)

router = APIRouter()


@router.get(
    "/patients/{patient_id}/groundtruth"
)
def get_groundtruth(
    patient_id: int
):

    patient_name = (
        f"patient{patient_id:03d}"
    )

    # =========================
    # MRI ORIGINAL
    # =========================

    mri_path = (
        BASE_DIR.parent /
        "data" /
        "training" /
        patient_name /
        f"{patient_name}_frame01.nii.gz"
    )

    if not mri_path.exists():

        raise HTTPException(
            status_code=404,
            detail="MRI not found"
        )

    # =========================
    # GROUND TRUTH
    # =========================

    gt_path = (
        BASE_DIR.parent /
        "data" /
        "training" /
        patient_name /
        f"{patient_name}_frame01_gt.nii.gz"
    )

    if not gt_path.exists():

        raise HTTPException(
            status_code=404,
            detail="Ground Truth not found"
        )

    mri_data = load_nifti(mri_path)

    gt_data = load_nifti(gt_path)

    # =========================
    # CARPETAS DE SALIDA
    # =========================

    mri_dir = (
        PATIENTS_DIR /
        patient_name /
        "comparison" /
        "mri"
    )

    gt_dir = (
        PATIENTS_DIR /
        patient_name /
        "comparison" /
        "groundtruth"
    )

    mri_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    gt_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    mri_urls = []

    gt_urls = []

    # =========================
    # GENERAR PNGs
    # =========================

    num_slices = mri_data.shape[2]

    for z in range(num_slices):

        # MRI

        mri_filename = f"slice_{z}.png"

        mri_output = (
            mri_dir /
            mri_filename
        )

        if not mri_output.exists():

            generate_slice_png(
                mri_data[:, :, z],
                mri_output
            )

        mri_urls.append(

            f"http://127.0.0.1:8000/generated/patients/"
            f"{patient_name}/comparison/mri/"
            f"{mri_filename}"

        )

        # Ground Truth

        gt_filename = f"mask_{z}.png"

        gt_output = (
            gt_dir /
            gt_filename
        )

        if not gt_output.exists():

            generate_slice_png(
                gt_data[:, :, z],
                gt_output
            )

        gt_urls.append(

            f"http://127.0.0.1:8000/generated/patients/"
            f"{patient_name}/comparison/groundtruth/"
            f"{gt_filename}"

        )

    return {

        "patient": patient_name,

        "num_slices": num_slices,

        "mri": mri_urls,

        "groundtruth": gt_urls

    }