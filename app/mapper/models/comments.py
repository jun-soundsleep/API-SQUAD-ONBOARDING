from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.mapper.db.database import Base


class Comments(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text)

    board_id = Column(Integer, ForeignKey("boards.id"))
    board = relationship("Boards", back_populates="comments")