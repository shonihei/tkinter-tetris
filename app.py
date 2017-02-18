from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()
