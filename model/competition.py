from pydantic import BaseModel
from sqlalchemy import String , Boolean , Integer , Column , DateTime , ForeignKey 
from model.users import user
from databases.database import base

class Competition_data(BaseModel):
    Competition_id : int
    Name : str
    Status : str
    Url : str
    Is_deleted : bool
    Created_at : str
    Updated_at : str
    id : int
    
    class config:
        orm_mode = True


class competition(base):
    __tablename__ = 'Competition'
    Competition_id = Column(Integer , primary_key = True)
    Name = Column(String)
    Status = Column(String)
    Url = Column(String)
    Is_deleted = Column(Boolean)
    Created_at = Column(String)
    Updated_at = Column(String)
    id = Column(Integer , ForeignKey(user.id))


