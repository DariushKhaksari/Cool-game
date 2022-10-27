from random import *
print(""" 
Welcome to my game, Be careful maybe this is the last time you are life... \U0001f923 \U0001f923 \U0001f923 \U0001f923 
they are your moves: 
 Rock \U0001F60E
 Paper \U0001F60E
 Scissor \U0001F60E
 For quit type exit. 
 ---------------""")

randomMove = randint(1, 3)
if randomMove == 1:
    pcMove = "rock"
elif randomMove == 2:
    pcMove = "paper"
elif randomMove == 3:
    pcMove = "scissor"
player1_wins = 0
player2_wins = 0
win=3
while player1_wins < win and player2_wins < win:
    print(f"player_1\U0001f449 {player1_wins} and player_2\U0001f449 {player2_wins}")

    player_1 = input("player_1, make your move: ").lower()
    print(f"move of player_2 is {pcMove}")
    player_2 = pcMove
    if player_1=="exit":
        break
    if player_1 == player_2:
        print("thats a tie")
    elif player_1 == "rock":
        if player_2 == "paper":
            print("player_2 wins")
            player2_wins += 1
        elif player_2 == "scissor":
            print("player_1 wins")
            player1_wins += 1
    elif player_1 == "paper":
        if player_2 == "rock":
            print("player_1 wins")
            player1_wins += 1
        elif player_2 == "scissor":
            print("player_2 wins")
            player2_wins += 1
    elif player_1 == "scissor":
        if player_2 == "paper":
            print("player_1 wins")
            player1_wins += 1
        elif player_2 == "rock":
            print("player_2 wins")
            player2_wins += 1
    else:
        print("somthing is wrong")
print(f"Final: player_1\U0001f449 {player1_wins} and player_2\U0001f449 {player2_wins}")
