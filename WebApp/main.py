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
    # Assume you need to load initial data for the test
    question_data = TestManager.fetch_question("biology", "ecology", random.randint(1, 9))
    q_id, question, _, question_number = question_data
    return render_template('test.html', question=question, question_id=q_id, question_number=question_number)


@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    question_id = request.form.get('question_id')
    user_answer = request.form.get('answer')

    next_question_data, question_number, answer_correct = TestManager.process_answer_and_fetch_next("biology", "ecology",question_id, user_answer)

    print(question_number)

    if question_number > 10:
        return redirect(url_for('results'))
    
    if question_number == 3:
        send_teams_message()

    new_question_id, next_question, _ = next_question_data
    
    return jsonify({
        'new_question_id': new_question_id,
        'new_question': next_question,
        'answer_correct': answer_correct,
        'question_number': question_number
    })


@app.route('/results')
def results():


    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
