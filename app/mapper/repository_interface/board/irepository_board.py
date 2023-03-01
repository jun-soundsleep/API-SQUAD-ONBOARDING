from abc import ABC, abstractmethod
from typing import List, Optional

from app.mapper.models.boards import Boards
from app.service.board.dto.request.board import BoardCreateRequest, BoardUpdateRequest


class IBoardRepository(ABC):
    @abstractmethod
    def get_all_boards(self) -> List[Boards]:
        pass

    @abstractmethod
    def get_boards(self, skip: int = 0, limit: int = 10) -> List[Boards]:
        pass

    @abstractmethod
    def create_boards_item(self, item: BoardCreateRequest) -> bool:
        pass

    @abstractmethod
    def search_boards_item(self, q: str) -> List[Boards]:
        pass

    @abstractmethod
    def get_filtered_boards_with_pagination(self, q: str, skip: int = 0, limit: int = 10) -> List[Boards]:
        pass

    @abstractmethod
    def delete_board_item(self, id: int) -> bool:
        pass

    @abstractmethod
    def update_board_item(self, id: int, item: BoardUpdateRequest) -> bool:
        pass

    @abstractmethod
    def get_boards_item_by_id(self, id: int) -> Boards:
        pass
