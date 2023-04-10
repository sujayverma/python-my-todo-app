def readfile(filePath="todos.txt") -> list:
    # file = open("./udemy-python-course/todos.txt", "r")
    # todos = file.readlines()
    # file.close()
    # USE of with context for file handling.
    """Reads a test file and return the list of items."""
    with open(filePath, "r") as file:
        todos = file.readlines()
    return todos


def writefile(todos, filePath="todos.txt") -> None:
    """Writes the text file with the list of items"""
    with open(filePath, "w") as file:
        file.writelines(todos)
