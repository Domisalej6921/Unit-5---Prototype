from tkinter import *

#Main Window
root = Tk()

#Definning the click function
def click():
    Label1 = Label(root, text="Checking your information in our database now!")
    Label1.grid(row=6, column=2)
    search = open("customerdetails.txt", "r")
    data = search.readlines()
    for line in data:
        if fullName.get() in line:
            Label2 = Label(root, text = "Hello " + fullName.get())
            Label2.grid(row=4, column=2)

#Title
myTitle = Label(root, text="Happy Hols", font=16)
myTitle.grid(row=0, column=2)

#Opening Paragraph
myLabel = Label(root, text="Welcome to Happy Hols.")
myLabel.grid(row=1, column=1)

#First Input Field
fullName = Entry(root, borderwidth=5, width=50)
fullName.grid(row=2, column=2)
fullName.insert(0, "Enter your full name: ")

#Submit Button
subbutton = Button(root, text="Submit!", command=click)
subbutton.grid(row=3, column=2)

#Creating window mainloop
root.mainloop()