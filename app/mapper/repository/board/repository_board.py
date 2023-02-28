from typing import Optional, List

from sqlalchemy.orm import Session

from app.mapper.models.boards import Boards
from app.mapper.repository_interface.board.irepository_board import IBoardRepository
from app.service.board.dto.request.board import Board_create_request


class BoardRepository(IBoardRepository):



    def __init__(self, db: Session):
        self.db = db

    def get_boards(self, skip: int = 0, limit: int = 10) -> Optional[List[Boards]]:
        return self.db.query(Boards).offset(skip).limit(limit).all()

    def create_boards_item(self, item: Board_create_request) -> bool:
        board = Boards(
            title=item.title,
            body=item.body,
            password=item.password,
            name=item.name
        )
        self.db.add(board)
        self.db.commit()
        self.db.refresh(board)
        return True

    def get_all_boards(self):
        return self.db.query(Boards).all()

    def search_boards_item(self, q: str) -> List[Boards]:
        return self.db.query(Boards).filter(Boards.title.ilike(f"%{q}%")).all()

    def get_filtered_boards_with_pagination(self, q: str, skip: int = 0, limit: int = 10) -> List[Boards]:
        return self.db.query(Boards).filterBoards.title.ilike(f"%{q}%").offset(skip).limit(limit).all()

    def delete_board_item(self, id: int) -> bool:
        self.db.query(Boards).filter(Boards.id == id).delete()
        self.db.commit()
        return True
