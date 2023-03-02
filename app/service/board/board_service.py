from app.mapper.models.boards import Boards
from app.mapper.repository.board.repository_board import BoardRepository
from app.dto.request.board import BoardUpdateRequest


class BoardService:
    def __init__(self, board_repository: BoardRepository):
        self.board_repository = board_repository

    def get_all_boards(self):
        return self.board_repository.get_all_boards()

    def create_board_item(self, item: Boards):
        try:
            self.board_repository.create_boards_item(item)
        except Exception as e:
            print(e)

    def get_board(self, skip: int = 0, limit: int = 10):
        try:
            return self.board_repository.get_boards(skip, limit)
        except Exception as e:
            print(e)

    def search_board(self, q: str = "", skip: int = 0, limit: int = 10):
        try:
            if skip is None or limit is None:
                return self.board_repository.search_boards_item(q)
            elif skip is not None and limit is not None:
                return self.board_repository.get_filtered_boards_with_pagination(q, skip, limit)

        except Exception as e:
            print(e)

    def delete_board(self, id: int) -> bool:
        try:
            return self.board_repository.delete_board_item(id)

        except Exception as e:
            print(e)

    def get_boards_item_by_id(self, id: int):
        try:
            return self.board_repository.get_boards_item_by_id(id)

        except Exception as e:
            print(e)

    def update_boards_item(self, id: int, item: BoardUpdateRequest):
        try:
            return self.board_repository.update_board_item(id, item)

        except Exception as e:
            print(e)