from tkinter import *
from tkinter.ttk import *
import math

root = Tk()
root.title("Calculator")
root.resizable(False, False)
root.iconbitmap("C:\\Users\\ANIL PC\\Desktop\\calc.ico")
root.configure(background='#bdc3c7')
entryText = StringVar()
ans = 0
equation = ""

entry = Entry(width=50, textvariable=entryText).grid(row=1, column=1, columnspan=4, padx=2, pady=3)

btnClear = Button(text="C", command=lambda:reset()).grid(row=2, column=1)
btnSqrt = Button(text="√", command=lambda:sqrt()).grid(row=2, column=2, pady=1)
btnSquare = Button(text="x²", command=lambda:square()).grid(row=2, column=3)
btnEquals = Button(text="=", command=lambda:calc()).grid(row=2, column=4, pady=1)

btn7 = Button(text="7", command=lambda:setText("7")).grid(row=3, column=1)
btn8 = Button(text="8", command=lambda:setText("8")).grid(row=3, column=2, pady=1)
btn9 = Button(text="9", command=lambda:setText("9")).grid(row=3, column=3)
btnDiv = Button(text="÷", command=lambda:setText("/")).grid(row=3, column=4, padx=1, pady=1)

btn4 = Button(text="4", command=lambda:setText("4")).grid(row=4, column=1)
btn5 = Button(text="5", command=lambda:setText("5")).grid(row=4, column=2, pady=1)
btn6 = Button(text="6", command=lambda:setText("6")).grid(row=4, column=3)
btnInto = Button(text="×", command=lambda:setText("*")).grid(row=4, column=4, pady=1)

btn1 = Button(text="1", command=lambda:setText("1")).grid(row=5, column=1)
btn2 = Button(text="2", command=lambda:setText("2")).grid(row=5, column=2, pady=1)
btn3 = Button(text="3", command=lambda:setText("3")).grid(row=5, column=3)
btnMinus = Button(text="-", command=lambda:setText("-")).grid(row=5, column=4, pady=1)

btnPM = Button(text="±", command=lambda:plusMinus()).grid(row=6, column=1)
btn0 = Button(text="0", command=lambda:setText("0")).grid(row=6, column=2, pady=1)
btnPoint = Button(text=".", command=lambda:setText(".")).grid(row=6, column=3)
btnPlus = Button(text="+", command=lambda:setText("+")).grid(row=6, column=4, pady=1)

def setText(text):
    currentText = entryText.get()
    if currentText == "Error":
        entryText.set(text)
    else:
        entryText.set(currentText+text)

def sqrt():
    global ans
    try:
        number = calc()
        entryText.set(math.sqrt(number))
    except:
        entryText.set("Error")

def square():
    global ans
    try:
        number = calc()
        entryText.set(number * number)
    except:
        pass

def calc():
    global ans, equation
    try:
        equation = entryText.get()
        entryText.set(eval(equation))
        ans = int(entryText.get())
        return ans
    except:
        pass
        
def plusMinus():
    global ans
    number = calc()
    entryText.set(ans * -1)

def reset():
    entryText.set("")
