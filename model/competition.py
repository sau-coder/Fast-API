from pydantic import BaseModel
from sqlalchemy import String , Boolean , Integer , Column , DateTime , ForeignKey 
from model.users import User
from databases.database import base

class CompetitionData(BaseModel):
    competition_id : int
    name : str
    status : str
    url : str
    is_deleted : bool
    created_at : str
    updated_at : str
    id : int
    
    class config:
        orm_mode = True


class Competition(base):
    __tablename__ = 'Competition'
    competition_id = Column(Integer , primary_key = True)
    name = Column(String)
    status = Column(String)
    url = Column(String)
    is_deleted = Column(Boolean)
    created_at = Column(String)
    updated_at = Column(String)
    id = Column(Integer , ForeignKey(User.id))


