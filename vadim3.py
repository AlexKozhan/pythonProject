from tkinter import *

root = Tk()
f1 = Frame(borderwidth=1)
f2 = Frame(borderwidth=1)

e1 = Entry(f1, width=30, relief=SOLID, font="Arial 15")
b1 = Button(f1, text="Открыть", height=2, width=15, font="Arial 13")
b2 = Button(f1, text="Сохранить", height=2, width=15, font="Arial 13")
t1 = Text(f2, width=80, height=20)
scroll = Scrollbar(f2, command=t1.yview)

def b1Funk(event):
    global file
    file = open(f"{e1.get()}", "w")

def b2Funk(event):
    file.write("")
    file.write(t1.get(1.0, END))
f1.pack()
f2.pack()
e1.pack(ipadx=10, side=LEFT)
b1.pack(side=LEFT)
b1.bind("<Button-1>", b1Funk)
b2.pack(side=LEFT)
b2.bind("<Button-1>", b2Funk)
t1.pack(side=LEFT)
scroll.pack(side=LEFT, fill=Y)
t1.config(yscrollcommand=scroll.set)

root.mainloop()