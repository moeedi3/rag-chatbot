import json
import pickle

from rank_bm25 import BM25Okapi


def create_bm25_index(chunks):

    corpus = []

    for chunk in chunks:

        # table → convert to string
        if chunk["type"] == "table":

            text = str(
                chunk["content"]
            )

        else:

            text = chunk["content"]

        tokens = text.lower().split()

        corpus.append(
            tokens
        )

    bm25 = BM25Okapi(
        corpus
    )

    return bm25


def save_bm25(bm25):

    with open(
        "storage/bm25.pkl",
        "wb"
    ) as f:

        pickle.dump(
            bm25,
            f
        )


def load_bm25():

    with open(
        "storage/bm25.pkl",
        "rb"
    ) as f:

        bm25 = pickle.load(
            f
        )

    return bm25

def bm25_search(query, bm25, chunks, top_k=5):

    query_tokens = query.lower().split()

    scores = bm25.get_scores(
        query_tokens
    )

    # get top scoring chunk indices
    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:top_k]

    results = []

    for idx in ranked_indices:

        results.append(
            chunks[idx]
        )

    return results