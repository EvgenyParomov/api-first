# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.todo import Todo
from openapi_server.models.todo_patch import TodoPatch


class BaseTodosApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTodosApi.subclasses = BaseTodosApi.subclasses + (cls,)
    def create_todo_item(
        self,
        todo: Todo,
    ) -> Todo:
        ...


    def delete_todo_item(
        self,
        todoId: str,
    ) -> None:
        ...


    def get_todos_list(
        self,
    ) -> List[Todo]:
        ...


    def update_todo_item(
        self,
        todoId: str,
        todo_patch: TodoPatch,
    ) -> Todo:
        ...
