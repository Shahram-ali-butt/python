from fastapi import FastAPI, APIRouter, status, HTTPException
from schemas import NoteCreate, NoteOut
from typing import List

note_list: List[NoteOut] = []

app = FastAPI()
notes_router = APIRouter()

@notes_router.get("/", response_model=List[NoteOut])
def notes_all(): 
    return note_list

@notes_router.get("/{note_id}", response_model=NoteOut)
def get_note(note_id: int):
    for note in note_list:
        if note.id == note_id:
            return note
    raise HTTPException(status_code=404, detail=f"Note with id: {note_id} not found") 

@notes_router.post("/", status_code=status.HTTP_201_CREATED, response_model=NoteOut)
def create_note(note: NoteCreate):
    new_note = NoteOut(id = len(note_list) + 1, **note.model_dump())
    note_list.append(new_note)
    return new_note
    
@notes_router.put("/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note_body: str):
    for note in note_list:
        if note.id == note_id:
            note.body = note_body
            return note
    raise HTTPException(status_code=404, detail=f"Note with id: {note_id} not found")
        
@notes_router.delete("/{note_id}")
def delete_note(note_id: int):
    for n in note_list:
        if n.id == note_id:
           note_list.remove(n)
           return  
    raise HTTPException(status_code=404, detail=f"Note with id: {note_id} not found")

app.include_router(notes_router, prefix = "/api/notes", tags=['Notes'])

@app.get("/api/healthchecker")
def healthcheck():
    return {"status": "running", "data": {"path": "/api_healthcheck", "operation": "get", "path_operation_function": "healthcheck"}}
