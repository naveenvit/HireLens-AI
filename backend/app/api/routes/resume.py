from fastapi import APIRouter, UploadFile, File
from app.utils.file_handler import validate_file, save_temp_file
from app.services.parser import extract_text
from app.services.cleaner import clean_text
from app.services.skill_extractor import extract_skills
import os

router = APIRouter(prefix="/resume", tags=["Resume"])


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    validate_file(file)
    path = save_temp_file(file)

    raw_text = extract_text(path)
    cleaned_text = clean_text(raw_text)
    skills = extract_skills(cleaned_text)

    os.remove(path)

    return {
        "message": "Resume processed successfully",
        "skills": skills,
        "skill_count": len(skills)
    }
