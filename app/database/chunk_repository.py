from app.database.db import get_connection
from psycopg2.extras import RealDictCursor

from app.database.db import get_connection


def create_chunk(document_id, page, chunk_type, content):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chunks
        (
            document_id,
            page,
            type,
            content
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s
        );
        """,
        (document_id, page, chunk_type, content),
    )

    conn.commit()

    cursor.close()

    conn.close()


def create_chunks(document_id, chunks):
    """
    Insert all chunks for one document.
    """

    conn = get_connection()

    cursor = conn.cursor()

    for chunk in chunks:

        cursor.execute(
            """
            INSERT INTO chunks
            (
                document_id,
                page,
                type,
                content
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s
            );
            """,
            (document_id, chunk["page"], chunk["type"], chunk["content"]),
        )

    conn.commit()

    cursor.close()

    conn.close()


def get_chunks_by_document(document_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            page,
            type,
            content
        FROM chunks
        WHERE document_id = %s
        ORDER BY id;
        """,
        (document_id,),
    )

    chunks = cursor.fetchall()

    cursor.close()

    conn.close()

    return chunks


def get_all_chunks():

    conn = get_connection()

    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("""
        SELECT

            chunks.id AS chunk_id,

            chunks.document_id,

            documents.filename,

            chunks.page,

            chunks.type,

            chunks.content

        FROM chunks

        JOIN documents

        ON documents.id = chunks.document_id

        ORDER BY chunks.id;
        """)

    chunks = cursor.fetchall()

    cursor.close()

    conn.close()

    return chunks
