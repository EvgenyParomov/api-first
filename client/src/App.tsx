import React from "react";
import "./App.css";
import { apiModel, todosApi } from "./shared/api/generated";
import { nanoid } from "nanoid";
import { useQueryClient } from "@tanstack/react-query";

function App() {
  const queryClient = useQueryClient();
  const { data: todos } = todosApi.useGetTodosListSuspense();

  const createTodoMutaion = todosApi.useCreateTodoItem({
    mutation: {
      onSettled: async () => {
        await queryClient.invalidateQueries(
          todosApi.getGetTodosListQueryOptions()
        );
      },
    },
  });

  const deleteTodoMutaion = todosApi.useDeleteTodoItem({
    mutation: {
      onSettled: async () => {
        await queryClient.invalidateQueries(
          todosApi.getGetTodosListQueryOptions()
        );
      },
      onMutate: async ({ todoId }) => {
        await queryClient.cancelQueries(todosApi.getGetTodosListQueryOptions());
        const previousTodos = queryClient.getQueryData<apiModel.Todo[]>(
          todosApi.getGetTodosListQueryKey()
        );
        if (previousTodos) {
          queryClient.setQueryData<apiModel.Todo[]>(
            todosApi.getGetTodosListQueryKey(),
            previousTodos.filter((todo) => todo.id !== todoId)
          );
        }
        return { previousTodos };
      },
    },
  });

  const updateTodoMutaion = todosApi.useUpdateTodoItem({
    mutation: {
      onSettled: async () => {
        await queryClient.invalidateQueries(
          todosApi.getGetTodosListQueryOptions()
        );
      },
      onMutate: async ({ data, todoId }) => {
        await queryClient.cancelQueries(todosApi.getGetTodosListQueryOptions());
        const previousTodos = queryClient.getQueryData<apiModel.Todo[]>(
          todosApi.getGetTodosListQueryKey()
        );
        if (previousTodos) {
          queryClient.setQueryData<apiModel.Todo[]>(
            todosApi.getGetTodosListQueryKey(),
            previousTodos.map((todo) =>
              todo.id === todoId ? { ...todo, ...data } : todo
            )
          );
        }
        return { previousTodos };
      },
    },
  });

  const handleSubmit: React.FormEventHandler<HTMLFormElement> = (e) => {
    e.preventDefault();
    if (e.target instanceof HTMLFormElement) {
      const formData = new FormData(e.target as HTMLFormElement);

      const text = formData.get("text");

      createTodoMutaion.mutate({
        data: {
          id: nanoid(),
          completed: false,
          text: text as string,
          createdAt: new Date().toISOString(),
        },
      });

      e.target.reset();
    }
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <input name="text" type="text" />
        <button type="submit" disabled={createTodoMutaion.isPending}>
          Submit
        </button>
      </form>
      <div>
        {todos?.map((todo) => (
          <div key={todo.id}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() =>
                updateTodoMutaion.mutate({
                  data: { completed: !todo.completed },
                  todoId: todo.id,
                })
              }
            />
            {todo.text}
            <button
              onClick={() => deleteTodoMutaion.mutate({ todoId: todo.id })}
            >
              Delete
            </button>
          </div>
        ))}
      </div>
    </>
  );
}

export default App;
