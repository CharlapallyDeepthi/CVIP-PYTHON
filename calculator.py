from tkinter import*
# creating a window
window=Tk()
# adding title to window
window.title('Calculator')
#global variables
number=0
operator=''
def clear():
    entry.delete(0,END)

def click(number):
    n1=entry.get()
    clear()
    n2=n1+number
    entry.insert(0,n2)

def calculate(op):
    global number,operator
    operator=op
    number=entry.get()
    operator = op
    clear()

def equal():
    global number,operator
    result=''
    number2=entry.get()
    clear()
    if operator=='+':
        result=int(number)+int(number2)
    elif operator=='-':
        result=int(number)-int(number2)
    elif operator=='*':
        result=int(number)*int(number2)  
    elif operator=='/':
        result=int(number)/int(number2)     
    elif operator=='%':
        result=int(number)%int(number2) 
    entry.insert(0,result)
    
#creating widgets
entry=Entry(window,width=15,justify=RIGHT)
but0=Button(window,text='0',padx=30,pady=10,command=lambda:click('0'))
but1=Button(window,text='1',padx=30,pady=10,command=lambda:click('1'))
but2=Button(window,text='2',padx=30,pady=10,command=lambda:click('2'))
but3=Button(window,text='3',padx=30,pady=10,command=lambda:click('3'))
but4=Button(window,text='4',padx=30,pady=10,command=lambda:click('4'))
but5=Button(window,text='5',padx=30,pady=10,command=lambda:click('5'))
but6=Button(window,text='6',padx=30,pady=10,command=lambda:click('6'))
but7=Button(window,text='7',padx=30,pady=10,command=lambda:click('7'))
but8=Button(window,text='8',padx=30,pady=10,command=lambda:click('8'))
but9=Button(window,text='9',padx=30,pady=10,command=lambda:click('9'))
add=Button(window,text='+',padx=30,pady=10,command=lambda:calculate('+'))
sub=Button(window,text='-',padx=32,pady=10,command=lambda:calculate('-'))
mul=Button(window,text='*',padx=32,pady=10,command=lambda:calculate('*'))
div=Button(window,text='/',padx=32,pady=10,command=lambda:calculate('/'))
mod=Button(window,text='%',padx=27,pady=10,command=lambda:calculate('%'))
clr=Button(window,text='CLR',padx=30,pady=10,command=clear)
equ=Button(window,text='=',padx=75,pady=10,command=equal)
#adding rows of calculator
#row0
entry.grid(row=0,column=0,columnspan=5,padx=1,pady=1)
#row1
but7.grid(row=1,column=0,padx=1,pady=1)
but8.grid(row=1,column=1,padx=1,pady=1)
but9.grid(row=1,column=2,padx=1,pady=1)
#row2
but4.grid(row=2,column=0,padx=1,pady=1)
but5.grid(row=2,column=1,padx=1,pady=1)
but6.grid(row=2,column=2,padx=1,pady=1)
#row3
but1.grid(row=3,column=0,padx=1,pady=1)
but2.grid(row=3,column=1,padx=1,pady=1)
but3.grid(row=3,column=2,padx=1,pady=1)
#row4
add.grid(row=4,column=0,padx=1,pady=1)
but0.grid(row=4,column=1,padx=1,pady=1)
sub.grid(row=4,column=2,padx=1,pady=1)
#row5
mul.grid(row=5,column=0,padx=1,pady=1)
div.grid(row=5,column=1,padx=1,pady=1)
mod.grid(row=5,column=2,padx=1,pady=1)
#row6
clr.grid(row=6,column=0,padx=1,pady=1)
equ.grid(row=6,column=1,columnspan=2,padx=1,pady=1)
window.mainloop()
