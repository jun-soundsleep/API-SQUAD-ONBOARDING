from fastapi import APIRouter, Depends, status

from app.domain.dto.request.comments import CommentsCreateRequest
from app.domain.dto.response.comment import CommentsCreateResponse, CommentsResponse
from app.service.comments.comments import CommentsService

router = APIRouter(
    prefix="/comment",
    tags=["comment"],
    responses={404: {"description": "Not found"}}
)


@router.get("", response_model=list[CommentsResponse])
def read_comments(board_id: int, commentService: CommentsService = Depends()):
    return commentService.read_comments(board_id)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=CommentsCreateResponse)
def create_comment(comment: CommentsCreateRequest, commentService: CommentsService = Depends()):
    return commentService.create_comment(comment)
