# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.todos_api_base import BaseTodosApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.todo import Todo
from openapi_server.models.todo_patch import TodoPatch


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


todos: Dict[str, Todo] = {}

@router.post(
    "/todos",
    responses={
        201: {"model": Todo, "description": "Todo item"},
    },
    tags=["todos"],
    response_model_by_alias=True,
)
async def create_todo_item(
    todo: Todo = Body(None, description=""),
) -> Todo:
    todos[todo.id] = todo
    return todo
    ...


@router.delete(
    "/todos/{todoId}",
    responses={
        204: {"description": "Delete success"},
    },
    tags=["todos"],
    response_model_by_alias=True,
)
async def delete_todo_item(
    todoId: str = Path(..., description=""),
) -> None:
    del todos[todoId]
    ...


@router.get(
    "/todos",
    responses={
        200: {"model": List[Todo], "description": "Todo list"},
    },
    tags=["todos"],
    response_model_by_alias=True,
)
async def get_todos_list(
) -> List[Todo]:
    return list(todos.values())
    ...


@router.patch(
    "/todos/{todoId}",
    responses={
        200: {"model": Todo, "description": "Todo item"},
    },
    tags=["todos"],
    response_model_by_alias=True,
)
async def update_todo_item(
    todoId: str = Path(..., description=""),
    todo_patch: TodoPatch = Body(None, description=""),
) -> Todo:
    todo = todos.get(todoId)

    if not todo:
        raise Exception("Todo not found")

    todo = Todo.from_dict({**todo.to_dict(), **todo_patch.to_dict()})
    todos[todo.id] = todo
    return todos[todoId]
    ...
