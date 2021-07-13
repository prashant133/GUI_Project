from tkinter import *

root = Tk()

#definding the geometry of the root
root.geometry("361x381+500+200")

#setting the icon for the project
root.iconbitmap('cal.ico')

#defining the title of project.
root.title("Calculator")
val=""
data=StringVar()


#definding the function

def buttonClick(number):
    global val
    val=val+str(number)
    data.set(val)

def buttonClear():
    global val
    val=""
    data.set("")

def buttonEqual():
    global  val
    result=str(eval(val))
    data.set(result)


#defining the GUI
display = Entry(root,textvariable=data,bd=29,justify="right",bg="powderblue",font=("arial",20))
display.grid(row=0,columnspan=4)
button_7 = Button(root,text="7",font =("Ariel",12,"bold"),bg="grey",bd=12,height=2,width=6,command=lambda:buttonClick(7))
button_7.grid(row=1,column=0)
button_8 = Button(root,text="8",font =("Ariel",12,"bold"),bg="grey",bd=12,height=2,width=6,command=lambda:buttonClick(8))
button_8.grid(row=1,column=1)
button_9 = Button(root,text="9",font =("Ariel",12,"bold"),bg="grey",bd=12,height=2,width=6,command=lambda:buttonClick(9))
button_9.grid(row =1,column=2)
button_add = Button(root,text="+",font =("Ariel",12,"bold"),bg="orange",bd=12,height=2,width=6,command=lambda:buttonClick('+'))
button_add.grid(row=1,column=3)


button_4 = Button(root,text="4",font =("Ariel",12,"bold"),bg="grey",bd=12,height=2,width=6,command=lambda:buttonClick(4))
button_4.grid(row=2,column=0)
button_5 = Button(root,text="5",font =("Ariel",12,"bold"),bg="grey",bd=12,height=2,width=6,command=lambda:buttonClick(5))
button_5.grid(row=2,column=1)
button_6 = Button(root,text="6",font =("Ariel",12,"bold"),bg="grey",bd=12,height=2,width=6,command=lambda:buttonClick(6))
button_6.grid(row =2,column=2)
button_sub = Button(root,text="-",font =("Ariel",12,"bold"),bg="orange",bd=12,height=2,width=6,command=lambda:buttonClick('-'))
button_sub.grid(row=2,column=3)


button_1 = Button(root,text="1",font =("Ariel",12,"bold"),bg="grey",bd=12,height=2,width=6,command=lambda:buttonClick(1))
button_1.grid(row=3,column=0)
button_2 = Button(root,text="2",font =("Ariel",12,"bold"),bg="grey",bd=12,height=2,width=6,command=lambda:buttonClick(2))
button_2.grid(row=3,column=1)
button_3 = Button(root,text="3",font =("Ariel",12,"bold"),bg="grey",bd=12,height=2,width=6,command=lambda:buttonClick(3))
button_3.grid(row =3,column=2)
button_mul = Button(root,text="x",font =("Ariel",12,"bold"),bg="orange",bd=12,height=2,width=6,command=lambda:buttonClick('*'))
button_mul.grid(row=3,column=3)


button_c = Button(root,text="C",font =("Ariel",12,"bold"),bg="orange",bd=12,height=2,width=6,command=buttonClear)
button_c.grid(row=4,column=0)
button_0 = Button(root,text="0",font =("Ariel",12,"bold"),bg="grey",bd=12,height=2,width=6,command=lambda:buttonClick(0))
button_0.grid(row=4,column=1)
button_div = Button(root,text="÷",font =("Ariel",12,"bold"),bg="orange",bd=12,height=2,width=6,command=lambda:buttonClick('/'))
button_div.grid(row =4,column=2)
button_equal = Button(root,text="=",font =("Ariel",12,"bold"),bg="orange",bd=12,height=2,width=6,command=buttonEqual)
button_equal.grid(row=4,column=3)

root.mainloop()