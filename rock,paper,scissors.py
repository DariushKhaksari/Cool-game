from random import *
print(""" 
Welcome to my game, Be careful maybe this is the last time you are alive... \U0001f923 \U0001f923 \U0001f923 \U0001f923 
they are your moves: 
Rock \U0001F60E
Paper \U0001F60E
Scissors \U0001F60E
For quit type Exit. 
---------------""")
move= ["Rock", "Paper", "Scissors"]
computer = move[randint(0,2)]
player = True
while player == True:
    
    player = input("enter your moves: ")
    if player=="Exit":
        break
    if player == computer:
        print("thats a tie")
    elif player == "Rock":
        if computer == "Paper":
            print("computer win")
        else:
            print("You win")
    elif player == "Paper":
        if computer == "Scissors":
            print("computer win")
        else:
            print("You win")
    elif player == "Scissors":
        if computer == "Rock":
            print("computer win")
        else:
            print("You win")
    else:
        print("wrong spell")
    player = True
    computer =move[randint(0,2)]