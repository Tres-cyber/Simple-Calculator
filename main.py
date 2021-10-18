import tkinter

root = tkinter.Tk()
root.title("Calculator")
root.geometry("180x250")
expression = ""


# function
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)


def clear():
    global expression
    expression = ""
    label_result.config(text=expression)


def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
            label_result.config(text=result)
        except:
            result = "Error"
            expression = ""
    label_result.config(text=result)


# gui
label_result = tkinter.Label(root, text="", height=3, width=5)
label_result.grid(row=0, column=0, columnspan=5)

# 1st row
button_1 = tkinter.Button(root, text="1", width=5, height=2, command=lambda: add("1"))
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(root, text="2", width=5, height=2, command=lambda: add("2"))
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root, text="3", width=5, height=2, command=lambda: add("3"))
button_3.grid(row=1, column=2)

button_divide = tkinter.Button(root, text="/", height=2, width=5, command=lambda: add("/"))
button_divide.grid(row=1, column=3)

# second row
button_4 = tkinter.Button(root, text="4", width=5, height=2, command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(root, text="5", width=5, height=2, command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(root, text="6", width=5, height=2, command=lambda: add("6"))
button_6.grid(row=2, column=2)

button_multiply = tkinter.Button(root, text="*", width=5, height=2, command=lambda: add("*"))
button_multiply.grid(row=2, column=3)

# third row

button_7 = tkinter.Button(root, text="7", width=5, height=2, command=lambda: add("7"))
button_7.grid(row=3, column=0)

button_8 = tkinter.Button(root, text="8", width=5, height=2, command=lambda: add("8"))
button_8.grid(row=3, column=1)

button_9 = tkinter.Button(root, text="9", width=5, height=2, command=lambda: add("9"))
button_9.grid(row=3, column=2)

button_subtraction = tkinter.Button(root, text="-", width=5, height=2, command=lambda: add("-"))
button_subtraction.grid(row=3, column=3)

# fourth row
button_clear = tkinter.Button(root, text="C", width=5, height=2, bg="gray", command=lambda: clear())
button_clear.grid(row=4, column=0)

button_zero = tkinter.Button(root, text="0", width=5, height=2, command=lambda: add("0"))
button_zero.grid(row=4, column=1)

button_dot = tkinter.Button(root, text=".", width=5, height=2, command=lambda: add("."))
button_dot.grid(row=4, column=2)

button_add = tkinter.Button(root, text="+", width=5, height=2, command=lambda: add("+"))
button_add.grid(row=4, column=3)

# fifth row
button_equals = tkinter.Button(root, text="=", width=10, height=2, bg="gray", command=lambda: calculate())
button_equals.grid(row=5, column=0, columnspan=10)

root.mainloop()

