import numpy as np

from app.retrieval.embeddings import model
from app.retrieval.bm25_store import (
    load_bm25,
    bm25_search
)


def search(query, index, chunks, top_k=5):

    # ========================
    # FAISS SEARCH
    # ========================

    query_vector = model.encode(
        [query]
    )

    query_vector = np.array(
        query_vector,
        dtype="float32"
    )

    distances, indices = index.search(
        query_vector,
        top_k
    )

    faiss_results = []

    for idx in indices[0]:

        faiss_results.append(
            chunks[idx]
        )



    # ========================
    # BM25 SEARCH
    # ========================

    bm25 = load_bm25()

    bm25_results = bm25_search(
        query,
        bm25,
        chunks
    )



    # ========================
    # WEIGHTED MERGE
    # ========================

    chunk_scores = {}



    # FAISS = weight 2
    for chunk in faiss_results:

        cid = chunk["chunk_id"]

        if cid not in chunk_scores:

            chunk_scores[cid] = {

                "chunk": chunk,

                "score": 2

            }

        else:

            chunk_scores[cid]["score"] += 2



    # BM25 = weight 1
    for chunk in bm25_results:

        cid = chunk["chunk_id"]

        if cid not in chunk_scores:

            chunk_scores[cid] = {

                "chunk": chunk,

                "score": 1

            }

        else:

            chunk_scores[cid]["score"] += 1



    ranked = sorted(

        chunk_scores.values(),

        key=lambda x: x["score"],

        reverse=True
    )



    final_results = []

    for item in ranked:

        final_results.append(
            item["chunk"]
        )



    print("\nFINAL RETRIEVED CHUNKS:")

    for chunk in final_results:

        print(
            chunk["chunk_id"]
        )


    return final_results[:5]