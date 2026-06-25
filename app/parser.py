import fitz
import pdfplumber
from cleaner import clean_text


def parse_document(pdf_path):

    parsed_data = []

    # Extract text
    doc = fitz.open(pdf_path)

    for page_num, page in enumerate(doc):

        text = page.get_text()

        if text.strip():

            parsed_data.append({

                "page": page_num + 1,

                "type": "text",

                "content": clean_text(text)

            })

    # Extract tables
    with pdfplumber.open(pdf_path) as pdf:

        for page_num, page in enumerate(pdf.pages):

            tables = page.extract_tables()

            for table in tables:

                parsed_data.append({

                    "page": page_num + 1,

                    "type": "table",

                    "content": table
                })

    return parsed_data


if __name__ == "__main__":

    result = parse_document(
        "data/pdfs/Enterprise_RAG_Assistant_Client_Brief.pdf"
    )

    for item in result:
        print(item)
        print("-" * 50)