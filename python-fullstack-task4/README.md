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

## API examples (for screenshots)

### Get all students

```bash
curl http://127.0.0.1:5000/api/students
```

### Add student

```bash
curl -X POST http://127.0.0.1:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john@example.com","course":"Flask"}'
```

### Update student (id=1)

```bash
curl -X PUT http://127.0.0.1:5000/api/students/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"John Updated","email":"john.updated@example.com","course":"API"}'
```

### Delete student (id=1)

```bash
curl -X DELETE http://127.0.0.1:5000/api/students/1
```
