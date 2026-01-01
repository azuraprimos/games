import turtle
t=turtle.Turtle()
t.hideturtle()
t.speed(0)

t2=turtle.Turtle()
t2.hideturtle()
t2.pensize(4)
t2.speed(0)
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("pink")
turn="X"
winner=""
name_player1 = turtle.textinput("Player 1", "Please enter your name:")
name_player2=turtle.textinput("player 2","please enter second player name: ")
game_end=False
# def get_cord(x,y):
#     print({x},
def grid():
    t2.pensize(4)
    for x in [-100, 100]:
      t2.penup()
      t2.goto(x, 300)
      t2.setheading(270) 
      t2.pendown()
      t2.forward(600)
for y in [-100, 100]:
    t2.penup()
    t2.goto(-300, y)
    t2.setheading(0) 
    t2.pendown()
    t2.forward(600)

board = [
  ["", "", ""],
  ["", "", ""],  
  ["", "", ""] 
]
turn="X"

grid()
def turnswitch():
    global turn
    if turn == "X":
      turn = "O"
      t.write(name_player1+"'s turn",align="center",font=("Arial",int(12)))
    elif turn=="O":
         turn="X"
         t.write(name_player2+"'s turn",align="center",font=("Arial",int(12)))

    else:
        return None
def draw_symbol(x, y):
    global turn
    t.penup()
    t.goto(x, y -50)  
    t.setheading(0)
    t.pendown()
    t.pensize(5)
    t.write(turn, align="center",font=("Arial",int(100),"bold")) 



def boxes(x, y):
    global board
    

    if y > 100:
        rows = 0
    elif y > -100:
        rows = 1
    else:
        rows = 2

    if x< -100:
        cols = 0
    elif x < 100:
        cols = 1
    else:
        cols = 2

    return rows, cols
game_end=False
def check_for_win():
    global winner,game_end
    #can write this family reunion of if-else by using for loops.
        
    if board[0][0]==board[0][1]==board[0][2]!="":
        winner=board[0][1]
        game_end=True
        return None
    elif board[0][0]==board[1][0]==board[2][0]!="":
        winner=board[0][1]
        game_end=True
        return None
    elif board[0][1]==board[1][1]==board[2][1]!="":
        winner=board[0][1]
        game_end=True
        return None
    elif board[1][0]==board[1][1]==board[1][2]!="":
        winner=board[1][0]
        game_end=True
        return None
    elif board[2][0]==board[2][1]==board[2][2]!="":
        winner=board[2][0]
        game_end=True
        return None
    elif board[0][2]==board[1][2]==board[2][2]!="":
        winner=board[0][2]
        game_end=True
        return None
    elif board[0][0]==board[1][1]==board[2][2]!="":
        winner=turn
        game_end=True
        return None
    elif board[0][2]==board[1][1]==board[2][0]!="":
        winner=board[0][2]
        game_end=True
        return None
     
    else:
        return None
        game_end = True

def display_winner():
     t.write(f"{winner} is the winner",align="center",font=("ariel",int(20)))

def user_inputs(x,y):
    global board,game_end,turn

    row,columns = boxes(x, y)  #


    if row is None or columns is None:
        return None

    if board[row][columns] != "":
        return None

    board[row][columns] = turn
    if row == 0:
        y2 = 200
    elif row == 1:
        y2= 0
    elif row == 2:
        y2 = -200

    if columns == 0:
        x2 = -200
    elif columns == 1:
        x2 = 0
    elif columns == 2:
        x2 = 200

    draw_symbol(x2,y2)
    check_for_win()
    if game_end:
        display_winner()
    else:
        turnswitch()
screen.onscreenclick(user_inputs)


turtle.done()
