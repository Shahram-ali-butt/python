from fastapi import HTTPException, Depends, status, APIRouter
from typing import List
from sqlalchemy.orm import Session
from notes_API import models, schemas
from notes_API.database import get_db

notes_router = APIRouter(prefix="/api/notes", tags=["Notes"])

@notes_router.get("/", response_model=List[schemas.NoteOut])
def get_notes(db: Session = Depends(get_db)):
    return db.query(models.Note).all()

@notes_router.get("/{note_id}", response_model=schemas.NoteOut)
def get_note(note_id: int, db: Session= Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@notes_router.post("/", response_model=schemas.NoteOut)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    new_note = models.Note(title=note.title, content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)  # refresh gets the new ID from DB
    return new_note

@notes_router.put("/{note_id}", response_model=schemas.NoteOut)
def update_note(note_id: int, updated_note: schemas.NoteCreate, db: Session= Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note.title = updated_note.title
    note.content = updated_note.content
    db.commit()
    db.refresh(note)
    return note

@notes_router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return None

