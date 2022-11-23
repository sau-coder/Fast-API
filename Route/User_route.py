from Fastapi import APIrouter , status , HTTPException
from database import SessionLocal
from model.user import user_data ,user

router = APIrouter()
db = SessionLocal()

@router.get('/User')
def get_all_user():
    users = db.query(user_data).all()

    return {"data" : users , "message" : 'Users get successfully'}

@router.get('/User/{user_id}')
def get_user(user_id : int):
    user = db.query(user_data).filter(user_data.id == user_id)
    
    return {'data' : user , 'message' : 'User retrived successfully'}

@router.post('/User')
def create_user(user_data1 : user_data):
    db_user = db.query(user_data).filter(user_data.id == user_data1.id).first()

    if db_user is not None:
        raise HTTPException(status_code  = 400 , detail = 'User already exist')

    new_user =  user_data(
        id = user_data1.id,
        name = user_data1.name,
        password = user_data1.password,
        is_deleted = user_data1.is_deleted,
        email = user_data1.email,
        created_at = user_data1.created_at,
        updated_at = user_data1.updated_at
    )     

    db.add(new_user)
    db.commit()

    return {'status' : 200 , 'message' : 'User added successfully'}

@router.put('User/{user_id}' , status_code = status.HTTP_200_OK)
def update_user(user_id : int  , user1 : user_data):

    user_to_update = db.quary(user).filter(user.id ==user_id).first()
    user_to_update.id = user1.id
    user_to_update.name = user1.name
    user_to_update.password = user1.password
    user_to_update.is_deleted = user1.is_deleted
    user_to_update.email = user1.email
    user_to_update.created_by = user1.created_at
    user_to_update.update_by = user1.updated_at

    db.commit()

    return {'status' : 200 , 'message' : 'user updated successfully'}

@router.delete('/User/{user_id}')
def delete_user(user_id : int):
    user_to_delete = db.query(user).filter(user.id == user_id).first()
    if user_to_delete is None:
        raise HTTPException(
            stutus_code =  status.HTTP_404_NOT_FOUND,detail = 'User not found')
    
    db.delete(user_to_delete)
    db.commit()

    return {'data' : user_to_delete , 'status' : 200 , 'message'  : 'User delete successfully'}