from pydantic import BaseModel, EmailStr

class loginModel(BaseModel):
    email : EmailStr
    password : str