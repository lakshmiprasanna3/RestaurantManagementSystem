from tkinter import*

roo = Tk()
roo.geometry("500x320+0+0")
roo.title("Item_Price List")


lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
lblinfo.grid(row=0, column=0)
lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
lblinfo.grid(row=0, column=2)
lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
lblinfo.grid(row=0, column=3)
lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fried Rice", fg="green", anchor=W)
lblinfo.grid(row=1, column=0)
lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rs.150", fg="blue", anchor=W)
lblinfo.grid(row=1, column=3)
lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Idli", fg="green", anchor=W)
lblinfo.grid(row=2, column=0)
lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rs.40", fg="blue", anchor=W)
lblinfo.grid(row=2, column=3)
lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Masala Dosa", fg="green", anchor=W)
lblinfo.grid(row=3, column=0)
lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rs.60", fg="blue", anchor=W)
lblinfo.grid(row=3, column=3)
lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Biryani", fg="green", anchor=W)
lblinfo.grid(row=4, column=0)
lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rs.175", fg="blue", anchor=W)
lblinfo.grid(row=4, column=3)
lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger", fg="green", anchor=W)
lblinfo.grid(row=5, column=0)
lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rs.60", fg="blue", anchor=W)
lblinfo.grid(row=5, column=3)
lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="green", anchor=W)
lblinfo.grid(row=6, column=0)
lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rs.35", fg="blue", anchor=W)
lblinfo.grid(row=6, column=3)

roo.mainloop()



