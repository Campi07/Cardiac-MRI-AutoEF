from fastapi import APIRouter

router = APIRouter()

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

@router.get("/patients")
def get_patients():

    return patients