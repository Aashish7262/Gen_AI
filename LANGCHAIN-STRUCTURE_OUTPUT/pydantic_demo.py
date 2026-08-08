from pydantic_with_output import BaseModel , EmailStr , Field
from typing import Optional 
class student(BaseModel):
    name : str = 'nitish'
    age : Optional[int] # default value 
    email: EmailStr = Field(description='This is the email')
    cgpa : float = Field(gt = 0, lt = 10,descriptiom = 'A decimal value representing the cgpa of the student')
new_student = {'age':'32','email':'abc@gmail.com','cgpa' : '5.0'}
student = student(**new_student)
student_json = student.model_dump_json()
print(student_json)
