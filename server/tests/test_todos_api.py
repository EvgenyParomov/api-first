# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.todo import Todo  # noqa: F401
from openapi_server.models.todo_patch import TodoPatch  # noqa: F401


def test_create_todo_item(client: TestClient):
    """Test case for create_todo_item

    
    """
    todo = {"created_at":"2000-01-23T04:56:07.000+00:00","id":"id","text":"text","completed":1}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/todos",
    #    headers=headers,
    #    json=todo,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_todo_item(client: TestClient):
    """Test case for delete_todo_item

    
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/todos/{todoId}".format(todoId='todo_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_todos_list(client: TestClient):
    """Test case for get_todos_list

    
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/todos",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_todo_item(client: TestClient):
    """Test case for update_todo_item

    
    """
    todo_patch = {"text":"text","completed":1}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/todos/{todoId}".format(todoId='todo_id_example'),
    #    headers=headers,
    #    json=todo_patch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

