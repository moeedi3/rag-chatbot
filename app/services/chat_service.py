from app.database.chunk_repository import get_all_chunks

from app.retrieval.vector_store import load_index
from app.retrieval.retriever import search
from app.generation.llm import generate_answer


def ask_question(question):

    index = load_index()

    chunks = get_all_chunks()
    if len(chunks) == 0:
        return {
            "answer": "No documents have been uploaded yet. Please ask an administrator to upload documents before asking questions.",
            "sources": [],
        }

    retrieved_chunks = search(question, index, chunks)

    answer = generate_answer(question, retrieved_chunks)

    sources = []

    seen = set()

    for chunk in retrieved_chunks:

        key = (chunk["filename"], chunk["page"])

        if key not in seen:

            sources.append({"filename": chunk["filename"], "page": chunk["page"]})

            seen.add(key)

    return {"answer": answer, "sources": sources}
