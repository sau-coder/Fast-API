from pydantic import BaseModel
from databases.database import base
from sqlalchemy import String , Boolean , Integer , Column , DateTime

class user_data(BaseModel):
    id : int
    name : str
    password : str
    is_deleted : bool
    email : str
    created_at : str
    updated_at : str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
    

class user(base):
    __tablename__ = 'User'
    id = Column(Integer , primary_key = True)
    name = Column(String)
    password = Column(String)
    is_deleted = Column(Boolean)
    email = Column(String)
    created_at  = Column(String)
    Updated_at = Column(String)

