from typing import Optional

from pydantic import BaseModel


class BoardCreateRequest(BaseModel):
    id: Optional[int]
    title: str
    body: str
    password: str
    name: str


class BoardSkipLimit(BaseModel):
    skip: int = 0
    limit: int = 10


class BoardUpdateRequest(BaseModel):
    id: int
    password: str
    title: Optional[str]
    body: Optional[str]
    name: Optional[str]
