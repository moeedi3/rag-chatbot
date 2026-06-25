import fitz
from cleaner import clean_text


def extract_text(pdf_path):
    doc = fitz.open(pdf_path)

    for page_num, page in enumerate(doc):

        print("=" * 40)
        print("PAGE:", page_num + 1)
        print("=" * 40)

        text = page.get_text()

        cleaned = clean_text(text)

        print(cleaned)


if __name__ == "__main__":
    extract_text("data/pdfs/Enterprise_RAG_Assistant_Client_Brief.pdf")