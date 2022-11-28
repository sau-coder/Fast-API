from databases.database import base
from sqlalchemy import String , Boolean , Integer , Column , DateTime

class User(base):
    __tablename__ = 'User'
    id = Column(Integer , primary_key = True)
    name = Column(String)
    password = Column(String)
    is_deleted = Column(Boolean)
    email = Column(String)
    created_at  = Column(String)
    Updated_at = Column(String)

