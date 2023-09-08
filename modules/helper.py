filePath = 'todos.txt'


def write_todos(values):
    """ Write the to do items list in the text file. """
    with open(filePath, 'w') as file:
        file.writelines(values)


def get_todos():
    """ Read a text file and return the list of values. """
    with open(filePath, 'r') as file:
        todos = file.readlines()
    return todos

print(help(get_todos))