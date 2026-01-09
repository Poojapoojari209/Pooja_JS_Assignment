from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, welcome to flask"

@app.route('/about')
def about():
    return "An About page paragraph should be a concise, engaging summary that tells your brand's story. "

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None

    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2

    return render_template('index.html', result=result)



if __name__ == '__main__':
    app.run(debug=True)
