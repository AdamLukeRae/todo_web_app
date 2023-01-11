def fetch_todos(filepath="todos.txt"):
    """return lines in file as a list
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """write lines in a file from a list
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
