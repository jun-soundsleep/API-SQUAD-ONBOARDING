from app.mapper.repository.board.repository_board import BoardRepository


class BoardService:
    def __init__(self, board_repository: BoardRepository):
        self.board_repository = board_repository

    def get_all_boards(self):
        return self.board_repository.get_all_boards()
