from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Literal

from .db import create_db_and_tables
from . import models
from sqlmodel import select
from .db import get_session
from .models import Application
from sqlmodel import select



app = FastAPI(title="Job Tracker API")

Status = Literal["applied", "interview", "offer", "rejected"]

class ApplicationIn(BaseModel):
    company: str
    role: str
    status: Status = "applied"
    notes: Optional[str] = None

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/")
def home():
    return {"message": "Welcome to Job Tracker API. Go to /docs"}

@app.post("/applications")
def create_application(payload: ApplicationIn):
    with get_session() as session:
        app_obj = Application(
            company=payload.company,
            role=payload.role,
            status=payload.status,
            notes=payload.notes,
        )
        session.add(app_obj)
        session.commit()
        session.refresh(app_obj)
        return app_obj
    
@app.get("/applications")
def list_applications():
    with get_session() as session:
        applications = session.exec(select(Application)).all()
        return applications

@app.get("/applications/{app_id}")
def get_application(app_id: int):
    with get_session() as session:
        app_obj = session.get(Application, app_id)
        if not app_obj:
            raise HTTPException(status_code=404, detail="Application not found")
        return app_obj
    
@app.put("/applications/{app_id}")
def update_application(app_id: int, payload: ApplicationIn):
    with get_session() as session:
        app_obj = session.get(Application, app_id)
        if not app_obj:
            raise HTTPException(status_code=404, detail="Application not found")

        app_obj.company = payload.company
        app_obj.role = payload.role
        app_obj.status = payload.status
        app_obj.notes = payload.notes

        session.add(app_obj)
        session.commit()
        session.refresh(app_obj)
        return app_obj

@app.delete("/applications/{app_id}")
def delete_application(app_id: int):
    with get_session() as session:
        app_obj = session.get(Application, app_id)
        if not app_obj:
            raise HTTPException(status_code=404, detail="Application not found")

        session.delete(app_obj)
        session.commit()
        return {"message": "Application deleted"}
