from fastapi import APIRouter , status ,HTTPException
from databases.database import SessionLocal
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
def create_competition(competition1 = Competition_data):
    db_competition = db.query(competition).filter(Competition_data.id == competition.id).first()

    if db_competition is not None:
        raise HTTPException(status_code=400 , detail = 'Compatition already exist')

    new_compatition = competition(
        Competition_id = competition1.Competition_id,
        Name = competition1.Name,
        Status = competition1.Status,
        Url = competition1.Url,
        Is_deleted = competition1.Is_deleted,
        Created_at = competition1.Created_at,
        Updated_at = competition1.Updated_at,
        id = competition1.id  
    )

    db.add(new_compatition)
    db.commit()
    
    return{'status' : 200 , 'message' : 'competition added successfully'}


@router.put('/competition/{competition_id}' , status_code = status.HTTP_200_OK)
def update_a_competition(competition_id : int , competition1 : Competition_data):

    competition_to_update = db.query(competition).filter(competition.id == competition_id)
    competition_to_update.Competition_id = competition1.Competition_id,
    competition_to_update.Name = competition1.Name,
    competition_to_update.Status = competition1.Status,
    competition_to_update.Url = competition1.Url,
    competition_to_update.Is_deleted = competition1.Is_deleted,
    competition_to_update.Created_at = competition1.Created_at,
    competition_to_update.Updated_at = competition1.Updated_at,
    competition_to_update.id = competition1.id

    db.commit()

    return{'status' : 200 , 'message' : 'competition updated successfully'}


@router.delete('/competiton/{competition_id}')
def delete_competition(competition_id : int):
    competition_to_delete = db.query(competition).filter(competition.id == competition_id).first()

    if competition_to_delete is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND , detail = 'Competition not found'
        )

    db.delete(competition_to_delete)
    db.commit()

    return {"data": competition_to_delete, "status": 200, "message": "Competition deleted successfully"}  

