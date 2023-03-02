from abc import ABC, abstractmethod

from app.dto.request.comments import CommentsCreateRequest, CommentsReadRequest
from app.mapper.models import Comments


class ICommentsRepository(ABC):
    @abstractmethod
    def create_comment(self, content: CommentsCreateRequest) -> bool:
        pass

    @abstractmethod
    def read_comments(self, board_id: CommentsReadRequest) -> list[Comments]:
        pass