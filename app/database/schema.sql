-- ============================
-- Documents Table
-- ============================

CREATE TABLE IF NOT EXISTS documents (

    id SERIAL PRIMARY KEY,

    filename TEXT NOT NULL,

    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



-- ============================
-- Chunks Table
-- ============================

CREATE TABLE IF NOT EXISTS chunks (

    id SERIAL PRIMARY KEY,

    document_id INTEGER NOT NULL,

    page INTEGER NOT NULL,

    type TEXT NOT NULL,

    content TEXT NOT NULL,

    FOREIGN KEY (document_id)

        REFERENCES documents(id)

        ON DELETE CASCADE

);