from getpass import getpass
from tkinter import *
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String

root = Tk()

e1 = Entry(width=40, font=20)
b1 = Button(text="Set", font=20)
b2 = Button(text="Get", font=20)
l1 = Label(font="Arial 15", width=60, height=20, borderwidth=1, anchor=NW)



sqlite_database = "mysql+pymysql://root:VFx33gA51542212@localhost/newDB"
engine = create_engine(sqlite_database, echo=True)

class Base(DeclarativeBase):
    pass



class Journal(Base):
    __tablename__ = "Zhurnal"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250))
    ocenka = Column(Integer)
    def __repr__(self):
        return f"{self.id} {self.name} {self.ocenka}"

Base.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as db:
    ob = db.query(Journal).filter(Journal.name == "Ban").first()
    if (ob != None):
        print(ob)

def SetButtonFunk(event):
    with Session(autoflush=False, bind=engine) as db:
        ob = Journal(name=e1.get().split(' ')[0], ocenka=int(e1.get().split(' ')[1]))
        db.add(ob)
        db.commit()
        e1.delete(0, END)

def GetButtonFunk(event):
    with Session(autoflush=False, bind=engine) as db:
        people = db.query(Journal).all()
        l1['text'] = ''
        for p in people:
            l1['text'] = l1['text'] + "\n" + f"{p.id} {p.name} {p.ocenka}"


e1.pack()
b1.pack()
b1.bind("<Button-1>", SetButtonFunk)
b2.pack()
b2.bind("<Button-1>", GetButtonFunk)
l1.pack()

root.mainloop()