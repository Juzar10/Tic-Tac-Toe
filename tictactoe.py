from tkinter import*
root=Tk()
root.title("tic tac toe game")

#creating empty nested list for keeping track of player position
position=[[0,0,0],
          [0,0,0],
          [0,0,0]]

#creating empty nested list to create buttons
button=[[0,0,0],
        [0,0,0],
        [0,0,0]]


#callback is function to tell buttons what to do
def callback(a,b):
    global player

#checks if you are not pressing same button twice
    if position[a][b]!=0:
        return

#code for what to do when you press the button
    if player=='X'and position[a][b]==0 and game_state==False:
        position[a][b]='X'
        button[a][b].config(text='X',fg="Black")

    if player=='O'and position[a][b]==0 and game_state==False:
        position[a][b]='O'
        button[a][b].config(text='O',fg="snow")

#flips player after every time button is pressed

    flip_player()

#checks for winner after every time button is pressed
    check_for_winner()


#after every time you click button check_for_winner determine if we have winner or not
def check_for_winner():
    global game_state
    for i in range(3):
        if position[0][i]==position[1][i]==position[2][i]!=0:
            button[0][i].config(bg='khaki4')
            button[1][i].config(bg='khaki4')
            button[2][i].config(bg='khaki4')
            game_state=True
            return

    for i in range(3):
        if position[i][0]==position[i][1]==position[i][2]!=0:
            button[i][0].config(bg='khaki4')
            button[i][1].config(bg='khaki4')
            button[i][2].config(bg='khaki4')
            game_state=True
            return

    if position[0][0]==position[1][1]==position[2][2]!=0:
        button[0][0].config(bg='khaki4')
        button[1][1].config(bg='khaki4')
        button[2][2].config(bg='khaki4')
        game_state=True
        return

    if position[0][2]==position[1][1]==position[2][0]!=0:
        button[0][2].config(bg='khaki4')
        button[1][1].config(bg='khaki4')
        button[2][0].config(bg='khaki4')
        game_state=True
        return

#after every turn this function flips the player
def flip_player():
    global player
    if player=='X':
        player='O'
        return
    if player=='O':
        player='X'
        return

#creating buttons with help of loops as we have to call this buttons again so it is easy this way
for i in range(3):
    for j in range(3):
        button[i][j]=Button(font=("Arial",60),width=2,height=1,bg='LightGoldenrod',command=lambda a=i,b=j:callback(a,b))
        button[i][j].grid(row=i,column=j)

#intializing 1st player to be X
player='X'

#intializing game_state to be in False mode
game_state=False

#mainloop to keep program running forever(until you click cross on top)
root.mainloop()