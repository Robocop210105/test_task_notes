from pydantic import BaseModel, Field
from datetime import datetime

class NoteSchemaRead(BaseModel):
    text: str = Field(min_length=1)
    time_create: datetime
    time_change: datetime


class NoteSchemaWrite(BaseModel):
    text: str = Field(min_length=1)
    board_id: int
