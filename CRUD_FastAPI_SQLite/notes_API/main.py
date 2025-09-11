from fastapi import FastAPI
from notes_API.database import engine
from routers import notes
from notes_API.models import Base

Base.metadata.create_all(bind= engine)

app = FastAPI()

app.include_router(notes.notes_router)

@app.get("/api/healthchecker")
def healthcheck():
    return {"message": "A CRUD API with fastapi and sqlite", "data": {"path": "/api/healthchecker", "operation": "get", "path_operation_function": "healthcheck"}}