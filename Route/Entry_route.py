from fastapi import APIRouter ,status , HTTPException
from model.Entry import entry , entry_data
from databases.database import SessionLocal

router = APIRouter()
db = SessionLocal()

@router.get('/entry', status_code=200)
def get_all_entry():
    Entries = db.query(entry).all()

    return {'data' : Entries , 'status' : 200 , 'message' : 'Entries fetched successfully'}


@router.get('/entry/{entry_id}')
def get_an_entry(entry_id : int):
    Entry_1 = db.query(entry).filter(entry.Entry_id == entry_id).first()

    return {'data' : Entry_1 , 'status' : 200 , 'message' : 'Entry retrived successfully'}


@router.post('/entry' , status_code = status.HTTP_201_CREATED)
def create_entry(Entry_data : entry_data):

    db_entry = db.query(entry).filter(entry.Entry_id == Entry_data.Entry_id).first()

    if db_entry is not  None:
        raise HTTPException (status_code=400 , detail='Entry already exist')

    new_entry = entry(
        Entry_id = Entry_data.Entry_id,
        Name = Entry_data.Name,
        Status = Entry_data.Status,
        Country = Entry_data.Country,
        Is_deleted = Entry_data.Is_deleted,
        Created_at = Entry_data.Created_at,
        Updated_at = Entry_data.Updated_at,
        Competition_id = Entry_data.Competition_id 
    )

    db.add(new_entry)
    db.commit()

    return {'status' : 200 , 'message' : 'Entry added successfully'}


@router.put('/entry/{entry_id}' , status_code=status.HTTP_200_OK)
def update_an_entry(entry_id : int , Entry : entry_data):
    Entry_update = db.query(entry).filter(entry.Entry_id == entry_id).first()
    breakpoint()
    Entry_update.Entry_id = Entry.Entry_id,
    Entry_update.Name = Entry.Name,
    Entry_update.Status = Entry.Status,
    Entry_update.Country = Entry.Country,
    Entry_update.Is_deleted = Entry.Is_deleted,
    Entry_update.Created_at = Entry.Created_at,
    Entry_update.Updated_at = Entry.Updated_at,
    Entry_update.Competition_id = Entry.Competition_id

    db.commit()

    return {'status' : 200 , 'message' : 'Entry updated successfully.'}


@router.delete('/entry/{entry_id}')
def delete_an_entry(Entry_id : int):
    
    delete_entry = db.quary(entry).filter(entry.id == Entry_id)

    if delete_entry is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND , detail = 'Entry not found'
        )

    db.delete(delete_entry)
    db.commit()

    return {'data' : delete_entry , 'status' : 200 , 'message' : 'Entry delete successfully'}








