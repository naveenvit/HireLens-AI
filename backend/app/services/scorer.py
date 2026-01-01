def calculate_ats_score(matched_count: int, job_skill_count: int) -> int:
    if job_skill_count == 0:
        return 0

    score = (matched_count / job_skill_count) * 100
    return round(score)
def score_label(score: int) -> str:
    if score >= 80:
        return "Excellent Match"
    elif score >= 60:
        return "Good Match"
    elif score >= 40:
        return "Average Match"
    else:
        return "Low Match"
