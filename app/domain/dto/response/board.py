from pydantic import BaseModel


class BoardCreateResponse(BaseModel):
    title: str
    body: str
    name: str


class BoardUpdateResponse(BaseModel):
    title: str
    body: str
    name: str


class BoardReadResponse(BaseModel):
    id: int
    title: str
    body: str
    name: str
