from fastapi import APIRouter , status ,HTTPException
from databases.database import SessionLocal
from competition.competition_schema import Competition
from competition.competition_model import CompetitionData

router = APIRouter()
db = SessionLocal()

@router.get('/competition',status_code=status.HTTP_201_CREATED)
def get_all_competition():
    competitions = db.query(Competition).all()

    return {'data' : competitions , 'status' : 200 , 'message' : 'competition get successfully'}


@router.get('/competition/{competition_id}')
def get_competition(competition_id : int):
    competition = db.query(Competition).filter(Competition.competition_id == competition_id).first()

    return {'data' : competition , 'status' : 200 , 'message' : 'competition retrived successfully'}


@router.post('/competition' , status_code = status.HTTP_201_CREATED)
def create_competition(competition1 : CompetitionData):
    db_competition = db.query(Competition).filter(Competition.competition_id == competition1.competition_id).first()

    if db_competition is not None:
        raise HTTPException(status_code=400 , detail = 'Compatition already exist')

    new_compatition = Competition(
        competition_id = competition1.competition_id,
        name = competition1.name,
        status = competition1.status,
        url = competition1.url,
        is_deleted = competition1.is_deleted,
        created_at = competition1.created_at,
        updated_at = competition1.updated_at,
        id = competition1.id  
    )

    db.add(new_compatition)
    db.commit()
    
    return{'status' : 200 , 'message' : 'competition added successfully'}


@router.put('/competition/{competition_id}' , status_code = status.HTTP_200_OK)
def update_a_competition(competition_id : int , competition1 : CompetitionData):

    competition_to_update = db.query(Competition).filter(Competition.id == competition_id)
    competition_to_update.competition_id = competition1.competition_id,
    competition_to_update.name = competition1.name,
    competition_to_update.status = competition1.status,
    competition_to_update.url = competition1.url,
    competition_to_update.is_deleted = competition1.is_deleted,
    competition_to_update.created_at = competition1.created_at,
    competition_to_update.updated_at = competition1.updated_at,
    competition_to_update.id = competition1.id

    db.commit()

    return{'status' : 200 , 'message' : 'competition updated successfully'}


@router.delete('/competition/{competition_id}')
def delete_competition(competition_id : int):
    competition_to_delete = db.query(Competition).filter(Competition.competition_id == competition_id).first()

    if competition_to_delete is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND , detail = 'Competition not found'
        )

    db.delete(competition_to_delete)
    db.commit()

    return {"data": competition_to_delete, "status": 200, "message": "Competition deleted successfully"}  

