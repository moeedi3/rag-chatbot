import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
# initialize client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_answer(question, retrieved_chunks):

    # =========================
    # Build context
    # =========================

    context = ""

    for chunk in retrieved_chunks:

        if chunk["type"] == "table":
            context += str(chunk["content"]) + "\n"

        else:
            context += chunk["content"] + "\n"

    # =========================
    # Prompt
    # =========================

    prompt = f"""
    Read the document text below.

    Then answer the user's question as best as possible by understanding and interpreting the text.

    You are allowed to summarize and infer information from the text.

    Document:

    {context}

    User question:

    {question}
    """
    print("\n====================")
    print("CONTEXT SENT TO GROQ")
    print("====================")
    print(context)
    # =========================
    # Groq API call
    # =========================

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=[{"role": "user", "content": prompt}]
    )
    print("\n====================")
    print("RAW GROQ RESPONSE")
    print("====================")
    print(response)
    # =========================
    # Return generated text
    # =========================

    return response.choices[0].message.content
