import streamlit as st
import todos_functions

todos = todos_functions.fetch_todos()


def add_todo():
    todo_local = st.session_state["new_todo"]
    todos.append(todo_local + "\n")
    todos_functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("this app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        todos_functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo",
              placeholder="add new todo",
              on_change=add_todo,
              key="new_todo")
