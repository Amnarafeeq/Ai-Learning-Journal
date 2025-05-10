from pydantic import BaseModel, EmailStr, validator, ValidationError



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

    @validator("name")
    def name_must_be_at_least_two_chars(cls, v):
        if len(v) < 4:
            raise ValueError("Name must be at least 4 characters long")
        return v  


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
try:
    std = StdWithAddress.model_validate(student_data)
    print(std.model_dump())

except ValidationError as e:
    print("Error", e)    


