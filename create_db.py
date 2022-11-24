from databases.database import base , engine
from model.users import user
from model.competition import competition
from model.Entry import entry

print('creating Database...')

base.metadata.create_all(engine)
