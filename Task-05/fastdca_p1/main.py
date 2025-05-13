from fastapi import FastAPI , Depends, Query, Path, HTTPException, status
from typing import Annotated

app = FastAPI()

#  1. Simple Dependency — Without any parameter
def get_simple_goal():
    return {"goal": "We are building AI Agents Workforce"}

@app.get("/get-simple-goal")
def simple_goal(response :  Annotated[dict, Depends(get_simple_goal)]):
    return response

#  2. Dependency with parameter (Injected automatically from query by FastAPI)
def get_goal(username: str):
    return {"goal": "We are building AI Agents Workforce", "username": username}

@app.get("/get-goal")
def get_my_goal(response :  Annotated[dict, Depends(get_goal)]):
    return response

#  3. Dependency using Query parameters (like login)
def dep_login(name: str = Query(None), password: str = Query(None)):
    if name == "Amna" and password == "amna1234":
        return {"message": "Login Successful"}
    else:
        return {"error": "Login failed"}

@app.get("/login")
def login(user: Annotated[dict, Depends(dep_login)]):
    return user    

#  4. Multiple Dependencies using Path and Query (with arithmetic logic)
def depfunc1(num: int = Path(...)): 
    return num + 1  # Add 1 to the path parameter

def depfunc2(bonus: int = Query(0)): 
    return bonus + 2  # Add 2 to the bonus query param

@app.get("/main/{num}")
def get_main(
    num: int,  # From path
    num1: Annotated[int, Depends(depfunc1)],  # Calculated using depfunc1
    num2: Annotated[int, Depends(depfunc2)]   # Calculated using depfunc2
):
    total = num + num1 + num2
    return {
        "message": f"Pakistan {total}",
        "details": {"num": num, "num1": num1, "num2": num2}
    }

#  5. Class-Based Dependency — Custom logic with validation

# Sample data store for blogs and users
data_store = {
   "blogs": {
        "1": "Generative AI Blog",
        "2": "Machine Learning Blog",
        "3": "Deep Learning Blog",
        "4": "Natural Language Processing Blog",
        "5": "Computer Vision Blog",
        "6": "AI in Healthcare Blog"
    },
    "users": {
        "8": "Amna",
        "9": "Areeba",
        "10": "Ahmed",
        "11": "Fatima",
        "12": "Zain",
        "13": "Sana"
    }
}

# Custom class to fetch item by ID or raise 404 if not found
class GetItemByID:
    def __init__(self, category: str):
        self.category = category  # category could be "blogs" or "users"

    def __call__(self, id: str):
        items = data_store.get(self.category, {})
        item = items.get(id)
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.category.title()} ID {id} not found"
            )
        return item

# Route to get blog by ID
@app.get("/blog/{id}")
def read_blog(blog: Annotated[str, Depends(GetItemByID("blogs"))]):
    return {"blog": blog}

# Route to get user by ID
@app.get("/user/{id}")
def read_user(user: Annotated[str, Depends(GetItemByID("users"))]):
    return {"user": user}
