"""
Name: Calculator
Made By: Mads Hermansen
Github: https://github.com/KarlofKuwait
"""
from tkinter import *

def Buttonclick(Numbers):
    global operator
    operator=operator+ str(Numbers)
    Inputs.set(operator)

def ClearScreen():
    global operator
    operator = ""
    Inputs.set("")

def EqualsSign():
    global operator
    if eval(operator) >= 100000000000:
        Inputs.set("Overflow")
    elif eval(operator) <= -100000000000:
        Inputs.set("Overflow")
    else:
        sumup = str(eval(operator))
        Inputs.set(sumup)
        operator = sumup

Calculator = Tk()
Calculator.title("Calculator")
Calculator.resizable(False, False)
Calculator.configure(background="gray30")
Inputs = StringVar()
operator = ""

Display = Entry(Calculator,
                font=("arial", 25, "bold"),
                textvariable=Inputs,
                bd=30,
                insertwidth=4,
                bg="gray30",
                justify="right").grid(columnspan=5)

Number0 = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="0",
                 command=lambda:Buttonclick(0),
                 bg="gray30").grid(column=1, row=4)

Dot = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text=".",
                 command=lambda:Buttonclick("."),
                 bg="gray30").grid(column=2, row=4)

Equals = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="=",
                 command=EqualsSign,
                 bg="gray30").grid(column=3, row=4)

Addition = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="+",
                 command=lambda: Buttonclick("+"),
                 bg="gray30").grid(column=4, row=4)

Number1 = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="1",
                 command=lambda: Buttonclick(1),
                 bg="gray30").grid(column=1, row=3)

Number2 = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="2",
                 command=lambda: Buttonclick(2),
                 bg="gray30").grid(column=2, row=3)

Number3 = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="3",
                 command=lambda: Buttonclick(3),
                 bg="gray30").grid(column=3, row=3)

Subtract = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="-",
                 command=lambda: Buttonclick("-"),
                 bg="gray30").grid(column=4, row=3)


Number4 = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="4",
                 command=lambda: Buttonclick(4),
                 bg="gray30").grid(column=1, row=2)

Number5 = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="5",
                 command=lambda: Buttonclick(5),
                 bg="gray30").grid(column=2, row=2)

Number6 = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="6",
                 command=lambda: Buttonclick(6),
                 bg="gray30").grid(column=3, row=2)

Multiplication = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="×",
                 command=lambda: Buttonclick("*"),
                 bg="gray30").grid(column=4, row=2)

Number7 = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="7",
                 command=lambda: Buttonclick(7),
                 bg="gray30").grid(column=1, row=1)

Number8 = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="8",
                 command=lambda: Buttonclick(8),
                 bg="gray30").grid(column=2, row=1)

Number9 = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="9",
                 command=lambda: Buttonclick(9),
                 bg="gray30").grid(column=3, row=1)

Division = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="÷",
                  command=lambda: Buttonclick("/"),
                 bg="gray30").grid(column=4, row=1)

Number7 = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="7",
                 command=lambda: Buttonclick(7),
                 bg="gray30").grid(column=0, row=1)

Exponent = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="^x",
                 command=lambda: Buttonclick("**"),
                 bg="gray30").grid(column=0, row=1)

Quit = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 text="Quit",
                 command=Calculator.quit,
                 bg="gray30").grid(column=0, row=4)

Clear = Button(Calculator,
                 padx=16,
                 bd=8,
                 fg="black",
                 font=("arial", 20, "bold"),
                 width=2,
                 height=3,
                 text="C",
                 command=ClearScreen,
                 bg="gray30").grid(column=0, rowspan=2, row=2)

Calculator.mainloop()
