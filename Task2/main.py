from tkinter import *
import math

root = Tk()
root.title("Simple calculator")
root.geometry("620x500")
root.resizable(False,False)
calculation = ""  # Initialize the calculation string

def show(symbol):
    global calculation
    calculation += str(symbol)
    result.config(text=calculation)

def calculate():
    global calculation
    res = ""
    if calculation != "":
        try:
            # Define allowed operations and functions here
            allowed_symbols = "0123456789+-*/. "


            # Check if the input contains only allowed symbols
            if all(char in allowed_symbols for char in calculation):

                res = eval(calculation)
            else:
                res = "INVALID INPUT"
        except Exception as e:
            res = "MATH ERROR!"
        calculation = str(res)
    result.config(text=res)

def root_func():
    global calculation
    res=math.sqrt(int(calculation))
    calculation=str(res)
    result.config(text=calculation)

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def fact_func():
    global calculation
    res = factorial(int(calculation))
    print(res)
    calculation = str(res)
    result.config(text=calculation)
def clear():
    global calculation
    calculation = ""
    result.config(text=calculation)

result = Label(root, text=0, height=2, width=30, font=("Arial", 24), borderwidth=1, relief="solid", bg="white", fg="black")
result.grid(columnspan=6)  # Span 6 columns for the result label

buttons = [
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "", "0", ".",
]

row, col = 2, 0

for button_text in buttons:
    btn = Button(root, text=button_text, command=lambda text=button_text: show(text), width=12, height=3, font=("Arial", 14, "bold"))
    btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

btn_fact = Button(root, text="!", command=lambda: fact_func(), width=12, height=3, font=("Arial", 14, "bold"))
btn_fact.grid(row=5, column=0)

btn_calc = Button(root, text="=", command=lambda: calculate(), width=12, height=3, font=("Arial", 14, "bold"))
btn_calc.grid(row=5, column=3)

btnc = Button(root, text="C", command=lambda: clear(), width=25, height=3, font=("Arial", 14, "bold"), bg="#3697f5", fg="#fff")
btnc.grid(row=1, column=0, columnspan=2)

btn_root = Button(root, text="√",command=lambda :root_func(), width=12, height=3, font=("Arial", 14, "bold"))
btn_root.grid(row=1, column=2)

btn_div = Button(root, text="/", command=lambda: show("/"), width=12, height=3, font=("Arial", 14, "bold"))
btn_div.grid(row=1, column=3)

root.mainloop()
