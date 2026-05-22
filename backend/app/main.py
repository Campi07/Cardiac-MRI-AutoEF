from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Cardiac MRI AI API running"
    }