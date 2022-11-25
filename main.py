from fastapi import FastAPI
from Route.User_route import router as user_router
from Route.competition_route import router as competition_router
from Route.Entry_route import router as entry_router

app = FastAPI()

@app.get('/')
def User_record ():
    return {'Get started with' : 'postgres with fastapi'}

app.include_router(user_router , tags=['User'] , prefix='/user/v1')
app.include_router(competition_router , tags=['Competition'] , prefix='/competition/v1')
app.include_router(entry_router , tags=['Entry'] , prefix='/entry/v1')
