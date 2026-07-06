from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def generate_embeddings(chunks):

    texts = []

    valid_chunks = []

    for chunk in chunks:

        # SKIP TABLES FOR NOW
        if chunk["type"] == "table":

            continue


        texts.append(
            chunk["content"]
        )

        valid_chunks.append(
            chunk
        )


    embeddings = model.encode(
        texts
    )

    return embeddings, valid_chunks