from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.data.db.database import get_db
from app.data.models.user import User

router = APIRouter(
    prefix="/board",
    tags=["board"],
    responses={404: {"description": "Not found"}}
)


@router.get('')
def read_boards_item(db: Session = Depends(get_db)):
    return db.query(User).all()
