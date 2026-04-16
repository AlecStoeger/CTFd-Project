from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)


def init_dummy_db():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE users (username TEXT, password TEXT)')
    cursor.execute(
        'INSERT INTO users VALUES ("admin", "CTF{SQL_1nj3ct10n_Succ3ss}")')
    return conn


db = init_dummy_db()


@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        user = request.form.get('username')
        pw = request.form.get('password')

        # VULNERABLE QUERY
        query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pw}'"

        try:
            cursor = db.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                message = f"Welcome back! Your flag is: {result[1]}"
            else:
                message = "Login Failed!"
        except Exception as e:
            message = f"Error: {e}"

    return render_template_string('''
        <style>
          #header {
            color: blue;
            font-size: 5rem;
          }
        </style>
      <div id="header">
        Welcome to our app!
      </div>
      <div id="hint">
        Login to your account. (Don't bother using "admin" as your username, we are
        already using that name.)
      </div>
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
        <p>{{ message }}</p>
    ''', message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
