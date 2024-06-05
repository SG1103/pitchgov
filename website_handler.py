from flask import Flask, render_template

app = Flask(__name__, template_folder='frontend')


demo_question = "This is a demo question"


@app.route('/')
def show_results():

    # Render the template from the 'websites' folder
    return render_template('saad_test.html', question=demo_question)


if __name__ == '__main__':
    app.run(debug=True)

