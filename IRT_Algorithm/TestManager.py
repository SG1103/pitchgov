import sqlite3
from OpenaiHandling import evaluate_answer

question_number = 0
responses_log = []

def fetch_question(difficulty):
    global question_number
    conn = sqlite3.connect('test_questions_environment.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, question, correct_answer FROM questions WHERE difficulty = ?", (difficulty,))
    question_data = cursor.fetchone()
    conn.close()
    question_number = 1 
    return (*question_data, question_number)

def process_answer_and_fetch_next(question_id, submitted_answer):
    global question_number
    global responses_log 

    conn = sqlite3.connect('test_questions_environment.db')
    cursor = conn.cursor()
    cursor.execute("SELECT correct_answer, difficulty FROM questions WHERE id = ?", (question_id,))
    correct_answer, current_difficulty = cursor.fetchone()
    
    is_correct = (evaluate_answer(submitted_answer, correct_answer) == 'Yes')
    new_difficulty = current_difficulty + 1 if is_correct else max(current_difficulty - 1, 1)

    cursor.execute("SELECT question FROM questions WHERE id = ?", (question_id,))
    question = cursor.fetchone()

    responses_log.append([question, is_correct, current_difficulty])

    if question_number >= 10:
        conn.close()
        return None, question_number, is_correct    
    
    cursor.execute("SELECT id, question, correct_answer FROM questions WHERE difficulty = ?", (new_difficulty,))
    new_question_data = cursor.fetchone()
    conn.close()
    question_number += 1
    return (new_question_data, question_number, is_correct)