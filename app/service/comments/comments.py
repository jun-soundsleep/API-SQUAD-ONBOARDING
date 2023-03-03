from fastapi import Depends, HTTPException,status

from app.domain.dto.request.comments import CommentsCreateRequest
from app.domain.dto.response.comment import CommentsResponse
from app.mapper.models import Comments, Boards
from app.mapper.repository.board.repository_board import BoardRepository
from app.mapper.repository.comments.comments import CommentsRepository


class CommentsService:
    def __init__(self, comments_repository: CommentsRepository = Depends(),
                 board_repository: BoardRepository = Depends()):
        self.comments_repository = comments_repository
        self.board_repository = board_repository

    def create_comment(self, comment_content: CommentsCreateRequest) -> CommentsCreateRequest:
        board_item = self.board_repository.get_boards_item_by_id(comment_content.board_id)
        if board_item is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return self.comments_repository.create_comment(comment_content)

    def read_comments(self, board_id: int) -> list[CommentsResponse]:
        data = self.comments_repository.read_comments(board_id)
        return [CommentsResponse(board_id=item.board_id, id=item.id, content=item.content) for item in data]
