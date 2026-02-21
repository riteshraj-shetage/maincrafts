# Python Full Stack - Task 3 (Flask CRUD + SQLite)

## Objective

Extend the Task-2 Flask authentication project with a database-driven CRUD module using SQLite.
Only logged-in users can access CRUD routes.

## Features (Task-3)

- Login-required CRUD for **Students**
  - Create: Add a new student
  - Read: View all students
  - Update: Edit student details
  - Delete: Delete a student
- Data stored permanently in **SQLite** (`database.db`)
- Session-based access control (Flask sessions)

## Project Structure

- `app.py` - Flask app (auth + CRUD)
- `database.db` - SQLite database
- `templates/` - HTML templates
- `static/style.css` - basic styling

## How to Run

1. Open terminal and go to this folder:

   ```bash
   cd python-fullstack-task3
   ```

2. (Optional) Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open in browser:
   - `http://127.0.0.1:5000/register`

## Routes

### Authentication

- `/register` (GET, POST)
- `/login` (GET, POST)
- `/dashboard` (GET) - protected
- `/logout` (GET)

### Students CRUD (all protected)

- `/students` (GET)
- `/add-student` (GET, POST)
- `/edit/<id>` (GET, POST)
- `/delete/<id>` (GET)

## Security Rule (Mandatory)

Direct access to CRUD routes without login redirects to `/login`.
