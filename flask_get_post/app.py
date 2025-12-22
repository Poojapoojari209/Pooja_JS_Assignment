from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", user = "Sachin") 

@app.route('/contact')
def contact():
    return render_template("contact.html", email="sachin123@gmail.com", phone="1234567890")

@app.route('/about')
def about():

    details = {
        "email": "sachin123@gmail.com",
        "phone": "1234567890",
       "course": ["mern","django"]
    }
    return render_template("about.html", details=details)

app.run(debug=True)
