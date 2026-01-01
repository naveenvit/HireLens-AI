from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import uuid
import os


def generate_pdf_report(data: dict) -> str:
    os.makedirs("reports", exist_ok=True)

    filename = f"report_{uuid.uuid4()}.pdf"
    file_path = os.path.join("reports", filename)

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 40

    def draw_line(text):
        nonlocal y
        c.drawString(40, y, text)
        y -= 20

    draw_line("AI Resume Analyzer Report")
    draw_line("-" * 50)

    draw_line(f"ATS Score: {data['ats_score']}%")
    draw_line(f"Match Level: {data['label']}")

    draw_line("")
    draw_line("Matched Skills:")
    for skill in data["matched_skills"]:
        draw_line(f"- {skill}")

    draw_line("")
    draw_line("Missing Skills:")
    for skill in data["missing_skills"]:
        draw_line(f"- {skill}")

    draw_line("")
    draw_line("Suggestions:")
    for line in data["ai_suggestions"].split("\n"):
        draw_line(line)

    c.showPage()
    c.save()

    return file_path
