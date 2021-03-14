from tkinter import * 
from tkinter import messagebox
from time import sleep as sp
from random import choice #Pick AI's RPS choice 
root = Tk()
root.iconphoto("icon.")
root.title("Rock Paper Scissors")
rps = choice(["rock","paper","scissors"])
win = False
#title(root, "RPS")
def r():
    if rps == "scissors":
        win = True
        #print("Yay you won and the CPU outputted " + rps)
        messagebox.showinfo("Winner!", "Congradulations! You won! The CPU's guess was " + rps + ".")
        exit()
    else:
        messagebox.showerror("You lost!", "Aww, looks like you lost. the CPU's guess was " + rps + ". Better luck next time.")
        exit()
def p():
    if rps == "rock":
        win = True
        #print("Yay you won and the CPU outputted " + rps)
        messagebox.showinfo("Winner!", "Congradulations! You won! The CPU's guess was " + rps + ".")
        exit()
    else:
        messagebox.showerror("You lost!", "Aww, looks like you lost. the CPU's guess was " + rps + ". Better luck next time.")
        exit()
def s():
    if rps == "paper":
        win = True
        #print("Yay you won and the CPU outputted " + rps)
        messagebox.showinfo("Winner!", "Congradulations! You won! The CPU's guess was " + rps + ".")
        exit()
    else:
        messagebox.showerror("You lost!", "Aww, looks like you lost. the CPU's guess was " + rps + ". Better luck next time.")
        exit()

welcome = Label(root, text="Welcome to rock paper scissors.\nThe computer has already chosen so you can choose right now.")
welcome.pack()
Rock = Button(root, text="Rock", padx=100, command=r)
Rock.pack()
Paper = Button(root, text="Paper", padx=100, command=p)
Paper.pack()
Scissors = Button(root, text="Scissors", padx=100, command=s)
Scissors.pack()



root.mainloop()
