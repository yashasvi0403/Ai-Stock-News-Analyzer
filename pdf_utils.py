from fpdf import FPDF


def clean_text(value):
    if value is None:
        return ""
    if isinstance(value, list):
        value = ", ".join(str(v) for v in value)
    value = str(value)

    # Replace unsupported unicode characters
    replacements = {
        "•": "-",
        "–": "-",
        "—": "-",
        "’": "'",
        "“": '"',
        "”": '"',
        "\n\n": "\n",
    }

    for old, new in replacements.items():
        value = value.replace(old, new)

    # FPDF with core fonts works best with latin-1 safe text
    value = value.encode("latin-1", "replace").decode("latin-1")
    return value


def add_section(pdf, heading, content):
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, clean_text(heading), ln=True)

    pdf.set_font("Arial", "", 11)

    if isinstance(content, list):
        if content:
            for item in content:
                pdf.multi_cell(190, 8, clean_text(f"- {item}"))
        else:
            pdf.multi_cell(190, 8, "No data available.")
    else:
        pdf.multi_cell(190, 8, clean_text(content))

    pdf.ln(2)


def create_pdf_report(news_title, original_text, analysis_result, output_path="report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_left_margin(10)
    pdf.set_right_margin(10)

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "AI Stock Market News Analysis Report", ln=True)

    pdf.ln(4)

    add_section(pdf, "News Title:", news_title)
    add_section(pdf, "Original News:", original_text)
    add_section(pdf, "Summary:", analysis_result.get("summary", "No summary"))
    add_section(pdf, "Sentiment:", analysis_result.get("sentiment", "Unknown"))
    add_section(pdf, "Confidence:", f"{analysis_result.get('confidence', 0)}%")
    add_section(pdf, "Companies Mentioned:", analysis_result.get("companies", []))
    add_section(pdf, "Market Impact:", analysis_result.get("market_impact", "No impact available"))
    add_section(pdf, "Key Points:", analysis_result.get("key_points", []))

    pdf.output(output_path)
    return output_path