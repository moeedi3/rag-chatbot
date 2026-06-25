import numpy as np

from indexer import build_index
from embeddings import model


def search(query, index, chunks, top_k=3):

    # Convert question to embedding
    query_vector = model.encode([query])

    query_vector = np.array(
        query_vector,
        dtype="float32"
    )


    # Search similar chunks
    distances, indices = index.search(
        query_vector,
        top_k
    )


    results = []


    for idx in indices[0]:

        results.append(
            chunks[idx]
        )


    return results


if __name__ == "__main__":

    index, chunks = build_index(
        "data/pdfs/Enterprise_RAG_Assistant_Client_Brief.pdf"
    )


    question = "What vector database should be used?"


    results = search(
        question,
        index,
        chunks
    )


    for result in results:

        print(result)

        print("-" * 50)