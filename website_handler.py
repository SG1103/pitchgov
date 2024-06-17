from flask import Flask, render_template
from IRT_Algorithm import IRT

app = Flask(__name__, template_folder='frontend', static_folder='frontend')


demo_question = "This is a demo question"


@app.route('/')
def show_results():

    # Render the template from the 'websites' folder
    return render_template('bio test.html', question=demo_question)


if __name__ == '__main__':
    app.run(debug=True)

