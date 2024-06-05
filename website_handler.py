from flask import Flask, render_template, request
from IRT_Algorithm.test_taking import take_test, estimate_ability

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        user_responses = take_test()
        ability_estimate = estimate_ability(user_responses)
        return render_template('results.html', variable_1 = ability_estimate)
    else:
        return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
