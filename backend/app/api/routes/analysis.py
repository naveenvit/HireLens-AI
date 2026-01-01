from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.services.cleaner import clean_text
from app.services.skill_extractor import extract_skills
from app.services.matcher import match_skills
from app.services.scorer import calculate_ats_score, score_label
from app.services.ai_suggestions import generate_suggestions

# ✅ ROUTER MUST BE DEFINED FIRST
router = APIRouter(prefix="/analysis", tags=["Analysis"])


class SkillMatchRequest(BaseModel):
    resume_skills: List[str]
    job_skills: List[str]


@router.post("/job-skills")
def extract_job_skills(job_description: str):
    cleaned = clean_text(job_description)
    skills = extract_skills(cleaned)
    return {
        "job_skills": skills,
        "count": len(skills)
    }


@router.post("/skill-match")
def skill_match(data: SkillMatchRequest):
    return match_skills(data.resume_skills, data.job_skills)

@router.post("/ats-score")
def ats_score(data: SkillMatchRequest):
    match_result = match_skills(
        data.resume_skills,
        data.job_skills
    )

    score = calculate_ats_score(
        match_result["matched_count"],
        match_result["job_skill_count"]
    )

    return {
        "ats_score": score,
        "label": score_label(score),
        "matched_skills": match_result["matched_skills"],
        "missing_skills": match_result["missing_skills"]
    }


@router.post("/full-analysis")
def full_analysis(data: SkillMatchRequest):
    match_result = match_skills(
        data.resume_skills,
        data.job_skills
    )

    score = calculate_ats_score(
        match_result["matched_count"],
        match_result["job_skill_count"]
    )

    suggestions = generate_suggestions(
        match_result["missing_skills"]
    )

    return {
        "ats_score": score,
        "label": score_label(score),
        "matched_skills": match_result["matched_skills"],
        "missing_skills": match_result["missing_skills"],
        "ai_suggestions": suggestions
    }

from fastapi.responses import FileResponse
from app.services.pdf_generator import generate_pdf_report

@router.post("/download-report")
def download_report(data: SkillMatchRequest):
    match_result = match_skills(
        data.resume_skills,
        data.job_skills
    )

    score = calculate_ats_score(
        match_result["matched_count"],
        match_result["job_skill_count"]
    )

    report_data = {
        "ats_score": score,
        "label": score_label(score),
        "matched_skills": match_result["matched_skills"],
        "missing_skills": match_result["missing_skills"],
        "ai_suggestions": generate_suggestions(
            match_result["missing_skills"]
        )
    }

    file_path = generate_pdf_report(report_data)

    return FileResponse(
        file_path,
        media_type="application/pdf",
        filename="ATS_Report.pdf"
    )
