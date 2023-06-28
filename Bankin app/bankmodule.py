from tkinter import *
from tkinter import messagebox
import mysql.connector
con=mysql.connector.connect(
 host="localhost",
 user="root",
 password="12345",
 db="Bank"
    )
frame=Tk()
frame.geometry("700x400")
frame.title("Add Details to Database")
l1=Label(frame,text="Database")
l2=Label(frame,text="Acc_no")
l3=Label(frame,text="Name")
l4=Label(frame,text="Password")
l5=Label(frame,text="Total_Balance")
l6=Label(frame,text="PIN")
t1=Entry(width=20)
t2=Entry(width=20)
t3=Entry(width=20)
t4=Entry(width=20)
t5=Entry(width=20)
def Insert():
    Acc=t1.get()
    Name=t2.get()
    Pass=t3.get()
    Total=t4.get()
    Pin=t5.get()
    a="insert into customer values('"+Acc+"','"+Name+"','"+Pass+"','"+Total+"','"+Pin+"')"
    obj=con.cursor()
    obj.execute(a)
    con.commit()
    messagebox.showinfo("Message","Insert")
b=Button(frame,text="Sumbit",command=Insert)
l1.pack()
l2.place(x=100,y=80)
t1.place(x=250,y=80)
l3.place(x=100,y=150)
t2.place(x=250,y=150)
l4.place(x=100,y=210)
t3.place(x=250,y=210)
l5.place(x=100,y=270)
t4.place(x=250,y=270)
l6.place(x=100,y=330)
t5.place(x=250,y=330)
b.place(x=270,y=380)
frame.mainloop()



