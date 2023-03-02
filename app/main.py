from fastapi import FastAPI

from app.controller.board import board
from app.controller.comments import comments
from app.log.logging import add_response_time_tracker

app = FastAPI()

app.include_router(board.router)
app.include_router(comments.router)

app.middleware("http")(add_response_time_tracker)


@app.get("/")
async def root():
    return {"Hello": "World"}
