import sqlite3

def setup_database():
    conn = sqlite3.connect('test_questions_environment.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            difficulty INTEGER,
            type TEXT,
            correct_answer TEXT
        )
    ''')

    # Questions with correct answers
    questions = [
        ("Describe the meaning of the term 'community'.", 1, "Short Answer", "Yes"),
        ("The organisms in this food web are said to be interdependent. Explain what is meant by this.", 2, "Short Answer", "Yes"),
        ("The information in part (b) shows some interactions and feeding relationships between different species. However, the image does not represent an entire ecosystem. Explain why.", 2, "Structured", "Yes"),
        ("After a period of drought, there was a reduction in the growth of grass. With reference to the image in part (b), explain how this would affect the population of caterpillars.", 3, "Data Response", "Yes"),
        ("Suggest how the students could choose four trees.", 2, "Structured", "Yes"),
        ("Calculate the mean number of lichens found in the quadrats from the west side of the tree.", 2, "Data Response", "Yes"),
        ("Give another method that the students could have used to measure the abundance of the lichen.", 2, "Short Answer", "Yes"),
        ("Give two abiotic factors which would impact the growth of these lichens.", 2, "Short Answer", "Yes"),
        ("State the meaning of the term 'biodiversity'.", 1, "Short Answer", "Yes"),
        ("Suggest one adjustment to the method which would help to ensure that the student collected a representative sample.", 2, "Structured", "Yes"),
        ("Identify which site has the highest biodiversity.", 2, "Data Response", "Yes"),
        ("Suggest why data could not be collected about these birds using the method from part (b).", 2, "Structured", "Yes"),
        ("Explain how their presence may have led to the biodiversity seen in the data collected.", 3, "Structured", "Yes")
    ]

    cursor.executemany('INSERT INTO questions (question, difficulty, type, correct_answer) VALUES (?, ?, ?, ?)', questions)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
