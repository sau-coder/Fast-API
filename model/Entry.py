from pydantic import BaseModel
from database import base
from sqlalchemy import String , Integer , Boolean , DateTime , Column , ForeignKey
from model.competition import competition

class entry_data(BaseModel):
    Entry_id : int
    Name : str
    Status : str
    Country : str
    Is_deleted : bool
    Created_at : DateTime
    Updated_at : DateTime
    Comp_id : int

    class config:
        orm_mode = True

class entry(base):
    __
    Entry_id = Column(int , primary_key = True)
    Name = Column(str)
    Status = Column(str)
    Country = Column(str)
    Is_deleted  = Column(bool)
    Created_at = Column(DateTime)
    Updated_at = Column(DateTime)
    Comp_id = Column(int , ForeignKey(competition.Comp_id))


