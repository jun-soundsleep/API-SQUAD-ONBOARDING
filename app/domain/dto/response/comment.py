from pydantic import BaseModel

from app.domain.dto.request.comments import Comments


class CommentsResponse(BaseModel):
    board_id: int
    id: int
    content: str


class CommentsCreateResponse(Comments):
    pass
