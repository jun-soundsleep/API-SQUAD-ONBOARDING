from app.mapper.models import boards
from app.test.test_sql import client, delete_table
from fastapi import status


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_board():
    delete_table(boards.Boards)

    test_data = {
        "title": "test_1",
        "body": "test_body",
        "password": "test_password",
        "name": "name"
    }

    test_data_without_password = {
        "title": "test_1",
        "body": "test_body",
        "name": "name"
    }
    board_get_url = '/board?skip=0&limit=10'

    post_response = client.post('/board', json=test_data)
    assert post_response.status_code == status.HTTP_201_CREATED
    assert post_response.json() == test_data_without_password

    get_response = client.get(board_get_url)
    assert get_response.status_code == status.HTTP_200_OK
    response_data_to_test = get_response.json()[0]
    del response_data_to_test['id']
    assert response_data_to_test == test_data_without_password

    test_data_new_title = "test_2"
    test_data['id'] = get_response.json()[0]['id']
    test_data['title'] = test_data_new_title

    patch_response = client.patch("/board/", json=test_data)
    assert patch_response.status_code == status.HTTP_200_OK

    get_response_second = client.get(board_get_url)
    assert get_response_second.status_code == status.HTTP_200_OK
    assert get_response_second.json()[0]['title'] == test_data_new_title

    delete_response = client.delete(f'/board?id={test_data["id"]}')
    assert delete_response.status_code == status.HTTP_200_OK

    get_response_third = client.get(board_get_url)
    assert get_response_third.status_code == status.HTTP_200_OK
    assert len(get_response_third.json()) == 0
