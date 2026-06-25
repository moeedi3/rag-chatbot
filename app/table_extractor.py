import pdfplumber


def extract_tables(pdf_path):

    with pdfplumber.open(pdf_path) as pdf:

        for page_number, page in enumerate(pdf.pages):

            tables = page.extract_tables()

            if tables:

                print("=" * 50)
                print("PAGE:", page_number + 1)
                print("=" * 50)

                for table in tables:

                    print(table)


if __name__ == "__main__":

    extract_tables(
        "data/pdfs/Enterprise_RAG_Assistant_Client_Brief.pdf"
    )