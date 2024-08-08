from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_data (id INTEGER PRIMARY KEY, data TEXT)''')
    conn.commit()
    conn.close()

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO user_data (data) VALUES (?)', (data,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Route to retrieve data
@app.route('/retrieve')
def retrieve():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM user_data')
    rows = c.fetchall()
    conn.close()
    return render_template('retrieve.html', rows=rows)

if __name__ == '__main__':
    init_db()  # Initialize database
    app.run(host='0.0.0.0', port=5000)
