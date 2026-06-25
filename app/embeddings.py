from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def generate_embeddings(chunks):

    texts = []

    for chunk in chunks:

        # Tables become string
        if chunk["type"] == "table":

            text = str(chunk["content"])

        else:

            text = chunk["content"]

        texts.append(text)

    embeddings = model.encode(texts)

    return embeddings