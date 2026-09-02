"""Render the LocalBuka technical interview Markdown guide as a PDF."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer


PROJECT_DIR = Path(__file__).resolve().parent
SOURCE_FILE = PROJECT_DIR / "LOCALBUKA_TECHNICAL_INTERVIEW_GUIDE.md"
OUTPUT_FILE = PROJECT_DIR / "LOCALBUKA_TECHNICAL_INTERVIEW_GUIDE.pdf"


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="GuideTitle", parent=styles["Title"], alignment=TA_CENTER,
        fontName="Helvetica-Bold", fontSize=20, leading=25, textColor=colors.HexColor("#13315C"),
        spaceAfter=18,
    ))
    styles.add(ParagraphStyle(
        name="GuideH1", parent=styles["Heading1"], fontName="Helvetica-Bold",
        fontSize=15, leading=19, textColor=colors.HexColor("#13315C"), spaceBefore=14, spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="GuideBody", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=9.5, leading=13, spaceAfter=7,
    ))
    styles.add(ParagraphStyle(
        name="GuideBullet", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=9.5, leading=13, leftIndent=14, firstLineIndent=-8, spaceAfter=4,
    ))
    return styles


def convert_markdown_to_story(markdown_text, styles):
    story = []
    in_code_block = False
    code_lines = []

    for raw_line in markdown_text.splitlines():
        line = raw_line.rstrip()
        stripped_line = line.strip()
        if stripped_line.startswith("```"):
            if in_code_block:
                story.append(Preformatted("\n".join(code_lines), styles["Code"]))
                story.append(Spacer(1, 5))
                code_lines = []
            in_code_block = not in_code_block
            continue
        if in_code_block:
            code_lines.append(stripped_line)
            continue
        if not stripped_line:
            continue
        display_line = stripped_line.replace("**", "").replace("`", "")
        if display_line.startswith("# "):
            story.append(Paragraph(display_line[2:], styles["GuideTitle"]))
        elif display_line.startswith("## "):
            story.append(Paragraph(display_line[3:], styles["GuideH1"]))
        elif display_line.startswith("- "):
            story.append(Paragraph("• " + display_line[2:], styles["GuideBullet"]))
        else:
            story.append(Paragraph(display_line, styles["GuideBody"]))
    return story


def add_page_number(canvas, document):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawRightString(A4[0] - 1.5 * cm, 1.1 * cm, f"LocalBuka Technical Interview Guide | Page {document.page}")
    canvas.restoreState()


def main():
    styles = build_styles()
    document = SimpleDocTemplate(
        str(OUTPUT_FILE), pagesize=A4, rightMargin=1.5 * cm, leftMargin=1.5 * cm,
        topMargin=1.5 * cm, bottomMargin=1.7 * cm,
        title="LocalBuka Technical Interview Guide",
        author="LocalBuka Case Study Candidate",
    )
    markdown_text = SOURCE_FILE.read_text(encoding="utf-8")
    story = convert_markdown_to_story(markdown_text, styles)
    document.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"Created {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
