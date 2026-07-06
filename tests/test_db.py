from app.database.db import get_connection

conn = get_connection()

print("CONNECTED TO NEON")

conn.close()
