from flask import Flask, request, jsonify, render_template
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from models import db, User, Product, Cart

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)


# Create tables
with app.app_context():
    db.create_all()


# FRONTEND ROUTES
@app.route('/')
def home():
    return render_template("products.html")

@app.route('/signup', methods=['GET'])
def signup_page():
    return render_template("signup.html")

@app.route('/login', methods=['GET'])
def login_page():
    return render_template("login.html")

@app.route('/products', methods=['GET'])
def products_page():
    return render_template("products.html")


@app.route('/add-product', methods=['GET'])
def add_product_page():
    return render_template("add_product.html")

@app.route('/cart', methods=['GET'])
def cart_page():
    return render_template("cart.html")


# SIGNUP API

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"msg": "Please fill all fields"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "Email already exists"}), 400

    hashed = generate_password_hash(password)
    user = User(name=name, email=email, password=hashed)

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "Signup successful"}), 201

# LOGIN API (JWT)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Invalid email or password"}), 401

    token = create_access_token(identity=str(user.id))

    return jsonify({"token": token})


# ADD PRODUCT (JWT PROTECTED)

@app.route('/product', methods=['POST'])
@jwt_required()
def add_product():
    user_id = get_jwt_identity()  # always string now
    print("JWT USER:", user_id)

    data = request.get_json()

    name = data.get("name")
    price = data.get("price")
    description = data.get("description")

    if not name or not price:
        return jsonify({"msg": "Name and price required"}), 400

    product = Product(
        name=name,
        price=price,
        description=description
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({"msg": "Product added successfully"}), 201

# PRODUCTS API

@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()

    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "description": p.description,
            "image": p.image
        } for p in products
    ])

# cart
# add to cart
@app.route('/cart/add', methods=['POST'])
@jwt_required()
def add_to_cart():
    user_id = int(get_jwt_identity())
    data = request.get_json()

    product_id = data.get("product_id")

    cart_item = Cart.query.filter_by(
        user_id=user_id,
        product_id=product_id
    ).first()

    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = Cart(
            user_id=user_id,
            product_id=product_id,
            quantity=1
        )
        db.session.add(cart_item)

    db.session.commit()
    return jsonify({"msg": "Product added to cart"})


# view cart
# view cart API
@app.route('/api/cart', methods=['GET'])
@jwt_required()
def view_cart():
    user_id = int(get_jwt_identity())

    items = Cart.query.filter_by(user_id=user_id).all()
    result = []

    for item in items:
        product = Product.query.get(item.product_id)
        result.append({
            "name": product.name,
            "price": product.price,
            "quantity": item.quantity
        })

    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True)
