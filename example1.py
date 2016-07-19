from Tkinter import *

#Defining the window variable
root = Tk()

l1 = Label(root, text="Search").grid(row=0, padx=5,pady=5)
e1 = Entry(root).grid(row=0,column=1)

l2 = Label(root, text="Search2").grid(row=1, pady=5)
e2 = Entry(root).grid(row=1,column=1)

checkbutton = Checkbutton(root, text="Emin misiniz?").grid(columnspan=2, sticky=W, pady=5)

#The main loop of the GUI program
root.lift()
root.mainloop()