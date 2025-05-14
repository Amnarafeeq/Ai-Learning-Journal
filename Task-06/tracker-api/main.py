from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, constr, field_validator
from datetime import date
from typing import Literal

app = FastAPI()

# Dummy databases
user_db = {}
task_db = {}

# ✅ User Models
class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20) # type: ignore
    email: EmailStr


class UserRead(BaseModel):
    username: constr(min_length=3, max_length=20) # type: ignore


# ✅ Task Models
class Tasks(BaseModel):
    title: str
    description: str
    due_date: date
    status: Literal["pending", "in-progress", "done"]
    user_id: int

    @field_validator("due_date")
    @classmethod
    def validate_due_date(cls, value):
        if value < date.today():
            raise ValueError("Due Date cannot be in the past")
        return value


class StatusUpdate(BaseModel):
    status: Literal["pending", "in-progress", "done"]


# ✅ USER ENDPOINTS

# Create user
@app.post("/users", response_model=UserRead)
def create_user(user: UserCreate):
    user_id = len(user_db) + 1
    user_db[user_id] = user
    return UserRead(username=user.username)


# Get user by ID
@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    user = user_db.get(user_id)
    if user:
        return UserRead(username=user.username)
    return {"error": "User not found"}


# ✅ TASK ENDPOINTS

# Create task
@app.post("/tasks", response_model=Tasks)
def create_task(task: Tasks):
    task_id = len(task_db) + 1
    task_db[task_id] = task
    return task


# Get task by ID
@app.get("/tasks/{task_id}", response_model=Tasks)
def get_task(task_id: int):
    task = task_db.get(task_id)
    if task:
        return task
    return {"error": "Task not found"}


# Update task status only
@app.put("/tasks/{task_id}")
def update_task(task_id: int, status_update: StatusUpdate):
    task = task_db.get(task_id)
    if task:
        updated_task = task.model_copy(update={"status": status_update.status})
        task_db[task_id] = updated_task
        return {"message": "Status updated", "task": updated_task}
    return {"error": "Task not found"}


# Get all tasks for a specific user
@app.get("/users/{user_id}/tasks")
def get_user_tasks(user_id: int):
    user_tasks = [task for task in task_db.values() if task.user_id == user_id]
    return user_tasks
