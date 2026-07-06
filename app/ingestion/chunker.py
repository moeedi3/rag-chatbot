def chunk_text(text):

    paragraphs = text.split("\n")

    chunks = []

    current_chunk = ""

    for para in paragraphs:

        para = para.strip()

        # skip empty lines
        if not para:
            continue

        # if new section starts (1. 2. 3. etc)
        if para[0].isdigit():

            # save old chunk first
            if current_chunk:

                chunks.append(current_chunk)

            # start new chunk
            current_chunk = para + "\n"

        else:

            # keep adding until reasonable size
            if len(current_chunk) < 800:

                current_chunk += para + "\n"

            else:

                chunks.append(current_chunk)

                current_chunk = para + "\n"

    # save last chunk
    if current_chunk:

        chunks.append(current_chunk)

    return chunks


def process_chunks(parsed_data, document_id, filename):

    final_chunks = []

    chunk_id = 1

    for item in parsed_data:

        # TEXT CHUNKS
        if item["type"] == "text":

            text_chunks = chunk_text(item["content"])

            for chunk in text_chunks:

                final_chunks.append(
                    {
                        "document_id": document_id,
                        "filename": filename,
                        "chunk_id": chunk_id,
                        "page": item["page"],
                        "type": "text",
                        "content": chunk,
                    }
                )

                chunk_id += 1

        # TABLE CHUNKS
        elif item["type"] == "table":

            final_chunks.append(
                {
                    "document_id": document_id,
                    "filename": filename,
                    "chunk_id": chunk_id,
                    "page": item["page"],
                    "type": "table",
                    "content": item["content"],
                }
            )

            chunk_id += 1

    return final_chunks
