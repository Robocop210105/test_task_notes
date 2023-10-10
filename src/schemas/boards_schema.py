from typing import List
from pydantic import BaseModel

from datetime import datetime

from schemas import NoteSchemaRead


class BoardSchemaWrite(BaseModel):
    name: str


class BoardSchemaRead(BaseModel):
    name: str
    time_create: datetime
    time_change: datetime
    notes: List[NoteSchemaRead] | None
