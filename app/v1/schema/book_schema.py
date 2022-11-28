# Python
from datetime import datetime
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field

class BookState(Enum):
    Available = "Available"
    Borrowed = "Borrowed"
    Unavailable = "Unavailable"
    Reserved = "Reserved"

class BookBase(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=60
    )
    author: str = Field(
        ...,
        min_length=3,
        max_length=60
    )
    category: str = Field(
        ...,
        min_length=1,
        max_length=60
    )
    language: str = Field(
        ...,
        min_length=1,
        max_length=60
    )
    state: BookState = Field(
        ...
    )
    location: str = Field(
        ...,
        min_length=3,
        max_length=60
    )
    days_limit: int = Field(...)
    pages_number: int = Field(...)
    edition: int = Field(...) 
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())


class Book(BookBase):
    id: int = Field(...)