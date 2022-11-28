from pydantic import BaseModel
from typing import Union, Optional

class EntryData(BaseModel):
    entry_id : Optional[int]
    name : Optional[str]
    status : Optional[str]
    country : Optional[str] 
    is_deleted : Optional[bool]
    created_at : Optional[str] 
    updated_at : Optional[str]
    competition_id : Optional[int] 

    class config:
        orm_mode = True