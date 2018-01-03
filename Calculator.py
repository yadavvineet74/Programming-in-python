from tkinter import *
import parser
root = Tk()
root.title("Calculator")
i = 0
def get_variable(num):
    global i
    display.insert(i,num)
    i+=1
def clearall():
    display.delete(0,END)
def backsp():
    allstring = display.get()
    if len(allstring):
        newstring = allstring[0:-1]
        clearall()
        display.insert(0,newstring)
    else:
        display.insert(0,"Error")
def calculate():
    allstring = display.get()
    try:
        a = parser.expr(allstring).compile()
        result = eval(a)
        clearall()
        display.insert(0,result)
    except Exception:
        clearall()

#def get_operator(operator):
    #   global i
    #length = len(operator)
    #display.insert(i,operator)
    #i+=length
def factorial():
    allstring = display.get()
    num = int(allstring)
    fact =1
    counter = num
    while(counter > 1):
        fact = fact * counter
        counter-=1
    clearall()
    display.insert(0,fact)




display = Entry(root)
# Display Numeric Buttona
display.grid(row = 0 , columnspan = 13, sticky = W+E)

button1=Button(root,text = "1",command =  lambda :get_variable(1))
button1.grid(row=1,column=0)

button2 = Button(root,text = "2",command =  lambda :get_variable(2))
button2.grid(row=1,column=3)

button3 = Button(root,text = "3", command =  lambda :get_variable(3))
button3.grid(row=1,column=6)

button4 = Button(root,text = "4", command =  lambda :get_variable(4))
button4.grid(row=3,column=0)

button5 = Button(root,text = "5", command =  lambda :get_variable(5))
button5.grid(row=3,column=3)

button6 = Button(root,text = "6", command =  lambda :get_variable(6))
button6.grid(row=3,column=6)

button7 = Button(root,text = "7", command =  lambda :get_variable(7))
button7.grid(row=5,column=0)

button8 = Button(root,text = "8", command =  lambda :get_variable(8))
button8.grid(row=5,column=3)

button9 = Button(root,text = "9", command =  lambda :get_variable(9))
button9.grid(row=5,column=6)

button0 = Button(root,text = "0", command =  lambda :get_variable(0))
button0.grid(row=7,column=3)

# Display Additional Buttons
buttonac = Button(root,text = "AC",command = lambda : clearall())
buttonac.grid(row=7,column=0)
buttoneq = Button(root,text = "=",command = lambda : calculate())
buttoneq.grid(row=7,column=6)
buttonplus = Button(root,text = "+",command = lambda :get_variable("+"))
buttonplus.grid(row=1,column=8)
buttonmin = Button(root,text = "-",command = lambda :get_variable("-"))
buttonmin.grid(row=3,column=8)
buttonmul = Button(root,text = "*",command = lambda :get_variable("*"))
buttonmul.grid(row=5,column=8)
buttondiv = Button(root,text = "/",command = lambda :get_variable("/"))
buttondiv.grid(row=7,column=8)

#Display Some Functional Operations Buttons

buttonpi = Button(root,text = "pi",command = lambda :get_variable(3.14))
buttonpi.grid(row=1,column=10)

buttonbs = Button(root,text = "<-",command = lambda : backsp())
buttonbs.grid(row=1,column=12)

buttonmod = Button(root,text = "%",command = lambda :get_variable("%"))
buttonmod.grid(row=3,column=10)

buttonfac = Button(root,text = "x!",command = lambda : factorial())
buttonfac.grid(row=3,column=12)

buttonobr = Button(root,text = "(", command = lambda :get_variable("("))
buttonobr.grid(row=5,column=10)

buttoncbr = Button(root,text = ")", command = lambda :get_variable(")"))
buttoncbr.grid(row=5,column=12)

buttonexp = Button(root,text = "exp")
buttonexp.grid(row=7,column=10)

buttonsqr = Button(root,text = "**2",command = lambda :get_variable("**2"))
buttonsqr.grid(row=7,column=12)



root.mainloop()