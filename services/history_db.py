import sqlite3

conn = sqlite3.connect(
    "data/translation_history.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS translations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_text TEXT,
    translated_text TEXT,
    source_language TEXT,
    target_language TEXT
)
""")

conn.commit()


def save_translation(
    source_text,
    translated_text,
    source_language,
    target_language
):
    cursor.execute(
        """
        INSERT INTO translations
        (
            source_text,
            translated_text,
            source_language,
            target_language
        )
        VALUES(?,?,?,?)
        """,
        (
            source_text,
            translated_text,
            source_language,
            target_language
        )
    )

    conn.commit()


def get_history():
    cursor.execute(
        """
        SELECT *
        FROM translations
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()