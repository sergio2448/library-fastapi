from datetime import datetime

from pydantic import BaseModel
from pydantic import Field

class PenaltyBase(BaseModel):
    days_late: int = Field(...)
    total_taxes: int = Field(...)
    state: str = Field(...)
    lending_id: int = Field(...)
    created_at = Field(default=datetime.now())

class Penalty(PenaltyBase):
    id: int = Field(...)