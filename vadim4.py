from tkinter import *

root = Tk()

f1 = Frame(borderwidth=1)
f2 = Frame(borderwidth=1)

rvar_1 = IntVar(value=0)

l1 = Label(f2, width=20, height=6, font="Arial 15")
def r1Funk():
    l1['text'] = "+133432125"
r1 = Radiobutton(f1, text="Вася", indicatoron=0, variable=rvar_1, value=0, font="Arial 13", bg="lightgrey", width=10, height=2, command=r1Funk)
def r2Funk():
    l1['text'] = "+91825092105"
r2 = Radiobutton(f1, text="Петя", indicatoron=0, variable=rvar_1, value=1, font="Arial 13", bg="lightgrey", width=10, height=2, command=r2Funk)
def r3Funk():
    l1['text'] = "+195991995"
r3 = Radiobutton(f1, text="Маша", indicatoron=0, variable=rvar_1, value=2, font="Arial 13", bg="lightgrey", width=10, height=2, command=r3Funk)

f1.pack(side=LEFT)
f2.pack(side=LEFT)
r1.pack(anchor=E)
r2.pack(anchor=E)
r3.pack(anchor=E)
l1.pack()
root.mainloop()