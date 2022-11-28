from pydantic import BaseModel

class UserData(BaseModel):
    id : int
    name : str
    password : str
    is_deleted : bool
    email : str
    created_at : str
    updated_at : str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
    