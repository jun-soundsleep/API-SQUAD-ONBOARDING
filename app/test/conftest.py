import pytest
from sqlalchemy import create_engine
from sqlalchemy.future import engine
from sqlalchemy.orm import Session, sessionmaker
from starlette.testclient import TestClient

from app.main import app
from app.mapper.db.database import Base, get_db
from app.mapper.models import Comments, Boards

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def delete_board_table():
    with Session(bind=engine) as session:
        session.query(Boards).delete()
        session.commit()


@pytest.fixture
def delete_comment_table():
    with Session(bind=engine) as session:
        session.query(Comments).delete()
        session.commit()


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def create_board_data_only_one():
    with Session(bind=engine) as session:
        test_data = {
            "title": "test_1",
            "body": "test_body",
            "password": "test_password",
            "name": "name"
        }
        boards = Boards(title=test_data["title"], body=test_data['body'],
                        password=test_data["password"], name="name")
        session.add(boards)
        session.commit()


@pytest.fixture
def create_comment_data_with_creating_board_data_ten_length(create_board_data_only_one):
    test_data = {
        "content": "string",
        "board_id": "board_id"
    }
    test_datas = [test_data for _ in range(10)]

    with Session(bind=engine) as session:
        for item in test_datas:
            board_data_id = session.query(Boards).first().id
            comment = Comments(
                content='hello',
                board_id=board_data_id
            )
            print(item)
            session.add(comment)
            session.commit()

    return board_data_id