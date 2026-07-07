import faiss

from app.database.chunk_repository import get_all_chunks

from app.retrieval.embeddings import generate_embeddings

from app.retrieval.vector_store import create_index, save_index

from app.retrieval.bm25_store import create_bm25_index, save_bm25

EMBEDDING_DIM = 384


def rebuild_indexes():

    print("\n==========================")
    print("REBUILDING SEARCH INDEXES")
    print("==========================")

    db_chunks = get_all_chunks()

    chunks = db_chunks

    print(f"Loaded {len(chunks)} chunks from database.")

    # ✅ Nothing left in database
    if len(chunks) == 0:

        print("No chunks remaining.")

        # Save empty FAISS index
        empty_index = faiss.IndexFlatL2(EMBEDDING_DIM)
        save_index(empty_index)

        # Save empty BM25
        save_bm25(None)

        print("Indexes cleared.")

        return []

    vectors, valid_chunks = generate_embeddings(chunks)

    print(f"Generated {len(valid_chunks)} embeddings.")

    index = create_index(vectors)

    save_index(index)

    print("FAISS index updated.")

    # ✅ Don't build BM25 if there are no chunks
    if len(valid_chunks) == 0:

        print("No chunks remaining. Saving empty BM25.")

        save_bm25(None)

        return []

    bm25 = create_bm25_index(valid_chunks)

    save_bm25(bm25)

    print("BM25 index updated.")

    return valid_chunks
