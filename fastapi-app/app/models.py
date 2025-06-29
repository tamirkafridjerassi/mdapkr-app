from pydantic import BaseModel, EmailStr
from typing import List

class Certifications(BaseModel):
    EMT: bool
    Driver: bool
    PRA: bool

class Person(BaseModel):
    name: str
    email: EmailStr
    certifications: Certifications

class Mission(BaseModel):
    type: str  # "ALS" or "BLS"
    dates: List[str]