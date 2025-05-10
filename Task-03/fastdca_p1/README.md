# 🚀 DACA Chatbot API with Pydantic Validation

A **FastAPI-based chatbot API** demonstrating advanced **Pydantic models** and **validation logic**.  
This project is part of the **DACA agentic workflow learning series**.

---

## 🔧 Features

- ✅ **Type-safe** request/response validation with **Pydantic v2**
- 🔁 **Nested models** for metadata and address handling
- 🛡 **Custom field validation** using `@validator`
- 💬 **Chat endpoint** with AI-like simulated response
- ⚙️ **Query parameters**, UUID generation, and timestamp auto-injection

---

## 📦 Installation

```bash
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
uv add "fastapi[standard]" pydantic
```

---

## 🧪 Pydantic Examples

### ✅ Basic Model

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    f_name: str
    age: int
    roll_number: int
    course: str
    email: str | None = None
```

---

### 🔁 Nested Address Model

```python
from pydantic import BaseModel, EmailStr

class StdAddress(BaseModel):
    street: str
    city: str
    zip_code: int

class StdWithAddress(BaseModel):
    name: str
    f_name: str
    roll_number: int
    email: EmailStr
    address: list[StdAddress]
```

---

### 🔍 Custom Validator

```python
from pydantic import validator

@validator("name")
def name_must_be_at_least_two_chars(cls, v):
    if len(v) < 4:
        raise ValueError("Name must be at least 4 characters long")
    return v
```

---

## 🚀 FastAPI Application (`main.py`)

### 📌 Defined Endpoints

- `/` – Welcome route  
- `/users/{user_id}` – Get user by ID (with optional role)  
- `/chat/` – POST route accepting a chat message and returning a structured AI reply

---

## 🧾 Message & Metadata Models

```python
from pydantic import BaseModel, Field
from datetime import datetime, UTC
from uuid import uuid4

class Metadata(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    session_id: str = Field(default_factory=lambda: str(uuid4()))

class Message(BaseModel):
    user_id: str
    text: str
    metadata: Metadata | None = None
    tags: list[str] | None = None

class Response(BaseModel):
    user_id: str
    reply: str
    metadata: Metadata
```

---

## ▶️ Run the App

```bash
uvicorn main:app --reload
```

Visit 👉 [http://localhost:8000/docs](http://localhost:8000/docs) to test the API using Swagger UI.

---

## 👩‍💻 Author

**Amna Rafeeq** 
