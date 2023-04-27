from tkinter import *
root = Tk()
root.state("zoomed")
m = "Science Building"
x = "Room no. 106"
mylabel = Label(root, text=f"You are in {m},{x}", fg="Red")
mylabel.pack()
mylabel.place(x=720, y=50, anchor=S)
root.mainloop()
