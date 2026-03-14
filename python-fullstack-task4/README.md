# Python Full Stack - Task 4

## Features

- Role-Based Access Control (RBAC) using `users.role`
- Admin Panel: `/admin`
- Admin-only operation: `/admin/delete/<id>`
- Students CRUD (HTML)
- REST API (JSON):
  - `GET /api/students`
  - `POST /api/students`
  - `PUT /api/students/<id>`
  - `DELETE /api/students/<id>`

## Roles

- `role` column exists in the `users` table
- Default role is `user`
- After login:
  - `session['user']` is set
  - `session['role']` is set
- Admin routes are protected using `@admin_required`

## Make a user admin

1. Register a user from `/register`
2. Open SQLite and run:

```sql
UPDATE users SET role='admin' WHERE username='YOUR_USERNAME';
```

3. Logout and login again

## API examples (Postman)

Base URL: `http://127.0.0.1:5000`

### 1) GET all students

- Method: `GET`
- URL: `http://127.0.0.1:5000/api/students`
- Headers: none
- Body: none

Expected response: JSON array

---

### 2) POST add a student

- Method: `POST`
- URL: `http://127.0.0.1:5000/api/students`
- Headers:
  - `Content-Type: application/json`
- Body (raw → JSON):

```json
{
  "name": "John",
  "email": "john@example.com",
  "course": "Flask"
}
```

Expected response:

```json
{ "message": "Student added successfully" }
```

---

### 3) PUT update a student

- Method: `PUT`
- URL: `http://127.0.0.1:5000/api/students/1`
- Headers:
  - `Content-Type: application/json`
- Body (raw → JSON):

```json
{
  "name": "John Updated",
  "email": "john.updated@example.com",
  "course": "API"
}
```

Expected response:

```json
{ "message": "Student updated" }
```

---

### 4) DELETE a student

- Method: `DELETE`
- URL: `http://127.0.0.1:5000/api/students/1`
- Headers: none
- Body: none

Expected response:

```json
{ "message": "Student deleted" }
```
