from pydantic import BaseModel, Field
from datetime import datetime


class MessageBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, example="john_doe")
    message: str = Field(..., min_length=1, max_length=500, example="Hello, world!")


class MessageCreate(MessageBase):
    pass


class MessageResponse(MessageBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
