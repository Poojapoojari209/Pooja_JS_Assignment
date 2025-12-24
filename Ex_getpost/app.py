from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods= ['Get'])
def home():
    return render_template('index.html')

@app.route('/submit', methods= ['post'])
def submit():
    name = request.form['name']
    return f"hello{name}"

if __name__ == '__main__':
    app.run(debug=True)