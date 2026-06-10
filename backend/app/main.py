from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import GENERATED_DIR, PATIENTS_DIR

import shutil
from contextlib import asynccontextmanager #borrar cuando se cierre fastapi


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield

    if PATIENTS_DIR.exists():

        shutil.rmtree(PATIENTS_DIR)

        PATIENTS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

from app.api import (
    upload,
    patients,
    slices,
    animation,
    groundtruth
)

app = FastAPI(
    lifespan=lifespan
)

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
app.include_router(animation.router)
app.include_router(groundtruth.router)

@app.get("/")
def root():

    return {
        "message":
        "Cardiac MRI AI Backend Running"
    }

