from app.database.db import get_connection


def create_document(filename):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO documents (filename)
        VALUES (%s)
        RETURNING id;
        """,
        (filename,),
    )

    document_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()

    conn.close()

    return document_id


def get_all_documents():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            filename,
            uploaded_at
        FROM documents
        ORDER BY uploaded_at DESC;
        """)

    documents = cursor.fetchall()

    cursor.close()

    conn.close()

    return documents


def get_document(document_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            filename,
            uploaded_at
        FROM documents
        WHERE id = %s;
        """,
        (document_id,),
    )

    document = cursor.fetchone()

    cursor.close()

    conn.close()

    return document


def delete_document(document_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM documents
        WHERE id = %s;
        """,
        (document_id,),
    )

    conn.commit()

    cursor.close()

    conn.close()
