from fastapi import FastAPI, Path, Query, Body, Header, Cookie , Response, Form , UploadFile , File
from pydantic import BaseModel
app = FastAPI()

# Path Parameters

@app.get("/user/{user_id}")
async def read_item(
    user_id: int = Path(
        ...,
        title= "This is the id of user. ",
        description= "Unique Identifier",
        ge=1
    )
):
    try:
        return {
            "data": {
                "id" : user_id,
                "name" : "Amna",
                "email" : "amna@gmail.com",
                "ph_num" : 1234567890
            },
            "status": "Ok"

        }
    except Exception as e:
        return {
            "status" : "error",
            "message": e,
            "data" : None
        }


# Query Parameters

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/student")
def root_def(
    id: int = Query(..., ge=1, description="Student ID must be greater than 0"),
    name: str = Query(..., min_length=2, max_length=30, description="Student name")
):
    try:
        return {
            "status": "Ok",
            "data": {
                "id": id,
                "name": name,
                "email": f"{name.lower().replace(' ', '')}@gmail.com"
            }
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }

# Body Parameter

class User(BaseModel):
    name: str
    email: str
    id: int

@app.post("/new_user")
def create_user(user: User = Body(...)):
    try:
        return {
            "status": "Ok",
            "data": {
                "user": user
            }
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }
    
# path, query and body parameters
class Student(BaseModel):
    name: str
    email: str
    course: str

@app.post("/register_student/{age}")
def register_student(
    age: int = Path(..., ge=1, le=120, description="Student's age must be between 1 and 120"),
    referral_code: str | None = Query(None, min_length=3, max_length=20, description="Optional referral code"),
    student: Student = Body(...)
):
    try:
        return {
            "status": "success",
            "message": "Student registered successfully",
            "data": {
                "name": student.name,
                "email": f"{student.name.lower().replace(' ', '')}@gmail.com",
                "course": student.course,
                "age": age,
                "referral_code": referral_code
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "data": None
        }

@app.get("/get-user")
def get_user(user_agent: str = Header(...)):
    return {"User-Agent": user_agent}        

# cookie

@app.get("/set-cookie")
def set_cookie(response: Response):
    response.set_cookie(key="token", value="amna_secure_token")
    return {"message": "Cookie has been set!"}

# Route to read the cookie

@app.get("/get-cookie")
def get_cookie(token: str = Cookie(default=None)):
    return {"Your Token": token}

# Form Data

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if len(username) < 4:
        return {"status": "error", "message": "Username must be at least 4 characters."}
    
    if len(password) < 4:
        return {"status": "error", "message": "Password must be at least 4 characters."}
    
    return {"status": "success", "username": username, "message": "Login successful"}


# Upload file

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    
    return {
        "filename": file.filename,
        "file_size": len(content),
        "file_type": file.content_type
    }