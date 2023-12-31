from modules.helper import get_todos, write_todos
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'].capitalize() + "\n"
            todos.append(new_todo)
            write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()

