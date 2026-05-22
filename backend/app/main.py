from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir conexión con frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fake database
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