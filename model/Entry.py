from pydantic import BaseModel
from databases.database import base
from sqlalchemy import String , Integer , Boolean , DateTime , Column , ForeignKey
from model.competition import competition

class entry_data(BaseModel):
    Entry_id : int
    Name : str
    Status : str
    Country : str
    Is_deleted : bool
    Created_at : str
    Updated_at : str
    Competition_id : int

    class config:
        orm_mode = True

class entry(base):
    __tablename__='entry'
    Entry_id = Column(Integer , primary_key = True)
    Name = Column(String)
    Status = Column(String)
    Country = Column(String)
    Is_deleted  = Column(Boolean)
    Created_at = Column(String)
    Updated_at = Column(String)
    Competition_id = Column(Integer , ForeignKey(competition.Competition_id))



