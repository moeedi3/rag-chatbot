def chunk_text(text, chunk_size=100):
    """
    Split text into chunks of fixed word size
    """

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(
            words[i:i + chunk_size]
        )

        chunks.append(chunk)

    return chunks


def process_chunks(parsed_data):

    final_chunks = []

    chunk_id = 1

    for item in parsed_data:

        # Handle text
        if item["type"] == "text":

            text_chunks = chunk_text(
                item["content"]
            )

            for chunk in text_chunks:

                final_chunks.append({

                    "chunk_id": chunk_id,

                    "page": item["page"],

                    "type": "text",

                    "content": chunk

                })

                chunk_id += 1


        # Handle table
        elif item["type"] == "table":

            final_chunks.append({

                "chunk_id": chunk_id,

                "page": item["page"],

                "type": "table",

                "content": item["content"]

            })

            chunk_id += 1

    return final_chunks

from parser import parse_document


if __name__ == "__main__":

    parsed = parse_document(
        "data/pdfs/Enterprise_RAG_Assistant_Client_Brief.pdf"
    )

    chunks = process_chunks(parsed)

    for chunk in chunks[:5]:
        print(chunk)
        print("-" * 50)