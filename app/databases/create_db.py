from databases.database import base , engine
from user.user_schema import User
from competition.competition_schema import Competition
from entry.entry_schema import Entry

print('creating Database...')

base.metadata.create_all(engine)
