from pydantic import BaseModel

class Note(BaseModel):
    title: str
    body: str

class NoteCreate(Note):
    pass

class NoteOut(Note):
    id: int