from tkinter import * #type: ignore

root = Tk()
root.title("Simple Calculator")
input = Entry(root, width=35, borderwidth=5)
input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

previous = ""  

def user_input(int):
    previous = input.get()
    input.delete(0, END)
    input.insert(0, str(previous) + str(int))

def clear():
    input.delete(0, END)

def user_operations(string):
    global previous
    previous = input.get()
    input.delete(0, END)

    match string:
        case '+':
            input.insert(0, previous + " " + string)
        case '-':
            input.insert(0, previous + " " + string)
        case '*':
            input.insert(0, previous + " " + string)
        case '/':
            input.insert(0, previous + " " + string)
        case _:
            quit()


def Del():
    existing = input.get()
    input.delete(0,END)
    new_existing = existing[:-1]
    input.insert(0,new_existing)

def result():
    expression = input.get() #string

    try:
        result = eval(expression)
        input.delete(0, END)
        input.insert(0, str(result))
    except Exception as e:
        input.delete(0, END)
        input.insert(0, "Error")
        print("Error:", e)


list = [f"Button{i+1}" for i in range(9, 0, -1)]

k = 1
j = 0
num = 9

for i in list:
    i = Button(root, text=num, padx=40, pady=20, command=lambda temp=num: user_input(temp), fg="Black", bg="#8B8000")
    i.grid(row=k, column=j)
    j += 1
    num -= 1
    if j % 3 == 0:
        k += 1
        j = 0

Button0 = Button(root, text=0, padx=40, pady=20, command=lambda: user_input(0), fg="Black", bg="#8B8000")
Button0.grid(row=4, column=1)

operators = ['+', '-', '*', '/']
Button_operators = [f"Button{i}" for i in operators]

num = 0

for i in Button_operators:
    i = Button(root, text=operators[num], padx=40, pady=20, command=lambda temp1=operators[num]: user_operations(temp1), bg="lightGreen")
    num += 1
    i.grid(row=num, column=3)

ButtonAns = Button(root, text="=", padx=40, pady=20, command=result, bg="Red", fg="Green")
ButtonAns.grid(row=4, column=2)

ButtonClear = Button(root, text="Clear", padx=30, pady=20, command=clear, bg="#FFCC99", fg="Black")
ButtonClear.grid(row=0, column=3)

ButtonDel = Button(root, text="DEL", padx=33, pady=20, command= Del, bg="Black", fg="White")
ButtonDel.grid(row=4, column=0,columnspan=1)

root.mainloop()
