from app.mapper.db.database import Base, engine
from .boards import Boards
from .comments import Comments

Base.metadata.create_all(bind=engine)
