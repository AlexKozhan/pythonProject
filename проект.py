from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session
from tkinter import *
engine = create_engine("mysql+pymysql://root:VFx33gA51542212@localhost/newdb", echo=True)


root = Tk()
root.title("Магазин")
f1 = Frame()
f2 = Frame()


class Base(DeclarativeBase):
    pass


class Food(Base):
    __tablename__ = "food"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50))
    manufacturer = Column(String(50))
    price = Column(Integer)
    quantity = Column(Integer)

    def __repr__(self):
        return f"{self.id} {self.type} {self.manufacturer} {self.price} {self.quantity}"


Base.metadata.create_all(bind=engine)

def fromDBtoText():
    t.delete(1.0, END)
    with Session(autoflush=False, bind=engine) as db:
        obj = db.query(Food).all()
        for i in obj:
            t.insert(END, str(i)+"\n")

def loadFile(e):
    fname=e.get()
    return f"{fname}"

def toBase():
    s = loadFile(e1)
    with Session(autoflush=False, bind=engine) as db:
        f = open(s, 'r')
        mas_str = f.readlines()
        mas_obj = []
        for i in mas_str:
            mas_inf = i.split(" ")
            mas_obj.append(Food(type=mas_inf[0], manufacturer=mas_inf[1], price=int(mas_inf[2]), quantity=int(mas_inf[3])))
        db.add_all(mas_obj)
        db.commit()

def delBase():
    s=loadFile(e2)
    with Session(autoflush=False, bind=engine) as db:
        f = open(s, 'r')
        mas_str = f.readlines()
        for i in mas_str:
            mas_inf = i.split(" ")
            obj = db.query(Food).filter(Food.type == mas_inf[0]).first()
            if obj.quantity>=int(mas_inf[3]):
                obj.quantity-=int(mas_inf[3])
            else:
                errorWindow(mas_inf[0])
                return
        db.commit()

def errorWindow(s):
    errorWindow = Tk()
    errorWindow.title("Ошибка")
    l=Label(errorWindow, text="\nНевозможно совершить покупку.\n Нет нужного количества товара \n"+str(s)+"\n", font=("Arial", 27))
    l.pack()
    errorWindow.mainloop()

f1.pack(side=LEFT)
f2.pack(side=LEFT)
e1 = Entry(f2, width=25,font=("Arial", 27))
b1 = Button(f2, text="Загрузить товары в БД", command=toBase, width=24, font=("Arial", 27))
e2 = Entry(f2, width=25, font=("Arial", 27))
b2 = Button(f2, text="Загрузить файл покупок", command=delBase, width=24, font=("Arial", 27))
e1.pack()
b1.pack()
e2.pack()
b2.pack()
t=Text(f1, width=50, height=20 )
t.pack()
b3 = Button(f1, text="Показать текущее \n содержимое БД",  command=fromDBtoText, width=19, height=2, font=("Arial", 27))
b3.pack()
root.mainloop()