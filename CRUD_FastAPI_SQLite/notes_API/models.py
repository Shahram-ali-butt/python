from .database import Base
from sqlalchemy import Column, String, Integer
from .database import Base

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)



