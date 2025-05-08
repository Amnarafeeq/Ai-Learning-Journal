from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Greet": "Hello From Amna"}

@app.get("/greet/{name}")
def greet_name(name: str):
    return {"message": f"Hello, {name}!"}
