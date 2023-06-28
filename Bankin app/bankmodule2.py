import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user ="root",
    password="12345",
    db="Bank"
)
from tkinter import *
from tkinter import messagebox
import webbrowser
frame = Tk()
frame.geometry("500x300")
frame.title("Bank App ")
l1=Label(frame,text="Bank App",font=('ALGERIAN',40),fg="green")
l2=Label(frame,text="Account no")
l3=Label(frame,text="Password")
t1=Entry(frame,width=20)
t2=Entry(frame,width=20)
def click():
    x=t1.get()
    a="select Total_Balance from customer where Acc_no='"+x+"'"
    obj=con.cursor()
    obj.execute(a)
    b=a
    y=int(t3.get())
    c=b-t
    Acc=t1.get()
    d="update customer set Total_Balance='"+c+"' where Acc_no='Acc'"
    obj=con.cursor()
    obj.execte(d)
    con.commit()
    messagebox.showinfo("Message","Update")
def withdrawl():
    frame2=Toplevel()
    frame2.geometry("500x400")
    frame2.title("Withdrawl")
    l4=Label(frame2,text="Enter money")
    t3=Entry(frame2,width=30)
    def click():
         x=t1.get()
         a="select Total_Balance from customer where Acc_no='"+x+"'"
         obj=con.cursor()
         obj.execute(a)
         b = obj.fetchall()
         for i in b:
             c=int(i[0])
         y=int(t3.get())
         d=c-y
         e=str(d)
         d="update customer set Total_Balance='"+e+"' where Acc_no='"+x+"'"
         obj=con.cursor()
         obj.execute(d)
         con.commit()
         messagebox.showinfo("Message","Update")
         
    b4=Button(frame2,text="CLICK TO WITHDRAW",command=click)
    l4.place(x=50,y=80)
    t3.place(x=50,y=130)
    b4.place(x=50,y=180)
    frame2.mainloop()
def deposit():
    frame3=Toplevel()
    frame3.geometry("500x400")
    frame3.title("deposit")
    l5=Label(frame3,text="Enter money")
    t4=Entry(frame3,width=30)
    def click():
         x=t1.get()
         a="select Total_Balance from customer where Acc_no='"+x+"'"
         obj=con.cursor()
         obj.execute(a)
         b = obj.fetchall()
         for i in b:
             c=int(i[0])
         y=int(t4.get())
         d=c+y
         e=str(d)
         d="update customer set Total_Balance='"+e+"' where Acc_no='"+x+"'"
         obj=con.cursor()
         obj.execute(d)
         con.commit()
         messagebox.showinfo("Message","Update")
         
    b5=Button(frame3,text="CLICK TO WITHDRAW",command=click)
    l5.place(x=50,y=80)
    t4.place(x=50,y=130)
    b5.place(x=50,y=180)
    frame3.mainloop()
def balance():
    frame4=Toplevel()
    frame4.geometry("500x400")
    frame4.title("Pin Verification")
    l6=Label(frame4,text="enter pin")
    t5=Entry(frame4,width=20)
    def v():
        x=t5.get()
        a=t1.get()
        y="select PIN from customer where Acc_no='"+a+"'"
        ob=con.cursor()
        ob.execute(y)
        z=ob.fetchall()
        for j in z:
             u=j[0]
        b="select Total_Balance from customer where Acc_no='"+a+"'"
        obj=con.cursor()
        obj.execute(b)
        c=obj.fetchall()
        for i in c:
            d=i[0]
        if(x==u):
            l7=Label(frame4,text="Your Balance")
            l8=Label(frame4,text=d)
            l7.place(x=100,y=180)
            l8.place(x=180,y=180)
        else:
            messagebox.showinfo("PIN VERIFICATION","INVALID")
    b5=Button(frame4,text="Login",command=v)
    l6.place(x=70,y=80)
    t5.place(x=130,y=80)
    b5.place(x=100,y=130)
    frame4.mainloop()
def show():
    webbrowser.open("http://www.hdfc.com")
def login():
    Acc=t1.get()
    Pass=t2.get()
    b="select Acc_no,Password from customer where Acc_no='"+Acc+"'"
    obj=con.cursor()
    obj.execute(b)
    row=obj.fetchall()
    for i in row:
        a=i[0]
        c=i[1]
    if(Pass==c):
        messagebox.showinfo("info","login")
        frame1=Toplevel()
        frame1.geometry("500x400")
        frame1.title("Bank options")
        l1=Label(frame1,text="OPTIONS",font=('ALGERIAN',40),fg="blue")
        b=Button(frame1,text="WITHDRAWL",font=('ALGERIAN',15),command=withdrawl)
        b1=Button(frame1,text="DEPOSIT",font=('ALGERIAN',15),command=deposit)
        b2=Button(frame1,text="BALANCE",font=('ALGERIAN',15),command=balance)
        b3=Button(frame1,text="CONNECT TO BANK",font=('ALGERIAN',15),command=show)
        l1.pack()
        b.place(x=100,y=80)
        b1.place(x=100,y=130)
        b2.place(x=100,y=180)
        b3.place(x=100,y=230)
        frame1.mainloop()
    else:
        messagebox.showinfo("info","failed")
b=Button(frame,text="Login",command=login)
l1.pack()
l2.place(x=100,y=80)
t1.place(x=250,y=80)
l3.place(x=100,y=150)
t2.place(x=250,y=150)
b.place(x=200,y=200)
frame.mainloop()
