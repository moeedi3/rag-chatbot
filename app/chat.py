from indexer import build_index
from retriever import search
from llm import generate_answer


def ask_question(pdf_path, question):

    # Build vector index
    index, chunks = build_index(pdf_path)


    # Retrieve relevant chunks
    retrieved_chunks = search(
        question,
        index,
        chunks
    )


    # Generate final answer
    answer = generate_answer(
        question,
        retrieved_chunks
    )


    return answer


if __name__ == "__main__":

    pdf = "data/pdfs/Enterprise_RAG_Assistant_Client_Brief.pdf"

    question = "Are there any important instructions?"


    answer = ask_question(
        pdf,
        question
    )


    print("\nFINAL ANSWER:\n")

    print(answer)