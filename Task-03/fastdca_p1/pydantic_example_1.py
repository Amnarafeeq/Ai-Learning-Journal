from pydantic import BaseModel, ValidationError

class Student(BaseModel):
    name: str
    f_name: str
    age: int
    roll_number: int
    course: str
    email: str | None = None

student_data = {"name": "John", "f_name": "Alice", "age": 22, "roll_number": 1234, "course": "AI", "email": "johnalice@gail.com"} 
std = Student(**student_data)
print(std)
print(std.model_dump())

try:
    invalid_std = Student(name = "John", f_name="Alice", age=22, roll_number=1234, course="AI")
except ValidationError as e:
    print("error", e)    