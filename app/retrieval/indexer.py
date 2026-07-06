from app.ingestion.parser import parse_document
from app.ingestion.chunker import process_chunks
from app.retrieval.embeddings import generate_embeddings
from app.retrieval.vector_store import create_index


def build_index(pdf_path, document_id, filename):

    print("GOING TO CALL PARSER")

    parsed_data = parse_document(pdf_path)

    chunks = process_chunks(parsed_data, document_id, filename)

    vectors, valid_chunks = generate_embeddings(chunks)

    index = create_index(vectors)

    return index, valid_chunks
