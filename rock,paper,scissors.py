from random import *
print(""" 
Welcome to my game, Be careful maybe this be the last time you are life... \U0001f923 \U0001f923 \U0001f923 \U0001f923 
they are your moves.
 Rock \U0001F60E
 Paper \U0001F60E
 Scissor \U0001F60E
 ---------------""")

randomMove = randint(1, 3)
if randomMove == 1:
    pcMove = "rock"
elif randomMove == 2:
    pcMove = "paper"
elif randomMove == 3:
    pcMove = "scissor"

player_1 = input("player_1, make your move: ").lower()
print(f"move of player_2 is {pcMove}")
player_2 = pcMove

if player_1 == player_2:
    print("thats a tie")
elif player_1 == "rock":
    if player_2 == "paper":
        print("player_2 wins")
    elif player_2 == "scissor":
        print("player_1 wins")
elif player_1 == "paper":
    if player_2 == "rock":
        print("player_1 wins")
    elif player_2 == "scissor":
        print("player_2 wins")
elif player_1 == "scissor":
    if player_2 == "paper":
        print("player_1 wins")
    elif player_2 == "rock":
        print("player_2 wins")
else:
    print("somthing is wrong")
