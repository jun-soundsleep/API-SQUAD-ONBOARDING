from typing import Optional

from pydantic import BaseModel


class Comments(BaseModel):
    content: str
    board_id: int


class CommentsCreateRequest(Comments):
    pass
