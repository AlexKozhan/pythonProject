from tkinter import *

root = Tk()

f1 = Frame(borderwidth=1, relief=SOLID)
f2 = Frame(borderwidth=2, relief=SOLID)
f3 = Frame(borderwidth=1)
f4 = Frame(borderwidth=1)
f5 = Frame(borderwidth=1, relief=SOLID)
l1 = Label(f1, text="Введите первое число: ", height=2, font=("Roboto", 12, "bold"),bg="lightgrey")
e1 = Entry(f2,width=16, justify=CENTER, font="Arial 13")
b1 = Button(text="Ввести", font="Roboto 13", width=16, height=2)
b2 = Button(f3, text="+", font="Roboto 13", width=5, height=2)
b3 = Button(f3, text="-", font="Roboto 13", width=5, height=2)
b4 = Button(f4, text="*", font="Roboto 13", width=5, height=2)
b5 = Button(f4, text="/", font="Roboto 13", width=5, height=2)
l2 = Label(text="Вычислить: ", font="Roboto 13", bg="grey")
l3 = Label(text="Результат: ", font=("Roboto", 13, "bold"))
l4 = Label(f5, width=16, font="Arial 13")
b6 = Button(text="Очистить", font="Arial 13", width=16)

def clear(event):
    l4["text"] = " "
    numbrs.clear()
b6.bind("<Button-1>", clear)

numbrs = []
def plus(event):
    try:
        l4['text'] = f"{numbrs[0]}+{numbrs[1]}={numbrs[0]+numbrs[1]}"
    except:
        l4['text'] = "Ошибка"
b2.bind("<Button-1>", plus)
def minus(event):
    try:
        l4['text'] = f"{numbrs[0]}-{numbrs[1]}={numbrs[0]-numbrs[1]}"
    except:
        l4['text'] = "Ошибка"
b3.bind("<Button-1>", minus)



def multiply(event):
    try:
        l4['text'] = f"{numbrs[0]}*{numbrs[1]}={numbrs[0]*numbrs[1]}"
    except:
        l4['text'] = "Ошибка"
b4.bind("<Button-1>", multiply)

def division(event):
    try:
        l4['text'] = f"{numbrs[0]}/{numbrs[1]}={numbrs[0]/numbrs[1]}"
    except:
        l4['text'] = "Ошибка"
b5.bind("<Button-1>", division)
def enter(event):
    try:
        numbrs.append(float(e1.get()))
        e1.delete(0, END)
        l1['text'] = "Введите второе число: "
    except:
        pass
b1.bind("<Button-1>", enter)
f1.pack()
f2.pack()
l1.pack()
e1.pack()
b1.pack()
l2.pack()
f3.pack()
b2.pack(side=LEFT)
b3.pack(side=LEFT)
f4.pack()
b4.pack(side=LEFT)
b5.pack(side=LEFT)
l3.pack()
l4.pack()
f5.pack()
b6.pack()


root.mainloop()