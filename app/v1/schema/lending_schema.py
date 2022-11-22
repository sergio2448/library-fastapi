# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field

class LendingBase(BaseModel):
    start_at: datetime = Field(...)
    end_at:datetime = Field(...)
    created_at = Field(default=datetime.now())

class Lending(LendingBase):
    id: int = Field(...)