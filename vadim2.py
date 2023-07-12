from tkinter import *

root = Tk()

l1 = Label(width=20)
e1 = Entry(width=24, justify=CENTER)
b1 = Button(width=20, height=2, bg="#ff0000")
b2 = Button(width=20, height=2, bg="#ff7d00")
b3 = Button(width=20, height=2, bg="#ffff00")
b4 = Button(width=20, height=2, bg="#00ff00")
b5 = Button(width=20, height=2, bg="#007dff")
b6 = Button(width=20, height=2, bg="#0000ff")
b7 = Button(width=20, height=2, bg="#7d00ff")

def b1Funk(event):
    l1['text'] = "красный"
    e1.delete(0, END)
    e1.insert(0, b1['bg'])
b1.bind("<Button-1>", b1Funk)

def b2Funk(event):
    l1['text'] = "оранжевый"
    e1.delete(0, END)
    e1.insert(0, b2['bg'])
b2.bind("<Button-1>", b2Funk)

def b3Funk(event):
    l1['text'] = "желтый"
    e1.delete(0, END)
    e1.insert(0, b3['bg'])
b3.bind("<Button-1>", b3Funk)

def b4Funk(event):
    l1['text'] = "зеленый"
    e1.delete(0, END)
    e1.insert(0, b4['bg'])
b4.bind("<Button-1>", b4Funk)

def b5Funk(event):
    l1['text'] = "голубой"
    e1.delete(0, END)
    e1.insert(0, b5['bg'])
b5.bind("<Button-1>", b5Funk)

def b6Funk(event):
    l1['text'] = "синий"
    e1.delete(0, END)
    e1.insert(0, b6['bg'])
b6.bind("<Button-1>", b6Funk)

def b7Funk(event):
    l1['text'] = "фиолетовый"
    e1.delete(0, END)
    e1.insert(0, b7['bg'])
b7.bind("<Button-1>", b7Funk)

l1.pack()
e1.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()

root.mainloop()