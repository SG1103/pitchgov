from flask import Flask, render_template
import IRT
import random

app = Flask(__name__, template_folder='frontend', static_folder='frontend')


demo_question = "This is a demo question"


@app.route('/')
def show_results():

    question_data = IRT.fetch_question(random.randint(1, 9))
    q_id, question, correct_answer = question_data
    return render_template('bio test.html', question=question)


if __name__ == '__main__':
    app.run(debug=True)

