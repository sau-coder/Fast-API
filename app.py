from fastapi import FastAPI
from user.user_route import router as user_router
from competition.competition_route import router as competition_router
from entry.entry_route import router as entry_router

app = FastAPI()

@app.get('/')
def User_record ():
    return {'Get started with' : 'postgres with fastapi'}

app.include_router(user_router , tags=['User'] , prefix='/user/v1')
app.include_router(competition_router , tags=['Competition'] , prefix='/competition/v1')
app.include_router(entry_router , tags=['Entry'] , prefix='/entry/v1')
