from sqlalchemy.orm import Session

from app.mapper.models import boards
from app.mapper.repository_interface.board.irepository_board import IBoardRepository


class BoardRepository(IBoardRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all_boards(self):
        return self.db.query(boards).all()
