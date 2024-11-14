from tkinter import *

win = Tk()
win. title("Calculator")
win.geometry("300x350")
win.config(bg="black")
win.resizable(False, False)


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def pressequal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

def key_press(event):
    global expression
    key = event.char
    if key in "0123456789+-*/.%":
        expression += key
    elif key == "\r":
        pressequal()
    elif key == "\x08":
        expression = expression[:-1]
        equation.set(expression)

win.bind("<Key>", key_press)

def clear():
    global expression
    expression = ""
    equation.set("")

def back():
    global expression
    try:
        expression = expression[:-1]
        equation.set(expression)
    except:
        return

expression = ""
equation = StringVar()

empty_column = Label(win, text="", height=4, width=0, bg="black")
empty_column.grid(column=0, row=0)
expresion_field = Entry(win, textvariable=equation, width=49)
expresion_field.grid(columnspan=4, ipady=10, row=0)


clearbutton = Button(win, text="AC", command=clear, bg="#FA9906", width=7, height=2)
clearbutton.grid(column=0, row=1)
backbutton = Button(win, text="←", command=back, bg="#FA9906", width=7, height=2)
backbutton.grid(column=1, row=1)
percentage = Button(win, text="%", command=lambda: press("%"), bg="#FA9906", width=7, height=2)
percentage.grid(column=2, row=1)

button9 = Button(text="9", command=lambda: press(9), bg="gray", fg="white", height=2, width=7)
button9.grid(column=2, row=2)
button8 = Button(text="8", command=lambda: press(8), bg="gray", fg="white", width=7, height= 2)
button8.grid(column=1, row=2)
button7 = Button(text="7", command=lambda: press(7), bg="gray", fg="white", width=7, height= 2)
button7.grid(column=0, row=2)
button6 = Button(text="6", command=lambda: press(6), bg="gray", fg="white", width=7, height= 2)
button6.grid(column=2, row=3)
button5 = Button(text="5", command=lambda: press(5), bg="gray", fg="white", width=7, height= 2)
button5.grid(column=1, row=3)
button4 = Button(text="4", command=lambda: press(4), bg="gray", fg="white", width=7, height= 2)
button4.grid(column=0, row=3)
button3 = Button(text="3", command=lambda: press(3), bg="gray", fg="white", width=7, height= 2)
button3.grid(column=2, row=4)
button2 = Button(text="2", command=lambda: press(2), bg="gray", fg="white", width=7, height= 2)
button2.grid(column=1, row=4)
button1 = Button(text="1", command=lambda: press(1), bg="gray", fg="white", width=7, height= 2)
button1.grid(column=0, row=4)
button0 = Button(text="0", command=lambda: press(0), bg="gray", fg="white", width=7, height= 2)
button0.grid(column=0, row=5)
decimal = Button(win, text=".", command=lambda: press("."), bg="gray", fg="white", width=7, height=2)
decimal.grid(column=2, row=5)
button00 = Button(win, text="00", command=lambda: press("00"), bg="gray", fg="white", width=7, height=2)
button00.grid(column=1, row=5)
equal = Button(win, text="=", command=pressequal, bg="#FFCD03", width=7, height=2)
equal.grid(column=3, row=5)
empty = Label(win, text="", height=18, width=0, bg="black")
empty.grid(rowspan=5, row=1, column=4)

divide = Button(win, text="/", command=lambda: press("/"), bg="#FA9906", width=7, height=2)
divide.grid(row=1, column=3)
multiply = Button(win, text="x", command=lambda: press("*"), bg="#FA9906", width=7, height=2)
multiply.grid(row=2, column=3)
minus = Button(win, text="-", command=lambda: press("-"), bg="#FA9906", width=7, height=2)
minus.grid(row=3, column=3)
plus = Button(win, text="+", command=lambda: press("+"), bg="#FA9906", width=7, height=2)
plus.grid(row=4, column=3)


win.mainloop()