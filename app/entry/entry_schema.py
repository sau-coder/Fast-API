from databases.database import base
from sqlalchemy import String , Integer , Boolean , DateTime , Column , ForeignKey
from competition.competition_schema import Competition

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



