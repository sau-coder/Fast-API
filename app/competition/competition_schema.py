from sqlalchemy import String , Boolean , Integer , Column , DateTime , ForeignKey 
from user.user_schema import User
from databases.database import base

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


