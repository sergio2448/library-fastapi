from datetime import datetime

from pydantic import BaseModel
from pydantic import Field

class LendingBase(BaseModel):
    start_at: datetime = Field(...)
    end_at: datetime = Field(...)
    user_id: int = Field(...)
    book_id: int = Field(...)
    created_at = Field(default=datetime.now())

class Lending(LendingBase):
    id: int = Field(...)