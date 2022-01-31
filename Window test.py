from tkinter import *


root= Tk() #creating the window widget

myLabel = Label(root, text="i am a packed label") #creating label widget 
myLabel.pack() #shoving label widget onto window widget
    

f = open("test.txt")
e = Entry(root, width=40, borderwidth=2)
e.pack()
e.insert(0, "enter email here")
f.write()


root.mainloop()
""" 
myLabel = Label(root, text="i am a grid label") #creating label widget 
myLabel3 = Label(root, text="i am a second grid label")
myLabel.grid(row=0, column=0) #placing label widget onto grid on the window widget
myLabel3.grid(row=1, column=1) """