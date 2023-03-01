from fastapi import Depends

from app.dto.request.comments import CommentsCreateRequest
from app.mapper.repository.comments.comments import CommentsRepository


class CommentsService:

    def __init__(self, comments_repository: CommentsRepository = Depends()):
        self.comments_repository = comments_repository

    def create_comment(self, comment: CommentsCreateRequest):
        self.comments_repository.create_comment(comment)
