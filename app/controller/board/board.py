from typing import Optional

from fastapi import APIRouter, Depends, Query, HTTPException

from app.mapper.db.database import get_db
from app.mapper.repository.board.repository_board import BoardRepository
from app.service.board.board_service import BoardService
from app.service.board.dto.request.board import BoardCreateRequest, BoardUpdateRequest

router = APIRouter(
    prefix="/board",
    tags=["board"],
    responses={404: {"description": "Not found"}}
)


@router.get("")
def get_board_item(q: Optional[str] = Query(None, min_length=3), skip: int = 0, limit: int = 10, db=Depends(get_db)):
    board_repository = BoardRepository(db)
    board_service = BoardService(board_repository)
    if q:
        return board_service.search_board(q)

    return board_service.get_board(skip=skip, limit=limit)


@router.post('')
def create_board_item(item: BoardCreateRequest, db=Depends(get_db)):
    board_repository = BoardRepository(db)
    board_service = BoardService(board_repository)

    return board_service.create_board_item(item)


@router.delete('')
def delete_board_item(id: int, db=Depends(get_db)):
    board_repository = BoardRepository(db)
    board_service = BoardService(board_repository)

    return board_service.delete_board(id)


@router.patch('')
def update_board_item(item: BoardUpdateRequest, db=Depends(get_db)):
    board_repository = BoardRepository(db)
    board_service = BoardService(board_repository)

    data = board_service.get_boards_item_by_id(item.id)

    if data is None:
        raise HTTPException(status_code=404)

    if data.password != item.password:
        raise HTTPException(status_code=401)

    return board_service.update_boards_item(item.id, item)

