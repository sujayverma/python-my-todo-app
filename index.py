import streamlit
import functions_for_todos

todos = functions_for_todos.readfile()


def add_todo() -> None:
    todo = streamlit.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions_for_todos.writefile(todos)


streamlit.title("My Todo App")
streamlit.subheader("This is my todo app.")
streamlit.write("This app is to increase you productivity.")
# print(todos)
# i = 0
for index, todo in enumerate(todos):
    key = todo + str(index)
    # i = i + 1
    checked = streamlit.checkbox(todo, key=key)
    if checked:
        todos.pop(index)
        functions_for_todos.writefile(todos, 'todos.txt')
        del streamlit.session_state[key]
        streamlit.experimental_rerun()

streamlit.text_input(
    label="Enter your todo: ",
    placeholder="Add your todos here...",
    on_change=add_todo,
    key="new_todo",
)

# streamlit.session_state
