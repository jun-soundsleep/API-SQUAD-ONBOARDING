from typing import Optional, List

from fastapi import APIRouter, Depends, Query, HTTPException, status

from app.domain.dto.response.board import BoardCreateResponse, BoardUpdateResponse, BoardReadResponse
from app.service.board.board_service import BoardService
from app.domain.dto.request.board import BoardCreateRequest, BoardUpdateRequest

router = APIRouter(
    prefix="/board",
    tags=["board"],
    responses={404: {"description": "Not found"}}
)


@router.get("", response_model=List[BoardReadResponse])
def get_board_item(q: Optional[str] = Query(None, min_length=3), skip: int = 0, limit: int = 10,
                   board_service: BoardService = Depends()):
    if q:
        return board_service.search_board(q)

    return board_service.get_board(skip=skip, limit=limit)


@router.post('', response_model=BoardCreateResponse,  status_code=status.HTTP_201_CREATED)
def create_board_item(item: BoardCreateRequest, board_service: BoardService = Depends()):
    return board_service.create_board_item(item)


@router.delete('')
def delete_board_item(id: int, board_service: BoardService = Depends()):
    return board_service.delete_board(id)


@router.patch('', response_model=BoardUpdateResponse)
def update_board_item(item: BoardUpdateRequest, board_service: BoardService = Depends()):
    data = board_service.get_boards_item_by_id(item.id)

    if data is None:
        raise HTTPException(status_code=404)

    if data.password != item.password:
        raise HTTPException(status_code=401)

    return board_service.update_boards_item(item.id, item)
