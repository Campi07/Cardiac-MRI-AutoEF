import nibabel as nib
import numpy as np

def load_nifti(path: str):

    nii_img = nib.load(path)

    image_data = nii_img.get_fdata()

    image_data = np.rot90(
        image_data,
        k=-1,
        axes=(0,1)
    )

    image_data = np.fliplr(image_data)

    return image_data