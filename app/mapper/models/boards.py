from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.mapper.db.database import Base


class Boards(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    body = Column(Text)
    name = Column(String)
    password = Column(String)

    comments = relationship("Comments", back_populates="board")
