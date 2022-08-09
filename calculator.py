import tkinter
from tkinter import *

expression = ""
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:

		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""

	except:

		equation.set(" ERROR ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")



if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="SteelBlue3")
	gui.title("SIMPLE CALCULATOR")
	gui.geometry("395x395+500+200")
	equation = StringVar()
	Display  = Entry(gui,bd=30,bg="SteelBlue3", textvariable=equation,font =('ariel',20,"bold"),justify ="right")
	Display.grid(columnspan=5, row=0)

	buttonsq = Button(gui,font=("bold") , text=' x² ',bg='steelblue',command=lambda: press("**2"), height=1, width=6,bd=11)
	buttonsq.grid(row=2, column=2)
	AC = Button(gui,font=("bold") ,text='AC',bg='pink',command=clear, height=1, width=6,bd=11)
	AC.grid(row=2, column=3)

	button1 = Button(gui,font=("bold") , text=' 1 ',bg='light skyblue',command=lambda: press(1), height=1, width=6,bd=11)
	button1.grid(row=3, column=0)
	button2 = Button(gui,font=("bold") , text=' 2 ',bg='light skyblue',command=lambda: press(2), height=1, width=6,bd=11)
	button2.grid(row=3, column=1)
	button3 = Button(gui,font=("bold") , text=' 3 ',bg='light skyblue',command=lambda: press(3), height=1, width=6,bd=11)
	button3.grid(row=3, column=2)
	plus    = Button(gui,font=("bold") , text='+',bg='light skyblue',command=lambda: press("+"), height=1, width=6,bd=11)
	plus.grid(row=6, column=2)

	button4  = Button(gui,font=("bold") ,text=' 4 ',bg='light skyblue',command=lambda: press(4), height=1, width=6,bd=11)
	button4.grid(row=4, column=0)
	button5  = Button(gui,font=("bold") ,text=' 5 ',bg='light skyblue',command=lambda: press(5), height=1, width=6,bd=11)
	button5.grid(row=4, column=1)
	button6  = Button(gui,font=("bold") ,text=' 6 ',bg='light skyblue',command=lambda: press(6), height=1, width=6,bd=11)
	button6.grid(row=4, column=2)
	minus    = Button(gui,font=("bold") ,text=' - ',bg='light skyblue',command=lambda: press("-"), height=1, width=6,bd=11)
	minus.grid(row=4, column=3)

	button7  = Button(gui,font=("bold") , text=' 7 ',bg='light skyblue',command=lambda: press(7), height=1, width=6,bd=11)
	button7.grid(row=5, column=0)
	button8  = Button(gui,font=("bold") , text=' 8 ',bg='light skyblue',command=lambda: press(8), height=1, width=6,bd=11)
	button8.grid(row=5, column=1)
	button9  = Button(gui,font=("bold") , text=' 9 ',bg='light skyblue',command=lambda: press(9), height=1, width=6,bd=11)
	button9.grid(row=5, column=2)
	multiply = Button(gui,font=("bold") , text=' x ',bg='light skyblue',command=lambda: press("*"), height=1, width=6,bd=11)
	multiply.grid(row=5, column=3)


	Decimal = Button(gui,font=("bold") , text='.', bg='light skyblue',command=lambda: press('.'), height=1, width=6,bd=11)
	Decimal.grid(row=6, column=0)
	button0 = Button(gui,font=("bold") , text=' 0 ', bg='light skyblue',command=lambda: press(0), height=1, width=6,bd=11)
	button0.grid(row=6, column=1)
	equal   = Button(gui, font=("bold") ,text=' = ', bg='LemonChiffon2', command=equalpress, height=1, width=6, bd=11)
	equal.grid(row=3, column=3)
	divide  = Button(gui,font=("bold") , text=' ÷ ', bg='light skyblue',command=lambda: press("/"),height=1,width=6,bd=11)
	divide.grid(row=6, column=3)


	gui.mainloop()
