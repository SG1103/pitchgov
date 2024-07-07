from flask import Flask, render_template, request, jsonify, redirect, url_for
import TestManager
import random
from ResultAnalyzer import getresults, send_teams_message

app = Flask(__name__, template_folder='frontend', static_folder='frontend')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/biology')
def biology():
    return render_template('biology.html')

@app.route('/test')
def test():
    question_data = TestManager.fetch_question("biology", "ecology", random.randint(1, 9))
    q_id, question, correct_answer, image_path, question_number = question_data
    return render_template('test.html', question=question, question_id=q_id, question_number=question_number, image_path=image_path)

@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    question_id = int(request.form.get('question_id'))
    user_answer = request.form.get('answer')

    next_question_data, question_number, answer_correct = TestManager.process_answer_and_fetch_next("biology", "ecology", question_id, user_answer)

    if question_number > 10:
        return jsonify({'end': True, 'redirect': url_for('results')})
    
    if question_number == 3:
        send_teams_message()

    if next_question_data:
        new_question_id, next_question, correct_answer, image_path = next_question_data
    else:
        return jsonify({'error': 'No more questions available'})

    return jsonify({
        'new_question_id': new_question_id,
        'new_question': next_question,
        'answer_correct': answer_correct,
        'question_number': question_number,
        'image_path': image_path
    })

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
