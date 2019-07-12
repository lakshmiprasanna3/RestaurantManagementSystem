from tkinter import *


root1 = Tk()
root1.geometry("720x420+0+0")
root1.title("Login Page")

name_inp = StringVar()
password_inp = StringVar()

def enter():
    if name_inp.get() == "prasanna" and password_inp.get() == "1234":
        root1.destroy()
        import question
    else:
        tkinter.messagebox.showinfo('Error', 'Authentication Failed')
        name_inp.set("")
        password_inp.set("")


def destroy():
    root1.destroy()


label0 = Label(root1, font=('aria',24, 'bold'), text="Welcome to your restaurant portal", fg="Purple", bd=10, anchor='w')
label0.grid(row=1,column=1)

label = Label(root1, font=('aria', 18, 'bold'), text="Login in to continue....", fg="brown", bd=10, anchor='w')
label.grid(row=2,column=1)

label1 = Label(root1, font=('aria', 15, 'bold'),text="Username :",fg="black")
label2 = Label(root1, font=('aria', 15, 'bold'), text="Pin :",fg="black")

entry1 = Entry(root1,width=25,bd=5, textvariable=name_inp)
entry2 = Entry(root1,width=25,bd=5, textvariable=password_inp)

label1.grid(row=3,sticky=E)
label2.grid(row=4,sticky=E)
entry1.grid(row=3,column=1)
entry2.grid(row=4,column=1)

enter_btn = Button(root1,font=('aria', 15, 'bold'), bg="sky blue",fg="white",text="Enter", command=enter)
enter_btn.grid(row=6, column=1)

exit_btn = Button(root1, padx=1,font=('aria', 15,'bold'), bg="sky blue",fg="white",text="Exit", command=destroy)
exit_btn.grid(row=7, column=1)



root1.mainloop()
