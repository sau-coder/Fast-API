from pydantic import BaseModel
from database import base
from sqlalchemy import string , Boolean , Integer , Column , DateTime , ForeignKey 
from sqlalchemy import MetaData
from model.user import user
metadata_obj = MetaData()

class Competition_data(BaseModel):
    Compitition_id : int
    Name : str
    Status : str
    Url : str
    Is_deleted : bool
    Created_at : DateTime
    Updated_at : DateTime
    id : int
    
    class config:
        orm_mode = True


class competition(base):
    __tablename__ = 'Competition'
    Compitition_id = Column(int , primary_key = True)
    Name = Column(str)
    Status = Column(str)
    Url = Column(str)
    Is_deleted = Column(bool)
    Created_at = Column(DateTime)
    Updated_at = Column(DateTime)
    id = Column(int , ForeignKey(user.id))


