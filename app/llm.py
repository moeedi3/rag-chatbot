import ollama


def generate_answer(question, retrieved_chunks):

    # Build context from retrieved chunks
    context = ""

    for chunk in retrieved_chunks:

        if chunk["type"] == "table":
            context += str(chunk["content"]) + "\n"

        else:
            context += chunk["content"] + "\n"


    prompt = f"""
You are a document assistant.

Answer ONLY using the provided context.

Do NOT use outside knowledge.

If answer is not found in context, say exactly:

I could not find this information in the uploaded documents.

Context:
{context}

Question:
{question}

Answer:
"""


    response = ollama.chat(
        model="llama3.1:8b",   # <-- change if needed
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    return response["message"]["content"]