from tkinter import *

window=Tk()

var=StringVar()
var.set("Addition")#by default

#combobox widget
w=OptionMenu(window,var,"Addition","Subtraction","Multiplication","Division")
w.grid(row=2,column=4)

def calculation():
    if var.get()=="Addition":
        soln=float(var1.get())+float(var2.get())
    elif var.get()=="Subtraction":
        soln=float(var1.get())-float(var2.get())
    elif var.get()=="Multiplication":
        soln=float(var1.get())*float(var2.get())
    else:
        try:
            soln=float(var1.get())//float(var2.get())
        except:
            soln="invalid"
    t.delete("1.0",END)
    t.insert(END,soln)

#button widget
b=Button(window,text="Calculate",command=calculation)
b.grid(row=3,column=4)

#Entry widgets
var1=StringVar()
e1=Label(window,text="Number 1")
e1=Entry(window,textvariable=var1,width=7)
e1.grid(row=2,column=2)

var2=StringVar()
e2=Label(window,text="Number 2")
e2=Entry(window,textvariable=var2,width=7)
e2.grid(row=2,column=3)

#text widget
t=Text(window,height=5,width=14)
t.grid(row=3,column=2)

window.mainloop()
