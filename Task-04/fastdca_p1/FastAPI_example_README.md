
# FastAPI Example - Using Parameters, Headers, Cookies, Form Data, and File Uploads

This repository provides an example FastAPI application showcasing different ways to handle parameters, headers, cookies, form data, and file uploads in a FastAPI app.

## Table of Contents
1. [Path Parameters](#path-parameters)
2. [Query Parameters](#query-parameters)
3. [Request Body](#request-body)
4. [Headers](#headers)
5. [Cookies](#cookies)
6. [Form Data](#form-data)
7. [File Uploads](#file-uploads)

## 1. Path Parameters
Path parameters are dynamic parts of the URL. They are used to capture information directly from the URL. These are commonly used to identify specific resources such as an item ID, user ID, etc.

### Example:
```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="The ID of the item")):
    return {"item_id": item_id}
```

### Usage:
- `/items/{item_id}` will retrieve the item with a specific ID.
- The `item_id` is a path parameter and will be passed directly in the URL.

---

## 2. Query Parameters
Query parameters are used to pass extra parameters in the URL after the `?`. They are typically used for filtering, sorting, or pagination.

### Example:
```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str = Query(None, min_length=3), skip: int = Query(0, ge=0), limit: int = Query(10, le=100)):
    return {"q": q, "skip": skip, "limit": limit}
```

### Usage:
- `/items/?q=search_term&skip=0&limit=10` will filter items based on the query term `q`, skip the first `0` items, and limit the results to `10` items.

---

## 3. Request Body
The request body is used to send data in POST, PUT, or PATCH requests. It is usually in JSON format and contains the data for resource creation or modification.

### Example:
```python
from fastapi import FastAPI, Body
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(...)):
    return {"item_id": item_id, "item": item}
```

### Usage:
- The client sends a JSON body with item details to update an item.

---

## 4. Headers
Headers are used to pass additional information about the request or response. Common uses include sending authentication tokens, content types, etc.

### Example:
```python
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/items/")
async def read_items(x_token: str = Header(...)):
    return {"X-Token": x_token}
```

### Usage:
- Headers like `Authorization` or `Content-Type` can be passed with each request.
- For example, an API token could be passed via the `X-Token` header.

---

## 5. Cookies
Cookies are small pieces of data stored by the client, typically used for managing user sessions.

### Example:
```python
from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get("/items/")
async def read_items(token: str = Cookie(None)):
    return {"token": token}
```

### Usage:
- Cookies can store session data like login tokens, allowing the server to identify and authenticate users.

---

## 6. Form Data
Form data is used for sending HTML form data (like `application/x-www-form-urlencoded`) in POST requests. It is commonly used for forms like login, registration, etc.

### Example:
```python
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}
```

### Usage:
- This is used when the client submits data through a form, like a login or registration form.

---

## 7. File Uploads
File uploads allow users to send files (e.g., images, documents) to the server.

### Example:
```python
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
```

### Usage:
- The `UploadFile` object allows handling file uploads in FastAPI. It can be used to save or process files uploaded by the client.

---

## How to Test

1. Clone the repository:
```bash
git clone https://github.com/your-repository-url.git
```

2. Install FastAPI and Uvicorn:
```bash
pip install fastapi uvicorn
```

3. Run the app:
```bash
uvicorn main:app --reload
```

4. Visit the interactive documentation (Swagger UI):
   Open `http://127.0.0.1:8000/docs` in your browser.

---

## Conclusion

This example demonstrates how to handle different types of parameters in FastAPI including path parameters, query parameters, request body, headers, cookies, form data, and file uploads. Each of these mechanisms is useful in specific scenarios depending on the data you need to pass or receive in an API request.

For more information, refer to the [FastAPI documentation](https://fastapi.tiangam.com/).
