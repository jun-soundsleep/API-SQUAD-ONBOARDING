from fastapi import FastAPI

from app.application.board import board
from app.data.db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(board.router)


@app.get("/")
def main():
    return {"main": "hi"}
