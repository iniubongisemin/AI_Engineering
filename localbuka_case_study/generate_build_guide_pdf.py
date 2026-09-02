"""Generate a code-first LocalBuka build-from-scratch PDF guide."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer


PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = PROJECT_DIR / "LOCALBUKA_BUILD_FROM_SCRATCH_GUIDE.pdf"


STEPS = [
    (
        "Step 1 — Create the package and install dependencies",
        "Create the folders shown below. The two __init__.py files allow Python to run the project as modules from the repository root. Install the dependencies, then create a root .env file with your two real API keys. Do not place the key values in source code or commit .env.",
        "Project structure and setup commands",
        """localbuka_case_study/
  __init__.py
  localbuka/
    __init__.py
    models.py
    data.py
    embeddings.py
    pine_cone.py
    recommender.py
    assistant.py
    cli.py
  tests/
    test_localbuka.py
  ingest.py
  run_examples.py
  requirements.txt

python3 -m pip install google-genai==2.20.0 pinecone==9.1.0 python-dotenv==1.2.2 reportlab==5.0.1

# .env at the AI_Engineering root — never commit this file
GEMINI_API_KEY=your_gemini_key
PINECONE_API_KEY=your_pinecone_key""",
    ),
    (
        "Step 2 — Define the data models",
        "Write this file first because the rest of the application shares these objects. Dish represents an item on a menu. UserPreferences represents what the user asked for. Recommendation represents an item after retrieval. PRICE_ORDER makes price comparisons explicit; the two validation lists prevent unsupported filters from being sent to the services.",
        "localbuka/models.py",
        None,
    ),
    (
        "Step 3 — Add the Nigeria-first sample catalogue",
        "This file gives the prototype its data. The dish helper makes the 24 records easier to read. Store city, cuisine, price, dietary tags, and spice as structured data because they are safety/product constraints. Keep the description because it provides semantic context for Gemini embeddings.",
        "localbuka/data.py",
        None,
    ),
    (
        "Step 4 — Create the Gemini embedding client",
        "GeminiEmbedder is the only class that calls the Gemini embedding API. The 768-dimensional output is chosen deliberately and must match the Pinecone index dimension in the next step. embed_texts embeds each record in a loop to guarantee one vector per dish. embed_one_text returns one vector for a search query, preventing an accidental list-of-vectors error.",
        "localbuka/embeddings.py",
        None,
    ),
    (
        "Step 5 — Create the Pinecone vector-store wrapper",
        "This class owns index setup, upserts, and searches. _create_index_if_needed makes the operation safe to run more than once. The upsert method writes the Gemini vector plus structured metadata. The search method uses city, cuisine, and maximum price as deterministic Pinecone filters; semantic similarity then ranks the remaining candidates. Dietary tags are intentionally checked again later in Python.",
        "localbuka/pine_cone.py",
        None,
    ),
    (
        "Step 6 — Build ingestion",
        "dish_to_text turns each structured dish into one rich text description for Gemini. main creates the two service clients, builds a text for every catalogue record, embeds those texts, and upserts the results. Run this one-time setup after creating or changing data.py. In production, trigger this only for changed dishes rather than re-embedding the entire catalogue.",
        "ingest.py",
        None,
    ),
    (
        "Step 7 — Build the recommendation workflow",
        "Recommender coordinates the search. Constructor injection of catalogue, embedder, and restaurant_index is deliberate: it allows tests to use fake services. recommend validates filters, enriches the query with prior-order names, embeds the query, asks Pinecone for extra candidates, then performs a final dietary check. The display score is primarily semantic similarity, with a very small popularity tiebreaker.",
        "localbuka/recommender.py",
        None,
    ),
    (
        "Step 8 — Build the conversational parser",
        "FoodAssistant is bounded rather than generative. The term dictionaries translate a small known vocabulary such as cheap to budget and spicy to hot. reply guards against unavailable restaurant facts, parse_preferences creates a UserPreferences object, and the helpers keep the parsing readable. This design is safer than allowing an LLM to invent hours, delivery coverage, or allergen claims.",
        "localbuka/assistant.py",
        None,
    ),
    (
        "Step 9 — Add the command-line entry point",
        "main creates objects in dependency order: GeminiEmbedder, PineconeRestaurantIndex, Recommender, then FoodAssistant. It asks for a city once so near me can become an explicit filter. The loop reads user requests until quit or exit is entered.",
        "localbuka/cli.py",
        None,
    ),
    (
        "Step 10 — Add three live example scenarios",
        "This script demonstrates that different preferences produce different recommendations. It calls the real embedding and vector services, so the index must already be ingested and keys must be configured. Use it as a live demo after the unit tests.",
        "run_examples.py",
        None,
    ),
    (
        "Step 11 — Add offline tests",
        "The FakeEmbedder and FakeRestaurantIndex have the same methods as the real services but make no network calls. This isolates application logic from cost and service availability. These tests protect parsing, query construction, dietary rechecking, and safe refusals.",
        "tests/test_localbuka.py",
        None,
    ),
    (
        "Step 12 — Run the complete application",
        "Run the commands in this order from the AI_Engineering repository root. Ingestion creates or refreshes the 24 vectors. Tests prove the local logic without APIs. The examples and CLI use Gemini and Pinecone. If you see a dimension error, confirm that Gemini's output_dimensionality and the Pinecone index dimension are both 768, and that you passed one vector rather than a list of vectors.",
        "Verification commands",
        """# One-time or after changing localbuka/data.py
python3 -m localbuka_case_study.ingest

# Offline tests; no Gemini or Pinecone API calls
cd localbuka_case_study
python3 -m unittest discover -s tests -v
cd ..

# Three live scenarios
python3 -m localbuka_case_study.run_examples

# Interactive chat
python3 -m localbuka_case_study.localbuka.cli

# Example interaction
Type your city: Lagos
Type what you want to eat: I want something spicy and cheap near me

# Safety check
Type what you want to eat: What are the opening hours?""",
    ),
]


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="GuideTitle", parent=styles["Title"], alignment=TA_CENTER,
        fontName="Helvetica-Bold", fontSize=20, leading=25,
        textColor=colors.HexColor("#13315C"), spaceAfter=18,
    ))
    styles.add(ParagraphStyle(
        name="GuideHeading", parent=styles["Heading1"], fontName="Helvetica-Bold",
        fontSize=14, leading=18, textColor=colors.HexColor("#13315C"),
        spaceBefore=8, spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="GuideBody", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=9.5, leading=13, spaceAfter=7,
    ))
    styles.add(ParagraphStyle(
        name="CodeCaption", parent=styles["BodyText"], fontName="Helvetica-Bold",
        fontSize=10, leading=13, textColor=colors.HexColor("#333333"), spaceBefore=6, spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name="GuideNote", parent=styles["BodyText"], fontName="Helvetica-Oblique",
        fontSize=8.5, leading=12, textColor=colors.HexColor("#555555"), spaceAfter=8,
    ))
    styles["Code"].fontName = "Courier"
    styles["Code"].fontSize = 6.7
    styles["Code"].leading = 8.2
    styles["Code"].leftIndent = 5
    styles["Code"].backColor = colors.HexColor("#F4F6F8")
    return styles


def source_for_step(file_name, fallback_code):
    if fallback_code is not None:
        return fallback_code
    return (PROJECT_DIR / file_name).read_text(encoding="utf-8")


def add_page_number(canvas, document):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawRightString(A4[0] - 1.5 * cm, 1.1 * cm, f"LocalBuka Build-from-Scratch Guide | Page {document.page}")
    canvas.restoreState()


def main():
    styles = build_styles()
    document = SimpleDocTemplate(
        str(OUTPUT_FILE), pagesize=A4, rightMargin=1.4 * cm, leftMargin=1.4 * cm,
        topMargin=1.4 * cm, bottomMargin=1.7 * cm,
        title="LocalBuka Build-from-Scratch Guide",
        author="LocalBuka Case Study Candidate",
    )
    story = [
        Paragraph("LocalBuka Build-from-Scratch Guide", styles["GuideTitle"]),
        Paragraph(
            "This is a code-first guide. Follow the steps in order and type the shown code into the named files. "
            "The explanations state why each implementation exists and how the pieces work together.",
            styles["GuideBody"],
        ),
    ]

    for position, (heading, explanation, file_name, fallback_code) in enumerate(STEPS):
        if position:
            story.append(PageBreak())
        story.append(Paragraph(heading, styles["GuideHeading"]))
        story.append(Paragraph(explanation, styles["GuideBody"]))
        story.append(Paragraph(f"Code to create: {file_name}", styles["CodeCaption"]))
        code = source_for_step(file_name, fallback_code).replace("😇", "")
        story.append(Preformatted(code, styles["Code"]))
        story.append(Spacer(1, 8))
        story.append(Paragraph(
            "Reasoning checkpoint: Do not move to the next step until this code is saved in the stated location. "
            "The next implementation depends on the names and interfaces defined here.",
            styles["GuideNote"],
        ))

    document.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"Created {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
