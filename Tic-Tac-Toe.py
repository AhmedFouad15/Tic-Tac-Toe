from tkinter import *

def nextturn(row, column):
    global player
    global score1
    global score2

    if buttons[row][column]['text'] == "" and checkwinner() is False:

        if player == players[0]:
            buttons[row][column]["text"] = player
            buttons[row][column].config(fg="Red")
            
            if checkwinner() is False:
                player = players[1]
                TurnLabel.config(text=(players[1] + " Turn"))

            elif checkwinner() is True:
                TurnLabel.config(text=("Congrats : " +players[0] + " won "))
                score1 +=1
                scorelabel.config(text="( " + players[0] + " Score is : " + str(score1) + " ) --- ( " + players[1] + " Score is : " + str(score2) + " )")


            elif checkwinner() == "Tie":
                TurnLabel.config(text="Tie")

        elif player == players[1]:
            buttons[row][column]["text"] = player
            buttons[row][column].config(fg="Green")
            
            if checkwinner() is False:
                player = players[0]
                TurnLabel.config(text=(players[0] + " Turn"))

            elif checkwinner() is True:
                TurnLabel.config(text=("Congrats : " +players[1] + " won "))
                score2 += 1
                scorelabel.config(text = "( " + players[0] + " Score is : " + str(score1) + " ) --- ( " + players[1] + " Score is : " + str(score2) + " )")

            elif checkwinner() == "Tie":
                TurnLabel.config(text="Tie") 

def checkwinner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="Light Green")
            buttons[row][1].config(bg="Light Green")
            buttons[row][2].config(bg="Light Green")
            return True
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="Light Green")
            buttons[1][column].config(bg="Light Green")
            buttons[2][column].config(bg="Light Green")
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
            buttons[0][0].config(bg="Light Green")
            buttons[1][1].config(bg="Light Green")
            buttons[2][2].config(bg="Light Green")
            return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
            buttons[0][2].config(bg="Light Green")
            buttons[1][1].config(bg="Light Green")
            buttons[2][0].config(bg="Light Green")
            return True
    elif emptyspace() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    else:
        return False

def emptyspace():
    space = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                space -=1
    if space == 0:
        return False
    else:
        return True

def newgame():
    global player

    if player == players[0]:
        player = players[1]
    else:
        player = players[0]

    TurnLabel.config(text = (player + " Turn"))

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg ="#F0F0F0")

def ResetScore():
    global score1, score2
    score1 = 0
    score2 = 0 
    scorelabel.config(text=("( " + players[0] + " Score is : " + str(score1) + " ) --- ( " + players[1] + " Score is : " + str(score2) + " )"))

window = Tk()
window.title("Tik-Tac-Toe")

score1,score2 = 0, 0
players = ["X", "O"]
player = players[0]
buttons=[[0,0,0,],
         [0,0,0,],
         [0,0,0,],]

TurnLabel = Label(window, text=(player + " Turn"), font=("Bold", 25), width=20)
TurnLabel.pack()

frameOfScore = Frame(window)
frameOfScore.pack()

scorelabel = Label(frameOfScore, text=("( " + players[0] + " Score is : " + str(score1) + " ) --- ( " + players[1] + " Score is : " + str(score2) + " )"))
scorelabel.grid(row=1,column=0)

resetbuttonscore = Button(frameOfScore, text= "Reset Score", font=("Arrial", 10), command=ResetScore)
resetbuttonscore.grid(row=1,column=1)

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column]= Button(frame, text="",font = ("Bold" , 50), width=3, height=1,
                                       command= lambda rows=row, columns=column: nextturn(rows, columns))
        buttons[row][column].grid(column= column, row= row)

resetGamebutton = Button(window, text= "Play Again", font=("Arrial", 10), command=newgame, width=35, bg = "#A020F0", fg="#F0F0F0")
resetGamebutton.pack()

window.mainloop()