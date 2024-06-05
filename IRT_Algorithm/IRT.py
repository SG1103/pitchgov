import sqlite3
import random
import numpy as np
from openai_handling import evaluate_answer

def fetch_question(difficulty):
    conn = sqlite3.connect('test_questions_environment.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, question, correct_answer FROM questions WHERE difficulty = ?", (difficulty,))
    question_data = cursor.fetchone()  # Fetch one row
    conn.close()
    return question_data


def take_test(max_questions=10):
    difficulty = 5  # Start with a moderate difficulty level
    responses = []
    print("Answer each question with 'Yes' or 'No'.")
    for _ in range(max_questions):
        q_id, question, correct_answer = fetch_question(difficulty)  # Fetch question including difficulty
        print(f"\nQuestion ID: {q_id}, Difficulty: {difficulty}")
        print(f"Question: {question}")
        answer_student = input("Your answer: ").strip().capitalize()  # Ensure consistent capitalization
        answer = evaluate_answer(answer_student, correct_answer)
        while answer not in ['Yes', 'No']:
            print("Invalid response. Please answer 'Yes' or 'No'.")
            answer = input("Your answer (Yes/No): ").strip().capitalize()  # Ensure consistent capitalization
        
        # Adjust difficulty level based on the response
        if answer == "Yes":
            if difficulty < 9:  # Increase difficulty if not at maximum
                difficulty += 1
        else:
            if difficulty > 1:  # Decrease difficulty if not at minimum
                difficulty -= 1
        
        responses.append((q_id, answer == correct_answer, difficulty))  # Include difficulty in response tuple
    
    return responses




def estimate_ability(responses):
    num_responses = len(responses)
    num_responses_last_half = max(num_responses // 2, 1)  # Ensure at least 1 question is considered
    difficulty_last_half = [response[2] for response in responses[-num_responses_last_half:]]  # Extract difficulty levels of last half of questions
    ability_estimate = np.mean(difficulty_last_half)
    return ability_estimate


if __name__ == "__main__":
    user_responses = take_test()
    ability_estimate = estimate_ability(user_responses)  # Call the function with user_responses as argument
    print(f"Estimated Ability of the Test Taker: {ability_estimate}")
