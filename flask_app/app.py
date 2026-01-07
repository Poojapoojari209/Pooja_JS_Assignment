from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, welcome to flask"

@app.route('/about')
def about():
    return "An About page paragraph should be a concise, engaging summary that tells your brand's story, explains what you do and who you serve, and builds trust with your audience "

@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"Sum is {a + b}"

if __name__ == '__main__':
    app.run(debug=True)
