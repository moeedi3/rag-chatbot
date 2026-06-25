from parser import parse_document
from chunker import process_chunks
from embeddings import generate_embeddings
from vector_store import create_index


def build_index(pdf_path):

    parsed_data = parse_document(pdf_path)

    chunks = process_chunks(parsed_data)

    vectors = generate_embeddings(chunks)

    index = create_index(vectors)

    return index, chunks
