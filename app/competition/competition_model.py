from pydantic import BaseModel

class CompetitionData(BaseModel):
    competition_id : int
    name : str
    status : str
    url : str
    is_deleted : bool
    created_at : str
    updated_at : str
    id : int
    
    class config:
        orm_mode = True