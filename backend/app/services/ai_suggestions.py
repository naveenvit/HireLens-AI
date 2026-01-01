from openai import OpenAI
from openai import RateLimitError
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_suggestions(missing_skills: list, job_title: str = "the role") -> str:
    if not missing_skills:
        return "Your resume already matches the job requirements very well."

    prompt = f"""
You are an ATS and resume optimization expert.

The candidate is applying for {job_title}.
They are missing the following skills: {', '.join(missing_skills)}.

Give clear, concise, ATS-friendly suggestions on:
1. Where to add these skills in the resume
2. How to phrase them in bullet points
3. What kind of experience or projects to highlight
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()

    except RateLimitError:
        # 🔥 Fallback (VERY IMPORTANT)
        return (
            "AI suggestions are temporarily unavailable due to API limits.\n\n"
            "Recommended actions:\n"
            + "\n".join(
                f"- Consider adding or highlighting experience with {skill}"
                for skill in missing_skills
            )
        )

    except Exception as e:
        return "AI suggestions could not be generated at this time."
