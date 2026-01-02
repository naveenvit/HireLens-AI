import re

SKILL_KEYWORDS = [
    "python", "java", "javascript", "react", "node",
    "fastapi", "django", "flask",
    "aws", "docker", "kubernetes",
    "mongodb", "mysql", "postgresql",
    "git", "github", "linux",
    "html", "css", "tailwind"
]

def extract_skills(text: str):
    text = text.lower()
    found_skills = set()

    for skill in SKILL_KEYWORDS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill)

    return sorted(found_skills)
