import sqlite3

def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('test_questions.db')
    cursor = conn.cursor()

    # Create a table to store questions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            difficulty INTEGER
        )
    ''')

    # Insert some mock questions into the table
    questions = [
        ("What is the capital of France?", 3),
        ("Solve 5 * 7.", 1),
        ("Explain the theory of relativity.", 9),
        ("What is the boiling point of water?", 2),
        ("Translate 'Hello' to Spanish.", 3),
        ("Calculate the integral of x^2 from 0 to 1.", 7),
        ("Who wrote 'Macbeth'?", 4),
        ("Define the concept of 'gravity'.", 5),
        ("What is the chemical formula for water?", 2),
        ("Discuss the causes of World War II.", 8)
    ]

    # Insert questions into the table
    cursor.executemany('INSERT INTO questions (question, difficulty) VALUES (?, ?)', questions)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database has been created and populated with questions.")
