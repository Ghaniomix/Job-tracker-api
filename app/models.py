from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Application(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    company: str
    role: str
    status: str = "applied"
    notes: Optional[str] = None
    applied_date: date = Field(default_factory=date.today)
