import nibabel as nib

def load_nifti(path):

    nii = nib.load(path)

    data = nii.get_fdata()

    return data, nii.header