from abc import ABC, abstractmethod

from app.domain.dto.request.comments import CommentsCreateRequest
from app.mapper.models import Comments


class ICommentsRepository(ABC):
    @abstractmethod
    def create_comment(self, content: CommentsCreateRequest) -> bool:
        pass

    @abstractmethod
    def read_comments(self, board_id: int) -> list[Comments]:
        pass