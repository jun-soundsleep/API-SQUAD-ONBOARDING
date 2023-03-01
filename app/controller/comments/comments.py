from fastapi import APIRouter, Depends

from app.dto.request.comments import CommentsCreateRequest, CommentsReadRequest
from app.service.comments.comments import CommentsService

router = APIRouter(
    prefix="/comment",
    tags=["comment"],
    responses={404: {"description": "Not found"}}
)


@router.get("")
def read_comments(board_id: int, commentService: CommentsService = Depends()):
    return commentService.read_comments(board_id)


@router.post("")
def create_comment(comment: CommentsCreateRequest, commentService: CommentsService = Depends()):
    return commentService.create_comment(comment)

