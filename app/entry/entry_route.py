from fastapi import APIRouter ,status , HTTPException
from entry.entry_schema import Entry
from entry.entry_model import EntryData
from databases.database import SessionLocal
from datetime import datetime
from sqlalchemy import update

router = APIRouter()
db = SessionLocal()

@router.get('/entry', status_code=200)
def get_all_entry():
    Entries = db.query(Entry).all()

    return {'data' : Entries , 'status' : 200 , 'message' : 'Entries fetched successfully'}


@router.get('/entry/{entry_id}')
def get_an_entry(entry_id : int):
    entry_1 = db.query(Entry).filter(Entry.entry_id == entry_id).first()

    return {'data' : entry_1 , 'status' : 200 , 'message' : 'Entry retrived successfully'}


@router.post('/entry' , status_code = status.HTTP_201_CREATED)
def create_entry(entry_data : EntryData):

    db_entry = db.query(Entry).filter(Entry.entry_id == EntryData.entry_id).first()

    if db_entry is not  None:
        raise HTTPException (status_code=400 , detail='Entry already exist')

    new_entry = Entry(
        entry_id = entry_data.Entry_id,
        name = entry_data.Name,
        status = entry_data.Status,
        country = entry_data.Country,
        is_deleted = entry_data.Is_deleted,
        created_at = datetime.utcnow(),
        updated_at = datetime.utcnow(),
        competition_id = entry_data.Competition_id 
    )
    db.add(new_entry)
    db.commit()

    return {'status' : 200 , 'message' : 'Entry added successfully'}



@router.put('/entry/{entry_id}' , status_code=status.HTTP_200_OK)
def update_an_entry(entry_id : int , entry : EntryData):

    entry_update = db.query(Entry).filter(Entry.entry_id == entry_id).first()
    if entry_update.entry_id != None:
        entry_update.entry_id = entry.Entry_id

    if entry_update.name != None:
        entry_update.name = entry.name

    if entry_update.status != None:    
        entry_update.status = entry.status

    if entry_update.country != None:    
        entry_update.country = entry.country

    if entry_update.is_deleted != None:
        entry_update.is_deleted = entry.is_deleted

    if entry_update.created_at != None:
        entry_update.created_at = entry.created_at

    if entry_update.competition_id != None:
        entry_update.competition = entry.competition_id
    



    db.commit()

    return {'status' : 200 , 'message' : 'Entry updated successfully.'}


@router.delete('/entry/{entry_id}')
def delete_an_entry(entry_id : int):
    
    delete_entry = db.query(Entry).filter(Entry.Entry_id == entry_id).first()

    if delete_entry is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND , detail = 'Entry not found'
        )

    db.delete(delete_entry)
    db.commit()

    return {'data' : delete_entry , 'status' : 200 , 'message' : 'Entry delete successfully'}








