from app.services.chat_service import ask_question


if __name__ == "__main__":

    pdf = "data/pdfs/Enterprise_RAG_Assistant_Client_Brief.pdf"

    question = "What vector database should be used?"


    answer = ask_question(
        pdf,
        question
    )

    print("\nANSWER:\n")

    print(answer)