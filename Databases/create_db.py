from app.databases.database import base , engine
from app.user.user_schema import User
from app.competition.competition_route import Competition
from app.entry.entry_schema import Entry

print('creating Database...')

base.metadata.create_all(engine)


