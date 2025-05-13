# 🚀 AI Agents Workforce API

This FastAPI project showcases different types of dependency injections, dynamic responses using path and query parameters, mock login, and reusable class-based logic for fetching data. It simulates AI blog and user management for demonstration purposes.

---

## 📂 Features

### ✅ 1. Simple Dependency Injection

Injects a static goal message using a simple function.

**Endpoint:** `/get-simple-goal`

**Response:**
```json
{ "goal": "We are building AI Agents Workforce" }
```

---

### ✅ 2. Parameterized Dependency

Accepts a `username` and includes it in the response.

**Endpoint:** `/get-goal?username=Amna`

**Response:**
```json
{ "goal": "We are building AI Agents Workforce", "username": "Amna" }
```

---

### ✅ 3. Login with Query Parameters

Validates login based on `name` and `password` query parameters.

**Endpoint:** `/login?name=Amna&password=amna1234`

**Success Response:**
```json
{ "message": "Login Successful" }
```

**Failure Response:**
```json
{ "error": "Login failed" }
```

---

### ✅ 4. Path & Query Dependencies

Calculates a total using:
- Path Parameter: `num`
- Dependency 1: adds 1 to `num`
- Dependency 2: adds 2 to `bonus` query param

**Endpoint:** `/main/5?bonus=3`

**Response:**
```json
{
  "message": "Pakistan 16",
  "details": {
    "num": 5,
    "num1": 6,
    "num2": 5
  }
}
```

---

### ✅ 5. Class-Based Dependency (Generic Fetch by ID)

Reusable class to fetch **blogs** or **users** by ID with built-in 404 error handling.

**Available Blogs:**
- 1: Generative AI Blog
- 2: Machine Learning Blog
- 3: Deep Learning Blog
- 4: Natural Language Processing Blog
- 5: Computer Vision Blog
- 6: AI in Healthcare Blog

**Available Users:**
- 8: Amna
- 9: Areeba
- 10: Ahmed
- 11: Fatima
- 12: Zain
- 13: Sana

**Blog Endpoint Example:** `/blog/2`

**User Endpoint Example:** `/user/13`

---

## 🛠️ Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/ai-agents-api.git
cd ai-agents-api
```

### 2. Create a Virtual Environment (Optional)
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn
```

### 4. Run the API Server
```bash
uvicorn main:app --reload
```

### 5. Open in Browser
Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access Swagger UI and test all endpoints.

---

## 🤝 Contributing

Want to add more features? Feel free to fork this repo and submit a pull request.

---

## 🧠 Author

**Amna Rafeeq**  
---
