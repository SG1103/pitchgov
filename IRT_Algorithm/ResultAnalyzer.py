import sqlite3
from TestManager import responses_log
from OpenaiHandling import create_report

def getresults():

    prompt = "Given the quiz data for a student, analyze the following aspects and generate a comprehensive report: 1. Calculate the total number of questions attempted and the percentage of correct answers. 2. Analyze performance trends by question difficulty, summarizing how the student's correctness rate changes with increasing difficulty levels. 3. Identify key strengths and weaknesses: Determine which difficulty levels and question topics the student handles well and which they struggle with. 4. Provide recommendations for topics the student should focus on improving based on the quiz results. 5. Optionally, include a simple textual visualization (like a bar chart made from text characters) showing the distribution of correct and incorrect answers across different difficulty levels. The data for analysis is structured as list of lists with each sublist being a question answered in the form [question, is_correct, difficulty]"

    result = str(responses_log)

    report = create_report(prompt, result)

    return report

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
