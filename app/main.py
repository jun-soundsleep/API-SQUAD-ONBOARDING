from fastapi import FastAPI

from app.controller.board import board
from app.controller.comments import comments


app = FastAPI()

app.include_router(board.router)
app.include_router(comments.router)


@app.get("/")
def main():
    return {"main": "hi"}
