from tkinter import*
newroot = Tk()
newroot.geometry("400x170+0+0")
newroot.title("Menu")

def enter1():
	newroot.destroy()
	import restaurant_management_system

def enter2():
	newroot.destroy()
	import check_item_pricelist

label11 = Label(newroot,font = ('aria',15,'bold'), text=" Bill",fg="black")
label11.grid(row=1, sticky=E)

press_btn = Button(newroot, text="Press Here", bg="pink",width=15,height=2,command= enter1)
press_btn.grid(row=1, column=1)

label12 = Label(newroot,font = ('aria',15,'bold'), text="Menu & Price List",fg="brown")
label12.grid(row=2, sticky=E)

press_btn2 = Button(newroot, text="Press Here", bg="pink",width=15,height=2,command= enter2)
press_btn2.grid(row=2, column=1)

newroot.mainloop()
