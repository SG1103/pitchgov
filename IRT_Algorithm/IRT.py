import sqlite3
from openai_handling import evaluate_answer

def fetch_question(difficulty):
    conn = sqlite3.connect('test_questions_environment.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, question, correct_answer FROM questions WHERE difficulty = ?", (difficulty,))
    question_data = cursor.fetchone()
    conn.close()
    return question_data

def process_answer_and_fetch_next(question_id, submitted_answer):
    conn = sqlite3.connect('test_questions_environment.db')
    cursor = conn.cursor()
    cursor.execute("SELECT correct_answer, difficulty FROM questions WHERE id = ?", (question_id,))
    correct_answer, current_difficulty = cursor.fetchone()
    
    is_correct = (evaluate_answer(submitted_answer, correct_answer) == 'Yes')
    new_difficulty = current_difficulty + 1 if is_correct else max(current_difficulty - 1, 1)
    
    cursor.execute("SELECT id, question, correct_answer FROM questions WHERE difficulty = ?", (new_difficulty,))
    new_question_data = cursor.fetchone()
    conn.close()
    
    return new_question_data, is_correct
