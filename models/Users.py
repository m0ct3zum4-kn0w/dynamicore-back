from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class newUser(BaseModel):
    email : EmailStr
    password : str

class UserBase(BaseModel):
    uid : Optional[str] = None
    email : EmailStr
    password : str
    created_at : Optional[datetime]
    updated_at : Optional[datetime]
    class Config:
        orm_mode = True
