from fastapi import Depends
from sqlalchemy.orm import Session

from app.mapper.models import Boards
from app.mapper.db.database import get_db
from app.mapper.models import Comments
from app.mapper.repository_interface.comments.irrepository_comments import ICommentsRepository
from app.dto.request.comments import CommentsCreateRequest, CommentsReadRequest


class CommentsRepository(ICommentsRepository):

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def create_comment(self, comment_content: CommentsCreateRequest):
        board = self.db.query(Boards).filter(Boards.id == comment_content.board_id).first()
        self.db.add(Comments(content=comment_content.content, board=board, board_id=board))
        self.db.commit()
        return True

    def read_comments(self, board_id: CommentsReadRequest) -> list[Comments]:
        data = self.db.query(Boards).filter(Boards.id == board_id).first()
        if data is None:
            return []
        else:
            return self.db.query(Boards).filter(Boards.id == board_id).first().comments

