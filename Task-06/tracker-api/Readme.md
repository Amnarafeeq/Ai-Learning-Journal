
# 📝 Task Management API

This is a **FastAPI** application that provides RESTful endpoints for managing users and their tasks. It supports user creation and task operations such as creation, status update, and retrieval.

---

## 🚀 Features

- Create and retrieve users  
- Create and retrieve tasks  
- Update task status (`pending`, `in-progress`, `done`)  
- Get all tasks for a specific user  
- Validates task due dates (cannot be in the past)

---

## 🧰 Tech Stack

- **FastAPI**: For building the API
- **Pydantic**: For data validation
- **Uvicorn**: ASGI server (used to run the app)

---

## 📦 Installation

1. **Create a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**  
   ```bash
   pip install fastapi uvicorn
   ```

3. **Run the app**  
   ```bash
   uvicorn main:app --reload
   ```

---

## 📚 API Endpoints

### 👤 Users

#### ➕ Create User
```http
POST /users
```
**Request Body:**
```json
{
  "username": "amna",
  "email": "amna@example.com"
}
```

#### 🔍 Get User
```http
GET /users/{user_id}
```

#### 📋 Get User's Tasks
```http
GET /users/{user_id}/tasks
```

---

### ✅ Tasks

#### ➕ Create Task
```http
POST /tasks
```
**Request Body:**
```json
{
  "title": "Complete Assignment",
  "description": "Finish math homework",
  "due_date": "2025-06-01",
  "status": "pending",
  "user_id": 1
}
```

#### 🔍 Get Task
```http
GET /tasks/{task_id}
```

#### 🔁 Update Task Status
```http
PUT /tasks/{task_id}
```
**Request Body:**
```json
{
  "status": "done"
}
```

---

## 🛡 Validation

- **Due Date** must not be in the past.
- **Status** must be one of `"pending"`, `"in-progress"`, or `"done"`.
- **Username** must be between 3 and 20 characters.

---

## 📎 Notes

- This project uses in-memory storage (`user_db`, `task_db`) for simplicity.
- No persistence: all data is lost when the server restarts.
- Ideal for learning and small demos.

---

## 🧑‍💻 Author

**Amna Rafeeq**
