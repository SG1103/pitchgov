import sqlite3
import random

def fetch_questions(number_of_questions):
    conn = sqlite3.connect('test_questions_environment.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, question, difficulty, type, correct_answer FROM questions")
    all_questions = cursor.fetchall()
    selected_questions = random.sample(all_questions, number_of_questions)
    conn.close()
    return selected_questions

def take_test():
    questions = fetch_questions(10)  # Fetch 10 random questions
    responses = []
    print("Answer each question with 'Yes' or 'No'.")
    for q in questions:
        print(f"\nQuestion: {q[1]} (Type: {q[3]}, Difficulty: {q[2]})")
        answer = input("Your answer (Yes/No): ").strip().capitalize()  # Ensure consistent capitalization
        while answer not in ['Yes', 'No']:
            print("Invalid response. Please answer 'Yes' or 'No'.")
            answer = input("Your answer (Yes/No): ").strip().capitalize()  # Ensure consistent capitalization
        responses.append((q[0], answer == q[4]))  # Store tuple of question ID and whether the response was correct
    return responses

def estimate_ability(responses):
    correct_count = sum(1 for _, is_correct in responses if is_correct)
    total_questions = len(responses)
    probability_of_correct_response = correct_count / total_questions
    # Assuming ability lies between 0 and 1 (a probability)
    ability_estimate = probability_of_correct_response
    return ability_estimate

if __name__ == "__main__":
    user_responses = take_test()
    ability_estimate = estimate_ability(user_responses)
    print(f"Estimated Ability of the Test Taker: {ability_estimate}")Yes
    