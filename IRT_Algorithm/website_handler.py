from flask import Flask, render_template, request, jsonify
import IRT
import random

app = Flask(__name__, template_folder='frontend', static_folder='frontend')

@app.route('/')
def home():
    # Fetch the first question and its ID when the quiz starts
    question_data = IRT.fetch_question(random.randint(1, 9))  # Randomly select difficulty for demonstration
    q_id, question, _ = question_data
    return render_template('bio test.html', question=question, question_id=q_id)

@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    # Extract submitted data
    question_id = request.form.get('question_id')
    user_answer = request.form.get('answer')

    # Process the answer and get the next question
    next_question_data, answer_correct = IRT.process_answer_and_fetch_next(question_id, user_answer)
    new_question_id, next_question, _ = next_question_data

    # Return JSON response with the new question data
    return jsonify({
        'new_question_id': new_question_id,
        'new_question': next_question,
        'answer_correct': answer_correct 
    })

if __name__ == '__main__':
    app.run(debug=True)
