from app.database.document_repository import create_document
from app.database.chunk_repository import create_chunks

from app.retrieval.indexer import build_index

from app.services.index_service import rebuild_indexes
from app.database.document_repository import (
    get_all_documents,
    get_document,
    delete_document as delete_document_db,
)

from app.services.index_service import rebuild_indexes


def process_document(pdf_path, filename):

    # ==========================
    # Create document
    # ==========================

    document_id = create_document(filename)

    print(f"Document ID: {document_id}")

    # ==========================
    # Parse PDF + Build Chunks
    # ==========================

    _, chunks = build_index(pdf_path, document_id, filename)

    # ==========================
    # Save chunks
    # ==========================

    create_chunks(document_id, chunks)

    print(f"{len(chunks)} chunks saved.")

    # ==========================
    # Rebuild search indexes
    # ==========================

    rebuild_indexes()

    return {"message": "Document processed successfully"}


def get_documents():

    documents = get_all_documents()

    result = []

    for doc in documents:

        result.append({"id": doc[0], "filename": doc[1], "uploaded_at": doc[2]})

    return result


def delete_document(document_id):

    document = get_document(document_id)

    if document is None:

        return False

    delete_document_db(document_id)

    rebuild_indexes()

    return True
