# User Management Web Application

A simple full-stack web application built with Python Flask, HTML, CSS, and SQLite for managing user details.

## Project Overview

This application demonstrates the fundamentals of full-stack web development by creating a user management system where you can:
- Add new user details (name and email)
- View all users in a styled table
- Store data permanently in a SQLite database

## Technologies Used

- **Backend**: Python + Flask
- **Frontend**: HTML, CSS
- **Database**: SQLite
- **Tools**: VS Code, Browser

## Project Structure

```
maincrafts/
├── app.py              # Flask backend application
├── setup_db.py         # Database initialization script
├── requirements.txt    # Python dependencies
├── database.db         # SQLite database (created after setup)
├── templates/
│   └── index.html      # HTML template with form and table
└── static/
    └── style.css       # CSS styling
```

## Setup Instructions

### 1. Install Dependencies

First, ensure you have Python 3.10+ installed. Then install Flask:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install flask
```

### 2. Initialize Database

Run the database setup script (only once):

```bash
python setup_db.py
```

This creates `database.db` with a `users` table.

### 3. Run the Application

Start the Flask server:

```bash
python app.py
```

The application will be available at: `http://127.0.0.1:5000/`

## How to Use

1. Open your browser and navigate to `http://127.0.0.1:5000/`
2. Fill in the form with a name and email
3. Click "Add User" to submit
4. View all added users in the table below the form

## Features

- ✅ User input form with validation
- ✅ POST request handling to store data
- ✅ SQLite database for persistent storage
- ✅ Display all users in a styled table
- ✅ Clean, modern UI with CSS styling
- ✅ Automatic page redirect after submission

## Project Flow

1. **Frontend (HTML)**: User enters name and email in the form
2. **Backend (Flask)**: Receives POST request with form data
3. **Database (SQLite)**: Stores user data in the `users` table
4. **Display**: Fetches all users from database and displays them

## Learning Outcomes

This project demonstrates:
- Python full-stack architecture
- How frontend, backend, and database connect
- Flask routing and request handling
- SQLite database operations
- Template rendering with Jinja2
- Form submission and data validation

## Future Enhancements

- Add update/delete user functionality
- Implement user authentication
- Add search and filter features
- Deploy to cloud platform (Heroku, AWS, etc.)
- Add REST API endpoints
- Implement pagination for large datasets

## Contact

For more information, visit: www.maincrafts.com
Email: hr@maincrafts.com
