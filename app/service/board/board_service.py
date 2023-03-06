from typing import List

from fastapi import Depends, HTTPException

from app.domain.dto.response.board import BoardReadResponse
from app.mapper.repository.board.repository_board import BoardRepository
from app.domain.dto.request.board import BoardUpdateRequest, BoardCreateRequest


class BoardService:
    def __init__(self, board_repository: BoardRepository = Depends()):
        self.board_repository = board_repository

    def create_board_item(self, item: BoardCreateRequest):
        data = self.board_repository.create_boards_item(item)
        delattr(data, "password")

        return data

    def get_board(self, skip: int = 0, limit: int = 10) -> List[BoardReadResponse]:
        data = self.board_repository.get_boards(skip, limit)

        return [BoardReadResponse(id=item.id, title=item.title, body=item.body, name=item.name) for item in data]

    def search_board(self, q: str = "", skip: int = 0, limit: int = 10) -> List[BoardReadResponse]:
        if skip is None or limit is None:
            return [BoardReadResponse(id=item.id, title=item.title, body=item.body, name=item.name) for item in self.board_repository.search_boards_item(q)]
        elif skip is not None and limit is not None:
            return [BoardReadResponse(id=item.id, title=item.title, body=item.body, name=item.name) for item in self.board_repository.get_filtered_boards_with_pagination(q, skip, limit)]

    def delete_board(self, id: int) -> bool:
        return self.board_repository.delete_board_item(id)

    def get_boards_item_by_id(self, id: int):
        return self.board_repository.get_boards_item_by_id(id)

    def update_boards_item(self, id: int, item: BoardUpdateRequest):
        data = self.get_boards_item_by_id(item.id)

        if data is None:
            raise HTTPException(status_code=404)

        if data.password != item.password:
            raise HTTPException(status_code=401)

        data = self.board_repository.update_board_item(id, item)
        delattr(data, "password")
        return data
