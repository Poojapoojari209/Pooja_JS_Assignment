from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':

        id = request.form.get('id')
        uname = request.form.get('uname')
        email = request.form.get('email')
        password = request.form.get('password')

        # Connect to server
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Pooja@14',
            database='sample'
        )

        cur = cnx.cursor()

        sql = "Insert into users (ID, UNAME, EMAIL, PASSWORD) values (%s, %s, %s, %s)"
        val = (id, uname, email, password)

        cur.execute(sql, val)
        cnx.commit()
        # cur.close()
      
        return "Successfully inserted the data"
    else:
        return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def get_user():

    cnx = mysql.connector.connect(
        host='127.0.0.1',
            port=3306,
            user='root',
            password='Pooja@14',
            database='sample'
    )
    cur = cnx.cursor()
    cur.execute(f"SELECT * FROM users")
    rows = cur.fefetvhchonel()

if __name__ == '__main__':
    app.run(debug=True)