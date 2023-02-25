import random
while True:
    choices = ["rock" , "paper" ,"scissor"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock,paper,scissor? ").lower()

    if player == computer:
        print("player : " , player)
        print("Computer :  " ,computer)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("player : ", player)
            print("Computer :  ", computer)
            print("you lose! ")
        if computer == "scissor ":
            print("player : ", player)
            print("Computer :  ", computer)
            print("you win! ")
    elif player == "scissor":
        if computer == "rock":
            print("player : ", player)
            print("Computer :  ", computer)
            print("you loss! ")
        if computer == "paper ":
            print("player : ", player)
            print("Computer :  ", computer)
            print("you win! ")
    elif player == "paper":
        if computer == "scissor":
            print("player : ", player)
            print("Computer :  ", computer)
            print("you loss! ")
        if computer == "rock ":
            print("player : ", player)
            print("Computer :  ", computer)
            print("you win! ")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("By!")



#                       precise form


import random

p1 = input("Player 1 : Enter your choice => ").upper()

p2 = input("Player 2 : Enter your choice => ").upper()

if (p1 == "ROCK" and p2 == "SISSOR") or (p1 == "PAPER" and p2 == "ROCK") or (p1 == "SISSOR" and p2 == "PAPER"):

    print("\nPlayer 1 wins")

elif (p1 == "ROCK" and p2 == "PAPER") or (p1 == "PAPER" and p2 == "SISSOR") or (p1 == "SISSOR" and p2 == "ROCK"):

    print("\nPlayer 2 wins")

else:

    print("\nGame Draw")

    # COMBINATIONS

    # player 1             Player 2        Win

    # rock                 rock            draw
    # rock                 paper           player 2
    # rock                 sissor          player 1

    # paper                rock            player 1
    # paper                paper           draw
    # paper                sissor          player 2

    # sissor               rock            player 2
    # sissor               paper           player 1
    # sissor               sissor          draw