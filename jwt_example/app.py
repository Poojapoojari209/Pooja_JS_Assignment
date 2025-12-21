from flask import Flask, jsonify, request
import jwt
import datetime

app = Flask(__name__)
SECRET_KEY = "mysecretkey"

# Home route
@app.route("/")
def home():
    return "Flask JWT App Running!"

# Generate JWT
@app.route("/login")
def login():
    token = jwt.encode({
        "user": "admin",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    }, SECRET_KEY, algorithm="HS256")

    return jsonify({
        "message": "JWT generated successfully",
        "token": token
    })

# Protected route
@app.route("/dashboard")
def dashboard():
    token = request.args.get("token")

    if not token:
        return "Token is missing!"

    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return f"Welcome {data['user']}! JWT is valid."
    except jwt.ExpiredSignatureError:
        return "Token expired!"
    except jwt.InvalidTokenError:
        return "Invalid token!"

if __name__ == "__main__":
    app.run(debug=True)
