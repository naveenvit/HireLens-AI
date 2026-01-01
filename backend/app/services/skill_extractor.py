import spacy

nlp = spacy.load("en_core_web_sm")

SKILL_SET = {
    "python", "java", "c++", "javascript",
    "react", "node", "fastapi", "django",
    "html", "css", "tailwind",
    "mongodb", "mysql", "postgresql",
    "aws", "docker", "kubernetes",
    "machine learning", "deep learning",
    "nlp", "data analysis",
    "git", "github", "rest api"
}
def extract_skills(text: str) -> list:
    doc = nlp(text)
    found_skills = set()

    # Check single tokens
    for token in doc:
        if token.text in SKILL_SET:
            found_skills.add(token.text)

    # Check multi-word skills
    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.strip()
        if chunk_text in SKILL_SET:
            found_skills.add(chunk_text)

    return sorted(found_skills)
