from app.database.chunk_repository import get_all_chunks

from app.retrieval.embeddings import generate_embeddings

from app.retrieval.vector_store import create_index, save_index

from app.retrieval.bm25_store import create_bm25_index, save_bm25


def rebuild_indexes():

    print("\n==========================")
    print("REBUILDING SEARCH INDEXES")
    print("==========================")

    # ==========================
    # Load all chunks from DB
    # ==========================

    db_chunks = get_all_chunks()

    chunks = db_chunks

    print(f"Loaded {len(chunks)} chunks from database.")

    # ==========================
    # Generate embeddings
    # ==========================

    vectors, valid_chunks = generate_embeddings(chunks)

    print(f"Generated {len(valid_chunks)} embeddings.")

    # ==========================
    # Build FAISS
    # ==========================

    index = create_index(vectors)

    save_index(index)

    print("FAISS index updated.")

    # ==========================
    # Build BM25
    # ==========================

    bm25 = create_bm25_index(valid_chunks)

    save_bm25(bm25)

    print("BM25 index updated.")

    return valid_chunks
