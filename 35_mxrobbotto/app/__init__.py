from flask import Flask, render_template, redirect, url_for, request, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contributions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            story_id INTEGER,
            user_id INTEGER,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (story_id) REFERENCES stories(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Check if the username already exists
        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Username already exists. Please choose a different username.', 'danger')
        else:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))

        conn.close()
    return render_template('register.html')

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user[1], password):
            session['user_id'] = user[0]
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

# User logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

# Homepage
@app.route('/')
@app.route('/index')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT stories.id, stories.title,
        (SELECT COUNT(*) FROM contributions WHERE story_id = stories.id AND user_id = ?) as contributed
        FROM stories
    ''', (user_id,))
    stories = cursor.fetchall()
    conn.close()
    return render_template('index.html', stories=stories, user_id=user_id)

# Create a new story
@app.route('/create_story', methods=['GET', 'POST'])
def create_story():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = session['user_id']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO stories (title, content) VALUES (?, ?)', (title, content))
        story_id = cursor.lastrowid
        cursor.execute('INSERT INTO contributions (story_id, user_id, content) VALUES (?, ?, ?)', (story_id, user_id, content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create_story.html')

# Update an existing story
@app.route('/update_story/<int:story_id>', methods=['GET', 'POST'])
def update_story(story_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT content FROM contributions WHERE story_id = ? ORDER BY timestamp DESC LIMIT 1', (story_id,))
    latest_content = cursor.fetchone()

    if request.method == 'POST':
        content = request.form['content']
        cursor.execute('INSERT INTO contributions (story_id, user_id, content) VALUES (?, ?, ?)', (story_id, user_id, content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    cursor.execute('SELECT 1 FROM contributions WHERE story_id = ? AND user_id = ?', (story_id, user_id))
    user_contributed = cursor.fetchone()
    conn.close()

    if user_contributed:
        flash('You have already contributed to this story.', 'danger')
        return redirect(url_for('index'))

    return render_template('update_story.html', story_id=story_id, latest_content=latest_content[0] if latest_content else '')

# View a story
@app.route('/view_story/<int:story_id>')
def view_story(story_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Check if the user has contributed to the story
    cursor.execute('SELECT 1 FROM contributions WHERE story_id = ? AND user_id = ?', (story_id, user_id))
    user_contributed = cursor.fetchone()

    if not user_contributed:
        flash('You can only view stories you have contributed to.', 'danger')
        return redirect(url_for('index'))

    cursor.execute('SELECT content FROM contributions WHERE story_id = ? ORDER BY timestamp', (story_id,))
    story_content = cursor.fetchall()
    conn.close()

    return render_template('view_story.html', story_id=story_id, story_content=story_content)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5001, debug=True)
