
from tkinter import * 
import tkinter as tk
root = tk.Tk() 
root.geometry("230x120")
root.title('Form')
l1 = Label(root, text = "Email:") 
l2 = Label(root, text = "Password:") 
l1.grid(row = 1, column = 1, pady = 10,padx=15) 
l2.grid(row = 2, column = 1, pady = 4,padx=15) 
e1 = Entry(root) 
e2 = Entry(root) 
e1.grid(row = 1, column = 2, pady = 10) 
e2.grid(row = 2, column = 2, pady = 4) 
submit = Button(root,text="submit")
submit.grid(column=2,row=3,pady="3")
mainloop() 
