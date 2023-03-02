from app.test.test_sql import client


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_board():
    response = client.get('/board/')
    assert response.status_code == 200

    test_data = {
        "title": "test_1",
        "body": "test_body",
        "password": "test_password",
        "name": "name"
    }

    response = client.post("/board/", json=test_data)
    assert response.status_code == 201
    print(response.json())
    assert response.json() == {
        "title": "test_1",
        "body": "test_body",
        "name": "name"
    }