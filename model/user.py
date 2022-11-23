from pydantic import BaseModel
from database import base
from sqlalchemy import string , Boolean , Integer , Column , DateTime

class user_data(BaseModel):
    id : int
    name : str
    password : str
    is_deleted : bool
    email : str
    created_at : DateTime
    updated_at : DateTime

    class Config:
        orm_mode = True

class user(base):
    __tablename__ = 'User'
    id = Column(Integer , primary_key = True)
    name = Column(str)
    password = Column(str)
    is_deleted = Column(bool)
    email = Column(str)
    created_at  = Column(DateTime)
    Updated_at = Column(DateTime)

