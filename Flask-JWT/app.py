from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

from models import db, User
import config

app = Flask(__name__)
app.config.from_object(config)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
jwt = JWTManager(app)

# Create tables
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ---------------------- HOME ROUTE -------------------------
@app.route('/')
def home():
    return "Flask Authentication API is running!"


# ---------------------- REGISTER ROUTE -------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    # GET request → show simple message
    if request.method == 'GET':
        return "Use POST method to register a new user."

    # POST request → create user
    data = request.get_json()
    if not data:
        return jsonify({"msg": "Please send JSON data"}), 400

    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"msg": "Username and password required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 409

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User registered successfully!"}), 201


# ---------------------- LOGIN ROUTE -------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    # GET request → show message in browser
    if request.method == 'GET':
        return "Use POST method to login."

    # POST request → validate credentials
    data = request.get_json()
    if not data:
        return jsonify({"msg": "Please send JSON data"}), 400

    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"msg": "Username and password required"}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        return jsonify({"msg": "Login successful (session)", "user": user.username})

    return jsonify({"msg": "Invalid credentials"}), 401


# ---------------------- LOGOUT -------------------------
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"msg": "Logged out"})


# ---------------------- JWT TOKEN LOGIN -------------------------
@app.route('/token', methods=['POST'])
def token_login():
    data = request.get_json()
    if not data:
        return jsonify({"msg": "Please send JSON data"}), 400

    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"msg": "Username and password required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"msg": "Invalid credentials"}), 401

    token = create_access_token(identity=user.id)
    return jsonify(access_token=token)


# ---------------------- PROTECTED ROUTES -------------------------

@app.route('/profile', methods=['GET'])
@login_required
def profile():
    return jsonify({
        "msg": "Profile data",
        "username": current_user.username
    })


@app.route('/api/data', methods=['GET'])
@jwt_required()
def secret_data():
    return jsonify({
        "msg": "This is protected API data using JWT"
    })


# ---------------------- RUN APP -------------------------
if __name__ == "__main__":
    app.run(debug=True)
