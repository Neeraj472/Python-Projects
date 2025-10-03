#                           Tic-Tac-Toe Game
import tkinter as tk
from tkinter import messagebox
r =tk.Tk()
r.title("Tic tac toe Game")
r.geometry("320x320")

board =[" " for i in range(9)]
current_player ="X"
buttons =[]
def check_winner(player):
    win_conditon=[[0,1,2],[3,4,5],[6,7,8], #row
                    [0,3,6],[1,4,7],[2,5,8], #col
                    [0,4,8],[2,4,6]  #diagonal
                    ]
    for i in win_conditon:
        if board[i[0]]==board[i[1]]==board[i[2]]==player:
            return True
    return False
    
def click(index):
    global current_player
    if board[index]==" ":
        board[index]=current_player
        buttons[index].config(text=current_player,state="disable")
        if check_winner(current_player):
            messagebox.showinfo(title="Congratulations",message=f"player {current_player} wins")
            reset()
            return
        elif " " not in board:
            messagebox.showinfo(title="Draw",message="Its a draw")
            reset()
            return
        current_player="O" if current_player=="X" else "X"
    
def reset():
    global board ,current_player
    board =[" " for i in range(9)]
    for n in buttons:
        n.config(text=" ",state ="normal")

for i in range(9):
    btn =tk.Button(r,text=" ",font=("Arial",25),width=5,height=2,bg="black",command=lambda i=i :click(i))
    btn.grid(row=i//3,column=i%3)
    buttons.append(btn)


r.mainloop()