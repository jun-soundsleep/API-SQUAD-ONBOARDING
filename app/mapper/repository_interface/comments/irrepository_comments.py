from abc import ABC, abstractmethod

from app.dto.request.comments import CommentsCreateRequest


class ICommentsRepository(ABC):
    @abstractmethod
    def create_comment(self, content: CommentsCreateRequest) -> bool:
        pass

    @abstractmethod
    def read_comments(self):
        pass