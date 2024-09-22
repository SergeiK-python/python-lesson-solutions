import tkinter as tk


def put_button(_window, text, x, y, command):
    button = tk.Button(_window, text=text, width=4, height=2, command=command)
    button.place(x=x, y=y)
    return button


def put_edit(_window, text, x, y):
    edit = tk.Entry(_window, width=40)
    edit.place(x=x+60, y=y)
    edit.insert(0, "0")
    label = tk.Label(window, width=7, text=text)
    label.place(x=x, y=y)
    return edit


def get_args():
    arg1 = int(edit_first.get())
    arg2 = int(edit_second.get())
    return arg1, arg2


def update_result(result):
    edit_result.delete(0, "end")
    edit_result.insert(0, result)


def add():
    arg = get_args()
    res = arg[0] + arg[1]
    update_result(res)


def sub():
    arg = get_args()
    res = arg[0] - arg[1]
    update_result(res)


def mul():
    arg = get_args()
    res = arg[0] * arg[1]
    update_result(res)


def div():
    arg = get_args()
    res = arg[0] / arg[1]
    update_result(res)


window = tk.Tk()
window.title("hello")
window.geometry("350x350")
window.resizable(False, False)

button_add = put_button(window, "+", 10, 100, command=add)
button_sub = put_button(window, "-", 50, 100, command=sub)
button_mul = put_button(window, "*", 10, 140, command=mul)
button_div = put_button(window, "/", 50, 140, command=div)

edit_first = put_edit(window, "arg_left", 10, 25)
edit_second = put_edit(window, "arg_right", 10, 50)
edit_result = put_edit(window, "result", 10, 75)

window.mainloop()
