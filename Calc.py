from tkinter import *
w=Tk()
w.geometry('355x420')
w.resizable(False,False)
w.title('Calculator')
w.configure(bg='grey')
#
def when_button_clicked(thing):
    global expr
    expr=expr+str(thing)
    inp_txt.set(expr)
def button_AC():
    global expr
    expr=" "
    inp_txt.set(" ")
def button_equalto():
    global expr
    result=str(eval(expr))  #eval() evaluates directly
    inp_txt.set(result)
    expr=" "

expr=" "
inp_txt=StringVar()
#
e1=Entry(w,bg='grey',fg='white',font=('Algerian',50),textvariable=inp_txt) #textvariable gets the input in the entry widget directly
e1.grid(columnspan=50,row=0,column=0)
#
bAC=Button(w,text='AC',fg='black',font=('Algerian',20),padx=23,pady=20,command=button_AC)
bAC.grid(row=1,column=0)
#
bPM=Button(w,text='±',fg='black',font=('Algerian',25),padx=25,pady=18,command=lambda: when_button_clicked('*(-1)'))
bPM.grid(row=1,column=1)
#
bpercent=Button(w,text='％',fg='black',font=('Algerian',30),padx=21,pady=15,command=lambda: when_button_clicked('/100*'))
bpercent.grid(row=1,column=2)
#
b7=Button(w,text='7',fg='black',font=('Algerian',30),padx=25,pady=10,command=lambda: when_button_clicked(7))
b7.grid(row=2,column=0)
#
b8=Button(w,text='8',fg='black',font=('Algerian',30),padx=25,pady=10,command=lambda: when_button_clicked(8))
b8.grid(row=2,column=1)
#
b9=Button(w,text='9',fg='black',font=('Algerian',30),padx=25,pady=10,command=lambda: when_button_clicked(9))
b9.grid(row=2,column=2)
#
b4=Button(w,text='4',fg='black',font=('Algerian',30),padx=25,pady=10,command=lambda: when_button_clicked(4))
b4.grid(row=3,column=0)
#
b5=Button(w,text='5',fg='black',font=('Algerian',30),padx=25,pady=10,command=lambda: when_button_clicked(5))
b5.grid(row=3,column=1)
#
b6=Button(w,text='6',fg='black',font=('Algerian',30),padx=25,pady=10,command=lambda: when_button_clicked(6))
b6.grid(row=3,column=2)
#
b1=Button(w,text='1',fg='black',font=('Algerian',30),padx=25,pady=10,command=lambda: when_button_clicked(1))
b1.grid(row=4,column=0)
#
b2=Button(w,text='2',fg='black',font=('Algerian',30),padx=25,pady=10,command=lambda: when_button_clicked(2))
b2.grid(row=4,column=1)
#
b3=Button(w,text='3',fg='black',font=('Algerian',30),padx=25,pady=10,command=lambda: when_button_clicked(3))
b3.grid(row=4,column=2)
#
bd=Button(w,text='➗',fg='black',font=('Algerian',30),padx=25,pady=15,command=lambda: when_button_clicked('/')) #
bd.grid(row=1,column=4)
#
bm=Button(w,text='✖️',fg='black',font=('Algerian',30),padx=25,pady=15,command=lambda: when_button_clicked('*'))
bm.grid(row=2,column=4)
#
bs=Button(w,text='➕',fg='black',font=('Algerian',30),padx=25,pady=15,command=lambda: when_button_clicked('+'))
bs.grid(row=3,column=4)
#
ba=Button(w,text='➖',fg='black',font=('Algerian',30),padx=25,pady=15,command=lambda: when_button_clicked('-'))
ba.grid(row=4,column=4)
#
bsq=Button(w,text='xʸ',fg='black',font=('Algerian',30),padx=25,pady=10,command=lambda: when_button_clicked('**'))
bsq.grid(row=5,column=0)
#
b0=Button(w,text='0',fg='black',font=('Algerian',30),padx=20,pady=10,command=lambda: when_button_clicked(0))
b0.grid(row=5,column=1)
#
bpoint=Button(w,text='.',fg='black',font=('Algerian',30),padx=32,pady=10,command=lambda: when_button_clicked('.'))
bpoint.grid(row=5,column=2)
#
bequal=Button(w,text='=',fg='black',font=('Algerian',30),padx=32,pady=15,command=lambda: button_equalto())
bequal.grid(row=5,column=4)
w.mainloop()
