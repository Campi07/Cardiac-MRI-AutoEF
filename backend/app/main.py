from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import GENERATED_DIR

from app.api import (
    upload,
    patients,
    slices
)

app = FastAPI()

app.mount(
    "/generated",
    StaticFiles(directory=str(GENERATED_DIR)),
    name="generated"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(patients.router)
app.include_router(slices.router)

@app.get("/")
def root():

    return {
        "message":
        "Cardiac MRI AI Backend Running"
    }