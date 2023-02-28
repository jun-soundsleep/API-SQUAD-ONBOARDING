from typing import Optional

from pydantic import BaseModel


class Board_create_request(BaseModel):
    id: Optional[int]
    title: str
    body: str
    password: str
    name: str


class Board_skip_limit(BaseModel):
    skip: int = 0
    limit: int = 10
