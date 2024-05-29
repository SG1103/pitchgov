import sqlite3
from pyirt import irt


#doesnt work need C## installation

# Establish a connection to the database
conn = sqlite3.connect('path_to_your_database.db')
cursor = conn.cursor()

# Function to retrieve questions based on difficulty
def fetch_questions(min_difficulty, max_difficulty):
    cursor.execute("SELECT id, question FROM questions WHERE difficulty BETWEEN ? AND ?", (min_difficulty, max_difficulty))
    return cursor.fetchall()

# Simulate an IRT model function to determine user ability
def estimate_ability(responses):
    src_dict = {}
    for idx, (q_id, answer) in enumerate(responses):
        # Assume '1' means correct, and '0' means incorrect
        src_dict[idx] = {'q': str(q_id), 'a': answer}
    
    irt_model = irt(src_dict)
    irt_model.solve()
    return irt_model.theta

# Example usage: Fetching medium difficulty questions (4-6)
questions = fetch_questions(4, 6)

# Simulate answers (1: correct, 0: incorrect)
responses = [(q_id, 1) for q_id, _ in questions[:5]] + [(q_id, 0) for q_id, _ in questions[5:]]

# Estimate ability of the test taker
estimated_ability = estimate_ability(responses)
print("Estimated Ability of the Test Taker:", estimated_ability)
