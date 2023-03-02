from fastapi import Depends

from app.domain.dto.request.comments import CommentsCreateRequest, CommentsReadRequest
from app.mapper.models import Comments
from app.mapper.repository.comments.comments import CommentsRepository


class CommentsService:

    def __init__(self, comments_repository: CommentsRepository = Depends()):
        self.comments_repository = comments_repository

    def create_comment(self, comment: CommentsCreateRequest):
        self.comments_repository.create_comment(comment)

    def read_comments(self, board_id: CommentsReadRequest) -> list[Comments]:
        return self.comments_repository.read_comments(board_id)