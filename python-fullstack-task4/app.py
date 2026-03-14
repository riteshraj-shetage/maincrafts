from functools import wraps
from flask import Flask, render_template, request, redirect, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "secure-secret-key"


def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    db = get_db()
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
        """
    )
    try:
        db.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'user'")
    except sqlite3.OperationalError:
        pass
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            course TEXT
        )
        """
    )
    db.commit()
    db.close()


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user' not in session or session.get('role') != 'admin':
            return redirect('/dashboard')
        return f(*args, **kwargs)
    return wrapper


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        db = get_db()
        db.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        db.commit()
        db.close()
        return redirect('/login')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()

        if user and check_password_hash(user['password'], password):
            session['user'] = user['username']
            session['role'] = user['role']
            db.close()
            return redirect('/dashboard')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return render_template('dashboard.html', user=session['user'], role=session.get('role'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('role', None)
    return redirect('/login')


@app.route('/admin')
@admin_required
def admin_dashboard():
    db = get_db()
    users = db.execute("SELECT id, username, role FROM users").fetchall()
    return render_template('admin.html', users=users)


@app.route('/admin/delete/<int:id>')
@admin_required
def admin_delete_student(id):
    db = get_db()
    db.execute("DELETE FROM students WHERE id = ?", (id,))
    db.commit()
    db.close()
    return redirect('/students')

# adding student management routes


@app.route('/students')
def students():
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    data = db.execute("SELECT * FROM students").fetchall()
    db.close()
    return render_template('students.html', students=data, role=session.get('role'))


@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        db = get_db()
        db.execute(
            "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
            (name, email, course)
        )
        db.commit()
        db.close()
        return redirect('/students')

    return render_template('add_student.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    student = db.execute(
        "SELECT * FROM students WHERE id = ?",
        (id,)
    ).fetchone()

    if request.method == 'POST':
        db.execute(
            "UPDATE students SET name = ?, email = ?, course = ? WHERE id = ?",
            (request.form['name'], request.form['email'],
             request.form['course'], id)
        )
        db.commit()
        db.close()
        return redirect('/students')

    db.close()
    return render_template('edit_student.html', student=student)


@app.route('/api/students', methods=['GET'])
def api_get_students():
    db = get_db()
    students = db.execute("SELECT * FROM students").fetchall()
    db.close()
    return jsonify([dict(row) for row in students])


@app.route('/api/students', methods=['POST'])
def api_add_student():
    data = request.get_json(silent=True)
    if not data or not data.get('name') or not data.get('email') or not data.get('course'):
        return jsonify({"error": "name, email, course are required"}), 400

    db = get_db()
    db.execute(
        "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
        (data['name'], data['email'], data['course'])
    )
    db.commit()
    db.close()
    return jsonify({"message": "Student added successfully"}), 201


@app.route('/api/students/<int:id>', methods=['PUT'])
def api_update_student(id):
    data = request.get_json(silent=True)
    if not data or not data.get('name') or not data.get('email') or not data.get('course'):
        return jsonify({"error": "name, email, course are required"}), 400

    db = get_db()
    existing = db.execute(
        "SELECT id FROM students WHERE id = ?", (id,)).fetchone()
    if not existing:
        db.close()
        return jsonify({"error": "Student not found"}), 404

    db.execute(
        "UPDATE students SET name=?, email=?, course=? WHERE id=?",
        (data['name'], data['email'], data['course'], id)
    )
    db.commit()
    db.close()
    return jsonify({"message": "Student updated"})


@app.route('/api/students/<int:id>', methods=['DELETE'])
def api_delete_student(id):
    db = get_db()
    existing = db.execute(
        "SELECT id FROM students WHERE id = ?", (id,)).fetchone()
    if not existing:
        db.close()
        return jsonify({"error": "Student not found"}), 404

    db.execute("DELETE FROM students WHERE id=?", (id,))
    db.commit()
    db.close()
    return jsonify({"message": "Student deleted"})


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
