from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.mapper.db.database import get_db
from app.mapper.models.user import User
from app.mapper.repository.board.repository_board import BoardRepository
from app.service.board.board_service import BoardService

router = APIRouter(
    prefix="/board",
    tags=["board"],
    responses={404: {"description": "Not found"}}
)

board_service = BoardService(board_repository=BoardRepository(get_db()))


@router.get('')
def read_boards_all_item():
    return board_service.get_all_boards()
