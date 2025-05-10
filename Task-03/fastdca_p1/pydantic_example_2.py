from pydantic import BaseModel, ValidationError, EmailStr


class StdAddress(BaseModel):
    street : str
    city: str
    zip_code: int

class StdWithAddress(BaseModel):
    name : str
    f_name : str
    roll_number: int
    email: EmailStr
    address: list[StdAddress]

try:
    student_data = {
        "name" : "Amna",
        "f_name": "Rafeeq",
        "roll_number" : 12345,
        "email" : "amna@gmail.com",
        "address": [
            {"street": "streetNo33", "city": "Karachi", "zip_code": 157315},
            {"street": "streetNo34", "city": "Karachi", "zip_code": 872831}
        ]
    }
except ValidationError as e:
    print("Error", e)    

std = StdWithAddress.model_validate(student_data)
print(std.model_dump())
