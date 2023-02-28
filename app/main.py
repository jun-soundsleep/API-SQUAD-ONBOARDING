from fastapi import FastAPI

from app.controller.board import board
from app.mapper.db.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(board.router)


@app.get("/")
def main():
    return {"main": "hi"}
