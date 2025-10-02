#                   Hangman game (you can also use images)
import tkinter as tk
from tkinter import messagebox
import random as rd
r =tk.Tk()
r.title('Hangman game')
r.geometry("400x500")
r.config(bg="black")
word=""
guessed=""
attempts =6
buttons=[]
score=0

stages = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]
f =tk.Frame(r,bg="black")

def start():
    global word,guessed,attempts,buttons,score
    words=["python", "computer", "hangman", "science", "programming", "college"]
    word =rd.choice(words)
    rdm =rd.choice(words)
    button_choice =word+rdm
    suffle_buttons=[]
    for i in button_choice:
        suffle_buttons.append(i)
    rd.shuffle(suffle_buttons)
    guessed ="_"*len(word)
    attempts =6
    guessed_label.config(text=guessed)
    attempt_label.config(text=f"Attempts left :{attempts}")
    result_label.config(text="")
    score_label.config(text=f"Score : {score}")

    stage_label.config(text=stages[0],fg="white")
    for b in buttons:
        b.destroy()
    buttons.clear()
    row,col =0,0
    for j in range(len(suffle_buttons)):
        bn =tk.Button(f,text=suffle_buttons[j],width=5,height=2,command=lambda x=suffle_buttons[j]:value(x))
        bn.grid(row=row,column=col,padx=2,pady=2)
        buttons.append(bn)
        col+=1
        if col==7:
            col=0
            row+=1
    start_button.config(text="Restart",command=start)

def value(n):
    check(n)
def check(n):
    global word,guessed,attempts,score
    guess =n                

    if len(guess)!=1 and not guess.isalpha():
        result_label.config(text="Please enter a single alphbet letter",fg="red")
        return
    
    if guess in word:
        new_guess =""
        for i in range(len(word)):
            if word[i]==guess:
                new_guess+=guess
            else:
                new_guess+=guessed[i]
        guessed =new_guess
        guessed_label.config(text=guessed)
        result_label.config(text="correct",fg="green")
        
    else:
        attempts-=1
        attempt_label.config(text=f"attempts left : {attempts}")
        result_label.config(text="Wrong",fg="red")
        stage_label.config(text=stages[6-attempts])

    if "_" not in guessed:
        result_label.config(text="you win",fg="#E8B938")
        score+=1
        score_label.config(text=f"Score: {score}")
        messagebox.showinfo(title="Congratulation",message="You Win")
        start()
        return
    elif attempts==0:
        result_label.config(text=f"game over, the word is {word}")
        stage_label.config(text=stages[6],fg="red") 
        messagebox.showinfo(title="Game Over",message="You loose")
        start()                     

game_name =tk.Label(r,text="Hangman game",font=("Arial",20),bg="black",fg="#940808")
game_name.grid(row=0, column=0, columnspan=4, pady=10)

guessed_label =tk.Label(r,text="",font=("Arial",15),bg="black",fg="#328EB3")
guessed_label.grid(row=1, column=0, columnspan=4, pady=10)

attempt_label =tk.Label(r,text=" ",font=("Arial",10),bg="black",fg="#32B395")
attempt_label.grid(row=2, column=0, columnspan=2, pady=5)

stage_label=tk.Label(r,text="",bg="black",fg="white")
stage_label.grid(row=4, column=0, columnspan=4, pady=10)

score_label=tk.Label(r,text=" ",font=("Arial",10),bg="black",fg="#32B395")
score_label.grid(row=3,column=0,columnspan=2)

result_label =tk.Label(r,text="",font=("Arial",15),bg="black",fg="white")
result_label.grid(row=7, column=0, columnspan=4, pady=30)
start_button =tk.Button(r,text="start",font=("Arial",10),bg="green",fg="white",command=start)
start_button.grid(row=4, column=2, columnspan=2, pady=5)
f.grid(row=5, column=0, columnspan=4, pady=20)

r.mainloop()