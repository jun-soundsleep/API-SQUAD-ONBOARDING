from fastapi import status


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_board(client, delete_board_table):
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


def test_read_comment(client, delete_comment_table, create_comment_data_with_creating_board_data_ten_length):
    response = client.get(f"/comment?board_id={create_comment_data_with_creating_board_data_ten_length}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10
    assert response.json()[0]['board_id'] == create_comment_data_with_creating_board_data_ten_length


def test_create_comment(client, delete_comment_table, delete_board_table, create_board_data_only_one):
    board_get_url = '/board?skip=0&limit=10'

    get_board_response = client.get(board_get_url)
    assert get_board_response.status_code == status.HTTP_200_OK

    board_id = get_board_response.json()[0]['id']
    test_data = {
        "content": "string",
        "board_id": board_id
    }

    post_board_response = client.post("/comment", json=test_data)
    assert post_board_response.status_code == status.HTTP_201_CREATED
    assert post_board_response.json() == test_data

    comment_read_response = client.get(f"/comment?board_id={test_data['board_id']}")
    assert comment_read_response.status_code == status.HTTP_200_OK
    assert comment_read_response.json()[0]['content'] == test_data['content']
