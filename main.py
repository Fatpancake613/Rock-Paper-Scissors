from tkinter import * #This is visual so using tkinter
from tkinter import messagebox #show if you won or lost
from random import choice #Pick AI's RPS choice 
root = Tk()
root.title("Rock Paper Scissors")
rps = choice(["rock","paper","scissors"])
win = False

def r(): #rock
    if rps == "scissors": #rock beats scissors
        win = True
   
        messagebox.showinfo("Winner!", "Congradulations! You won! The CPU's guess was " + rps + ".") #winning screen
        exit()
    else:
        messagebox.showerror("You lost!", "Aww, looks like you lost. the CPU's guess was " + rps + ". Better luck next time.") #losing screen
        exit()
def p(): #paper
    if rps == "rock": #paper beats rock
        win = True
     
        messagebox.showinfo("Winner!", "Congradulations! You won! The CPU's guess was " + rps + ".") #winning screen
        exit()
    else: 
        messagebox.showerror("You lost!", "Aww, looks like you lost. the CPU's guess was " + rps + ". Better luck next time.") #losing screen
        exit()
def s(): #scissors
    if rps == "paper": #scissors beats paper
        win = True
       
        messagebox.showinfo("Winner!", "Congradulations! You won! The CPU's guess was " + rps + ".") #winning screen
        exit()
    else:
        messagebox.showerror("You lost!", "Aww, looks like you lost. the CPU's guess was " + rps + ". Better luck next time.") #losing screen
        exit()

welcome = Label(root, text="Welcome to rock paper scissors.") #welcome label
welcome.pack()
Rock = Button(root, text="Rock", padx=100, command=r) #buttons
Rock.pack()
Paper = Button(root, text="Paper", padx=100, command=p)
Paper.pack()
Scissors = Button(root, text="Scissors", padx=100, command=s)
Scissors.pack()



root.mainloop()
