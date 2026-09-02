#!/usr/bin/env python3
"""Generate deduplicated German Family Reunion Visa interview questions PDF."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT

OUTPUT_PATH = "/workspace/German_Family_Reunion_Visa_Interview_Questions.pdf"

# Deduplicated questions organized by category
CATEGORIES = [
    {
        "title": "1. Personal Information",
        "questions": [
            "What is your name?",
            "What is your spouse's/wife's name?",
            "What is your contact number?",
            "What is your education/qualification?",
            "What is your spouse's education/qualification?",
            "Where do you live? (With in-laws or at your parents' house?)",
            "What is your spouse's birthday?",
            "Where was your spouse born? / Where does your spouse live?",
        ],
    },
    {
        "title": "2. Marriage & Relationship",
        "questions": [
            "Was your marriage arranged or a love marriage?",
            "How did you get to know your spouse?",
            "Did you meet your spouse before the wedding?",
            "Who arranged your marriage (rishta)?",
            "Who approached you for this marriage proposal?",
            "Who approached your spouse for this marriage proposal?",
            "Who talked to you and your spouse about this marriage proposal?",
            "Why did you accept this proposal?",
            "How many marriage proposals came before this one?",
            "Is this your first marriage?",
            "Was your spouse married before?",
            "Do you allow your husband a second marriage?",
            "What is your relationship with your in-laws?",
            "Was the wedding held within the family or outside?",
            "How long did the communication/talks go on before marriage?",
            "Did you talk after the marriage was fixed?",
            "Do you talk daily now?",
            "How do you communicate (e.g., WhatsApp, calls)?",
            "How did you actually chat?",
            "Do you mostly chat or call?",
            "How often do you talk on WhatsApp or phone calls?",
            "Is talking to your husband every day frustrating for you?",
        ],
    },
    {
        "title": "3. Wedding & Nikah Details",
        "questions": [
            "What is your marriage date?",
            "What is your Nikah date?",
            "Where did your marriage take place?",
            "In which hall did the wedding take place? / Name of the hall?",
            "Name of the hotel where Rukhsati took place?",
            "Did Nikah and Rukhsati/wedding happen on the same day or on different days?",
            "Has Rukhsati taken place, or was it only Nikah?",
            "Was your spouse present at the Nikah?",
            "Was your spouse present at the wedding/Rukhsati event?",
        ],
    },
    {
        "title": "4. Spouse in Germany – Work & Living",
        "questions": [
            "Is your husband a German national?",
            "What does your spouse do in Germany? / What is your husband's profession/job?",
            "What is your husband's salary?",
            "What type of visa does your husband have?",
            "When and how did your spouse go to Germany?",
            "On which visa did your husband go?",
            "How many rooms are in your husband's apartment/home?",
            "What is the size of your husband's apartment?",
            "Does your husband live alone or with someone?",
            "What does your husband usually do when he returns from work?",
            "When did your husband last come to Pakistan?",
            "How much time has passed since he left Pakistan?",
        ],
    },
    {
        "title": "5. Financial & Family Matters",
        "questions": [
            "Does your husband send you money? How much does he send per month?",
            "How much money do you receive per month?",
            "Are you pregnant?",
            "Do you have children? / How many children do you have?",
            "How many children did your spouse have before?",
            "Do you have any siblings living abroad? If yes, which countries are they in and on which visa did they go?",
        ],
    },
    {
        "title": "6. German Language (A1) Certificate",
        "questions": [
            "Have you completed A1?",
            "When did you obtain your A1 certificate?",
            "What are your marks in A1?",
        ],
    },
    {
        "title": "7. Critical / Scenario Questions",
        "questions": [
            "What will you do if you do not get the visa?",
            "If we still do not give you the visa, will your husband leave everything behind and come to Pakistan for you?",
            "If we reject your visa, will your husband come back to Pakistan?",
            "If we do not give you the visa, will your wife permanently come to Pakistan?",
        ],
    },
    {
        "title": "8. Qualities & Personal Preferences",
        "questions": [
            "What are the main qualities of your husband?",
            "What qualities of your wife do you like?",
            "What do you like about your husband?",
        ],
    },
    {
        "title": "9. German Language Test Questions (Asked in German)",
        "questions": [
            "How are you? (Wie geht es Ihnen?)",
            "Where did your husband live? (Wo wohnt Ihr Mann?)",
            "What is the day today? (Welcher Tag ist heute?)",
            "What will be the day tomorrow? (Welcher Tag ist morgen?)",
            "Count from 1 to 10 (Zählen Sie von 1 bis 10)",
        ],
    },
]

def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Heading1"],
        fontSize=18,
        spaceAfter=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1a365d"),
    )

    subtitle_style = ParagraphStyle(
        "CustomSubtitle",
        parent=styles["Normal"],
        fontSize=11,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#4a5568"),
    )

    category_style = ParagraphStyle(
        "CategoryTitle",
        parent=styles["Heading2"],
        fontSize=13,
        spaceBefore=16,
        spaceAfter=10,
        textColor=colors.HexColor("#2c5282"),
        borderPadding=4,
    )

    question_style = ParagraphStyle(
        "Question",
        parent=styles["Normal"],
        fontSize=10,
        spaceAfter=6,
        leftIndent=12,
        textColor=colors.HexColor("#2d3748"),
    )

    note_style = ParagraphStyle(
        "Note",
        parent=styles["Normal"],
        fontSize=9,
        spaceAfter=8,
        textColor=colors.HexColor("#718096"),
        leftIndent=12,
    )

    story = []

    story.append(Paragraph("German Family Reunion / Spouse Visa", title_style))
    story.append(Paragraph("Interview Questions – Compiled & Deduplicated", title_style))
    story.append(Spacer(1, 6))
    story.append(
        Paragraph(
            "Karachi Embassy, Pakistan | German National Cases | "
            "Compiled from multiple interview experiences (2025–2026)",
            subtitle_style,
        )
    )
    story.append(Spacer(1, 12))

    total_questions = sum(len(cat["questions"]) for cat in CATEGORIES)
    story.append(
        Paragraph(
            f"<b>Total unique questions: {total_questions}</b> across {len(CATEGORIES)} categories",
            note_style,
        )
    )
    story.append(Spacer(1, 8))

    for category in CATEGORIES:
        story.append(Paragraph(category["title"], category_style))
        for i, question in enumerate(category["questions"], 1):
            story.append(Paragraph(f"{i}. {question}", question_style))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 20))
    story.append(
        Paragraph(
            "<b>Tips for the Interview:</b>",
            ParagraphStyle(
                "TipsHeader",
                parent=styles["Heading3"],
                fontSize=11,
                textColor=colors.HexColor("#2c5282"),
            ),
        )
    )
    tips = [
        "Keep answers short, confident, and consistent — even if questions are repeated.",
        "Do not change your answer if the same question is asked multiple times.",
        "Do not speak unnecessary extra details.",
        "Be prepared for the 'what if visa is rejected' scenario questions.",
        "Bring original NADRA Marriage Registration Certificate (MRC) — soft copies may not be accepted.",
        "Visa fee (as of recent experiences): approximately 24,500 PKR — carry sufficient cash.",
        "Processing time for family reunion cases: approximately 6–12 months.",
    ]
    for tip in tips:
        story.append(Paragraph(f"• {tip}", note_style))

    doc.build(story)
    print(f"PDF created: {OUTPUT_PATH}")
    print(f"Total unique questions: {total_questions}")

if __name__ == "__main__":
    build_pdf()
