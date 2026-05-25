from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent # aca esta el root, como ruta

GENERATED_DIR = BASE_DIR / "generated"
PREVIEWS_DIR = GENERATED_DIR / "previews"
PATIENTS_DIR = GENERATED_DIR / "patients"
TEMP_DIR = BASE_DIR / "temp"

PREVIEWS_DIR.mkdir(parents=True, exist_ok=True)
PATIENTS_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR.mkdir(parents=True, exist_ok=True)