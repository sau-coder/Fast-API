from fastapi import APIRouter , status ,HTTPException
from database import SessionLocal
from model.competition import competition , Competition_data

router = APIRouter()
db = SessionLocal()

@router.get('/competition',status_code = 200)
def get_all_competition():
    competitions = db.query(competition).all()

    return {'data' : competitions , status : 200 , 'message' : 'competition get successfully'}

@router.get('/compitition/{competition_id}')
def get_competition(competition_id : int):
    Competition = db.query(competition.id == competition_id).first()

    return {'data' : Competition , 'status' : 200 , 'message' : 'competition retrived successfully'}

@router.post('/competition' , status_code = status.HTTP_201_CREATED)
def create_competition(competition = )