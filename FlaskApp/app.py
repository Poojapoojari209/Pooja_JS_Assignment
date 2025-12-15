from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == "POST":

        id = request.form.get('id')
        uname = request.form.get('uname')
        email = request.form.get('email')
        password = request.form.get('password')

        # Connect to server
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Pooja@14',
            database='sample'
        )

        cur = conn.cursor()

        sql = "Insert into users (ID, UNAME, EMAIL, PASSWORD) values (%s, %s, %s, %s)"
        val = (id, uname, email, password)

        cur.execute(sql, val)
        cur.close()
      
        return "Successfully inserted the data"
    
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)