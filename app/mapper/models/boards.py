from sqlalchemy import Column, Integer, String, Text

from app.mapper.db.database import Base


class Boards(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    body = Column(Text)
    name = Column(String)
    password = Column(String)

