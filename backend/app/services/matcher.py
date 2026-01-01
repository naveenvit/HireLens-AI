def match_skills(resume_skills: list, job_skills: list) -> dict:
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched = sorted(resume_set.intersection(job_set))
    missing = sorted(job_set - resume_set)

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "matched_count": len(matched),
        "missing_count": len(missing),
        "job_skill_count": len(job_set)
    }
