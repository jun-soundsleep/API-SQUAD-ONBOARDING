from pydantic import BaseModel


class Comments(BaseModel):
    content: str
    board_id: int


class CommentsCreateRequest(Comments):
    pass


class CommentsReadRequest(BaseModel):
    board_id: int
