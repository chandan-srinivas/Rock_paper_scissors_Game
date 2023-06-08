from random import *

moves = ["rock","paper","scissors"]
gamerunning = True

while gamerunning:
    computer = moves[randint(0,2)]
    player = input("rock,paper or scissors? (or exit from the game): ").lower()
    if player=="exit from the game":
        gamerunning = False
    elif player == computer:
        print("Tie!")
    elif player == "rock":
        if computer=="paper":
            print("You Lose! ",computer,"beats",player)
        else:
            print("You Win! ",player," beats ",computer)
    elif player == "paper":
        if computer == "scissors":
            print("You Lose! ",computer," beats ",player)
        else:
            print("You Win! ",player," beats ",computer)
    elif player == "scissors":
        if computer == "rock":
            print("You Lose! ",computer," beats ",player)
        else :
            print("You Win! ",player," beats ",computer)
    else:
        print("please Check if spelling is wrong!")
