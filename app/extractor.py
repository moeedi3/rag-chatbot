import fitz
import pdfplumber


def extract_text(pdf_path):
    doc = fitz.open(pdf_path)

    results = []

    for page_num, page in enumerate(doc):
        text = page.get_text()

        results.append({
            "page": page_num + 1,
            "type": "text",
            "content": text
        })

    return results


def extract_tables(pdf_path):
    tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):

            extracted_tables = page.extract_tables()

            for table in extracted_tables:
                tables.append({
                    "page": page_num + 1,
                    "type": "table",
                    "content": table
                })

    return tables


if __name__ == "__main__":

    pdf_file = "data/pdfs/manual.pdf"

    text_data = extract_text(pdf_file)
    table_data = extract_tables(pdf_file)

    print("\nTEXT:\n")
    print(text_data[:2])

    print("\nTABLES:\n")
    print(table_data)