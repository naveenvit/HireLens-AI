import os
import uuid
from fastapi import UploadFile, HTTPException

ALLOWED_EXTENSIONS = {".pdf", ".docx"}
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB


def validate_file(file: UploadFile):
    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed"
        )


def save_temp_file(file: UploadFile) -> str:
    ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4()}{ext}"
    temp_path = f"temp/{filename}"

    os.makedirs("temp", exist_ok=True)

    file_bytes = file.file.read()

    if len(file_bytes) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds 2MB"
        )

    with open(temp_path, "wb") as f:
        f.write(file_bytes)

    return temp_path
