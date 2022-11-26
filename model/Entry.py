from pydantic import BaseModel
from typing import Union, Optional
from databases.database import base
from sqlalchemy import String , Integer , Boolean , DateTime , Column , ForeignKey
from model.competition import Competition

class EntryData(BaseModel):
    entry_id : Optional[int] = None
    name : Optional[str] = None
    status : Optional[str] = None
    country : Optional[str] = None
    is_deleted : Optional[bool]
    created_at : Optional[str] = None
    updated_at : Optional[str] =None
    competition_id : Optional[int] = None

    class config:
        orm_mode = True

class Entry(base):
    __tablename__='entry'
    entry_id = Column(Integer , primary_key = True)
    name = Column(String)
    status = Column(String)
    country = Column(String)
    is_deleted  = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    competition_id = Column(Integer , ForeignKey(Competition.competition_id))



