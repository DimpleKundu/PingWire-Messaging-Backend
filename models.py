from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    username: str
    password: str

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Message(BaseModel):
    sender: str
    receiver: str
    content: str
    timestamp: Optional[datetime] = None
