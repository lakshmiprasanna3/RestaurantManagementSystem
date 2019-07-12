from tkinter import*
import tkinter.messagebox
import time
import random


#### creating window and its geometry ######

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")


#### creating Frame ######

top = Frame(root, width = 1600, height = 50, relief = SUNKEN)
top.pack(side = TOP)

left = Frame(root, width = 800, height = 700, relief = SUNKEN)
left.pack(side = LEFT)

right = Frame(root, width = 300,height = 700, relief = SUNKEN)
right.pack(side = RIGHT)


##### creating label of title and time ###

label_info = Label(top, font = ('arial',40,'bold'), text ="Restaurant Management System", fg = "Brown", bd = 10, anchor = 'w')
label_info.grid(row = 0, column = 0)

local_time = time.asctime(time.localtime(time.time()))

label_info = Label(top, font = ('arial',20,'bold'), text = "Date:  "+local_time, fg = "purple", bd = 10, anchor = 'w')
label_info.grid(row = 1, column = 0)



###########now on left frame  enter menu ####################################################################

rand = StringVar()
friedrice_inp = StringVar()
idli_inp = StringVar()
masaladosa_inp = StringVar()
biryani_inp = StringVar()
burger_inp = StringVar()
drinks_inp = StringVar()
cost_inp = StringVar()
services_inp = StringVar()
tax_inp = StringVar()
subtotal_inp = StringVar()
total_inp = StringVar()

def ref():
	
	f1 = open('value1.txt','r')
	line = f1.readlines()
	friedrice_p = float(line[0])
	idli_p = float(line[1])
	masaladosa_p = float(line[2])
	biryani_p = float(line[3])
	burger_p = float(line[4])
	drinks_p = float(line[5])

	f1.close()

	x = random.randint(23000,53000)
	random_ref = str(x)
	rand.set(random_ref)
	try:
		if friedrice_inp.get() == "":
			CoF = 0
		else:
			CoF = float(friedrice_inp.get())*friedrice_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		friedrice_inp.set("")
		
	try:	
		if idli_inp.get() == "":
			Coi = 0
		else:
			Coi = float(idli_inp.get())*idli_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		idli_inp.set("")
	
	try:
		if masaladosa_inp.get() == "":
			Comd = 0
		else:
			Comd= float(masaladosa_inp.get())*burger_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		masaladosa_inp.set("")

	try:
		if drinks_inp.get() == "":
			CoD = 0
		else:
			CoD = float(drinks_inp.get())*drinks_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		drinks_inp.set("")

	try:
		if burger_inp.get() == "":
			Cob = 0
		else:
			Cob = float(burger_inp.get())*burger_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		burger_inp.set("")

	try:
		if biryani_inp.get() == "":
			Cobi = 0
		else:
			Cobi = float(biryani_inp.get())*biryani_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		biryani_inp.set("")

	CostOfMeal = (CoF+Coi+Comd+CoD+Cob+Cobi)
	
	PayTax = (CostOfMeal)*0.18
	ServiceCharge = (CostOfMeal)*0.05 	
	totalTax = PayTax + ServiceCharge
	totalCost = (CostOfMeal + PayTax + ServiceCharge)

	services_inp.set(str('%.2f' % (ServiceCharge)))
	tax_inp.set(str('%.2f' % (PayTax)))
	subtotal_inp.set(str('%.2f' % (CostOfMeal)))
	total_inp.set(str('%.2f' % (totalCost)))
	cost_inp.set(str('%.2f' % (totalTax)))
	 		
def bck():
	root.destroy()
	import question
def qexit():
	root.destroy()

def reset():
	rand.set("")
	friedrice_inp.set("")
	idli_inp.set("")
	masaladosa_inp.set("")
	biryani_inp.set("")
	burger_inp.set("")
	drinks_inp.set("")
	cost_inp.set("")
	services_inp.set("")
	tax_inp.set("")
	subtotal_inp.set("")
	total_inp.set("")


customer_number = Label(left, font=('arial',16,'bold'),text = "Order Id", bd = 16, anchor = 'w')
customer_number.grid(row=0,column=0,sticky = E)
txt_customer = Entry(left,font=('arial',16,'bold'), textvariable=rand, bd=10, insertwidth =4,bg="yellow", justify ='right')
txt_customer.grid(row=0,column=1)

friedrice = Label(left, font=('arial',16,'bold'),text = "Friedrice", bd = 16, anchor = 'w' )
friedrice.grid(row=1,column=0,sticky = E)
txt_friedrice = Entry(left,font=('arial',16,'bold'), textvariable=friedrice_inp, bd=10, insertwidth =4,bg = "pink", justify ='right')
txt_friedrice.grid(row=1,column=1)

idli = Label(left, font=('arial',16,'bold'),text = "Idli", bd = 16, anchor = 'w' )
idli.grid(row=2,column=0,sticky = E)
txt_idli = Entry(left,font=('arial',16,'bold'), textvariable=idli_inp, bd=10, insertwidth =4,bg = "pink", justify ='right')
txt_idli.grid(row=2,column=1)


burger = Label(left, font=('arial',16,'bold'),text = "Burger", bd = 16, anchor = 'w' )
burger.grid(row=3,column=0,sticky = E)
txt_burger = Entry(left,font=('arial',16,'bold'), textvariable=burger_inp, bd=10, insertwidth =4,bg = "pink", justify ='right')
txt_burger.grid(row=3,column=1)

drinks = Label(left, font=('arial',16,'bold'),text = "Drinks", bd = 16, anchor = 'w' )
drinks.grid(row=4,column=0,sticky = E)
txt_drinks = Entry(left,font=('arial',16,'bold'), textvariable=drinks_inp, bd=10, insertwidth =4,bg = "pink", justify ='right')
txt_drinks.grid(row=4,column=1)

masaladosa = Label(left, font=('arial',16,'bold'),text = "Masala dosa", bd = 16, anchor = 'w' )
masaladosa.grid(row=5,column=0,sticky = E)
txt_masaladosa = Entry(left,font=('arial',16,'bold'), textvariable=masaladosa_inp, bd=10, insertwidth =4,bg = "pink", justify ='right')
txt_masaladosa.grid(row=5,column=1)

biryani = Label(left, font=('arial',16,'bold'),text = "Biryani", bd = 16, anchor = 'w' )
biryani.grid(row=0,column=2,sticky = E)
txt_biryani = Entry(left,font=('arial',16,'bold'), textvariable=biryani_inp, bd=10, insertwidth =4,bg = "pink", justify ='right')
txt_biryani.grid(row=0,column=3)

subtotal = Label(left, font=('arial',16,'bold'),text = "Cost of Meal", bd = 16, anchor = 'w' )
subtotal.grid(row=1,column=2,sticky = E)
txt_subtotal = Entry(left,font=('arial',16,'bold'), textvariable=subtotal_inp, bd=10, insertwidth =4,bg = "green", justify ='right')
txt_subtotal.grid(row=1,column=3)

services = Label(left, font=('arial',16,'bold'),text = "Service Charge", bd = 16, anchor = 'w' )
services.grid(row=2,column=2,sticky = E)
txt_services = Entry(left,font=('arial',16,'bold'), textvariable=services_inp, bd=10, insertwidth =4,bg = "green", justify ='right')
txt_services.grid(row=2,column=3)

tax = Label(left, font=('arial',16,'bold'),text = "GST", bd = 16, anchor = 'w' )
tax.grid(row=3,column=2,sticky = E)
txt_tax = Entry(left,font=('arial',16,'bold'), textvariable=tax_inp, bd=10, insertwidth =4,bg = "green", justify ='right')
txt_tax.grid(row=3,column=3)

cost = Label(left, font=('arial',16,'bold'),text = "Total Tax", bd = 16, anchor = 'w' )
cost.grid(row=4,column=2,sticky = E)
txt_cost = Entry(left,font=('arial',16,'bold'), textvariable=cost_inp, bd=10, insertwidth =4,bg = "green", justify ='right')
txt_cost.grid(row=4,column=3)

total = Label(left, font=('arial',16,'bold'),text = "Total Cost", bd = 16, anchor = 'w' )
total.grid(row=5,column=2,sticky = E)
txt_total = Entry(left,font=('arial',16,'bold'), textvariable=total_inp, bd=10, insertwidth =4,bg = "green", justify ='right')
txt_total.grid(row=5,column=3) 


### right Frame Button ####

btn_total = Button(left, padx= 16, pady= 8, bd= 16, fg= "white", font=('arial',16,'bold'), width=10, text= "Total", bg= "red",command = ref)
btn_total.grid(row=7, column= 1)

btn_reset = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Reset", bg= "violet",command = reset)
btn_reset.grid(row=7, column= 2)

btn_exit = Button(left, padx= 16, pady= 8, bd= 16, fg= "white", font=('arial',16,'bold'), width=10, text= "Exit", bg= "blue",command = qexit)
btn_exit.grid(row=7, column= 3)

#-------backbutton-------#

btn_bck = Button(right, padx= 16,pady=8, bd= 6, fg= "black", font=('arial',16,'bold'), width=6, text= "Back",bg= "cadet blue",command = bck)
btn_bck.grid(row=0, column= 0)

label_info = Label(right, font = ('aria',20,'bold'), text =" Thank you!  Visit Again! ", fg = "red", bd = 10, anchor = 'w')
label_info.grid(row = 2, column = 0)


root.mainloop()

