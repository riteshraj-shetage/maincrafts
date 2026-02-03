# User Authentication System

A full-stack web application built with Python Flask featuring user registration, login, session management, and password hashing with SQLite database.

## Project Overview

This application demonstrates secure user authentication by implementing:

- User registration with password hashing
- Secure login with session management
- Protected dashboard accessible only to logged-in users
- Logout functionality
- SQLite database for persistent user storage

## Technologies Used

- **Backend**: Python + Flask
- **Frontend**: HTML, CSS
- **Database**: SQLite
- **Security**: Werkzeug (password hashing)
- **Session Management**: Flask Sessions
- **Tools**: VS Code, Browser

## Project Structure

```
maincrafts/
    python-fullstack-task2/
        ├── app.py              # Flask backend with authentication routes
        ├── setup_db.py         # Database initialization script
        ├── requirements.txt    # Python dependencies
        ├── database.db         # SQLite database (created after setup)
        ├── templates/
        │   ├── register.html   # Registration page
        │   ├── login.html      # Login page
        │   └── dashboard.html  # Protected dashboard
        └── static/
            └── style.css       # CSS styling
```

## Setup Instructions

### 1. Install Dependencies

First, ensure you have Python 3.10+ installed. Then install required packages:

```bash
pip install -r requirements.txt
```

This will install:

- Flask==3.1.2
- Werkzeug==3.1.5

### 2. Initialize Database

Run the database setup script (only once):

```bash
python setup_db.py
```

This creates `database.db` with a `users` table containing:

- `id` (Primary Key)
- `username` (Unique)
- `password` (Hashed)

### 3. Run the Application

Start the Flask server:

```bash
python app.py
```

The application will be available at: `http://127.0.0.1:5000/`

## How to Use

1. **Register**: Navigate to `http://127.0.0.1:5000/register`
   - Enter a unique username
   - Enter a password (will be hashed before storage)
   - Click "Create Account"

2. **Login**: After registration, you'll be redirected to `/login`
   - Enter your username and password
   - Click "Login"

3. **Dashboard**: After successful login, access the protected dashboard
   - Only accessible when logged in
   - Displays personalized welcome message

4. **Logout**: Click logout to end your session and return to login page

## Features

- ✅ User registration with form validation
- ✅ Secure password hashing using Werkzeug
- ✅ Session-based authentication
- ✅ Protected routes (dashboard requires login)
- ✅ SQLite database with UNIQUE constraint on username
- ✅ Login/Logout functionality
- ✅ Clean UI with CSS styling
- ✅ Automatic redirects after actions

## Security Features

- **Password Hashing**: Passwords are hashed using `generate_password_hash()` before storage
- **Session Management**: Flask sessions store logged-in user information
- **Protected Routes**: Dashboard checks for active session before access
- **Database Constraints**: UNIQUE constraint prevents duplicate usernames

## Project Flow

1. **Registration**:
   - User submits username and password
   - Password is hashed using Werkzeug
   - Data stored in SQLite database
   - Redirect to login page

2. **Login**:
   - User submits credentials
   - Backend verifies username exists
   - Password hash is validated using `check_password_hash()`
   - Session created with username
   - Redirect to dashboard

3. **Dashboard**:
   - Checks if user is in session
   - If yes: displays personalized dashboard
   - If no: redirects to login

4. **Logout**:
   - Removes user from session
   - Redirects to login page

## Database Schema

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
)
```

## Learning Outcomes

This project demonstrates:

- Flask routing and request handling (GET/POST methods)
- Password hashing and security best practices
- Session management for user authentication
- SQLite database operations with constraints
- Protected routes and access control
- Form validation and user input handling
- Template rendering with Jinja2
- Full-stack authentication workflow
- Security considerations in web development

## Future Enhancements

- Add password strength requirements
- Implement "Forgot Password" functionality
- Add email verification
- Implement role-based access control (admin/user)
- Add profile update functionality
- Implement password reset via email
- Add "remember me" checkbox
- Implement account deletion
- Add user activity logs
- Deploy to cloud platform (Heroku, AWS, etc.)
- Add CAPTCHA for bot prevention
- Implement two-factor authentication (2FA)
- Add REST API endpoints
- Implement pagination for user lists
