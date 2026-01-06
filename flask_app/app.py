from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, welcome to flask"

@app.route('/about')
def about():
    return "An About page paragraph should be a concise, engaging summary that tells your brand's story, explains what you do and who you serve, and builds trust with your audience "

if __name__ == '__main__':
    app.run(debug=True)
