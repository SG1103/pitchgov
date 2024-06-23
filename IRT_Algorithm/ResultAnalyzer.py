import sqlite3
from TestManager import responses_log

def getresults():
    return responses_log

def get_quiz_data(user_id):
    """Fetch quiz data for a specific user."""
    conn = sqlite3.connect('test_questions_environment.db')
    cursor = conn.cursor()
    # Assuming there is a table that logs user responses with user_id, question_id, is_correct, and difficulty
    cursor.execute("""
        SELECT question_id, is_correct, difficulty FROM user_responses
        WHERE user_id = ? ORDER BY response_id ASC
    """, (user_id,))
    results = cursor.fetchall()
    conn.close()
    return results

def analyze_results(user_id):
    """Analyze results and calculate grade level."""
    quiz_data = get_quiz_data(user_id)
    correct_answers = []
    incorrect_answers = []
    difficulties = []

    for idx, (question_id, is_correct, difficulty) in enumerate(quiz_data):
        if is_correct:
            correct_answers.append(question_id)
        else:
            incorrect_answers.append(question_id)

        # Only add difficulties of the last half of the questions
        if idx >= len(quiz_data) / 2:
            difficulties.append(difficulty)

    # Calculate the average difficulty of the last 50% of the questions
    if difficulties:
        average_difficulty = sum(difficulties) / len(difficulties)
    else:
        average_difficulty = 0

    return {
        "correct_answers": correct_answers,
        "incorrect_answers": incorrect_answers,
        "grade_level": average_difficulty
    }

if __name__ == "__main__":
    user_id = 1  # Example user_id
    results = analyze_results(user_id)
    print("Results:", results)
