import sqlite3
from OpenaiHandling import evaluate_answer

question_number = 0
responses_log = []

def fetch_question(topic, subtopic, difficulty):
    global question_number
    table_name = f"{topic}_{subtopic}"
    conn = sqlite3.connect('new_questions_environment.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, question, correct_answer FROM {table_name} WHERE difficulty = ? LIMIT 1", (difficulty,))
    question_data = cursor.fetchone()
    conn.close()
    question_number = 1  # Reset question number for new topic session
    return (*question_data, question_number)

def process_answer_and_fetch_next(topic, subtopic, question_id, submitted_answer):
    global question_number
    global responses_log 

    table_name = f"{topic}_{subtopic}"
    conn = sqlite3.connect('new_questions_environment.db')
    cursor = conn.cursor()
    
    # Fetch correct answer and difficulty of the current question
    cursor.execute(f"SELECT correct_answer, difficulty FROM {table_name} WHERE id = ?", (question_id,))
    correct_answer, current_difficulty = cursor.fetchone()
    
    # Check if the submitted answer is correct
    is_correct = (evaluate_answer(submitted_answer, correct_answer) == 'Yes')
    
    # Adjust difficulty for the next question
    new_difficulty = current_difficulty + 1 if is_correct else max(current_difficulty - 1, 1)

    # Fetch the question text for logging purposes
    cursor.execute(f"SELECT question FROM {table_name} WHERE id = ?", (question_id,))
    question = cursor.fetchone()[0]

    # Log the response
    responses_log.append([question, is_correct, current_difficulty])

    # Check if the question number limit is reached
    if question_number >= 10:
        conn.close()
        return None, question_number, is_correct    
    
    # Fetch the next question based on the new difficulty
    cursor.execute(f"SELECT id, question, correct_answer FROM {table_name} WHERE difficulty = ? LIMIT 1", (new_difficulty,))
    new_question_data = cursor.fetchone()
    conn.close()
    
    question_number += 1
    return (new_question_data, question_number, is_correct)

