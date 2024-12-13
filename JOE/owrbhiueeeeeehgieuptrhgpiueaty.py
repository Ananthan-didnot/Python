"""
Author: Joe George
Date: 3 December 2024
Stick Game
"""

def stickgame():
    print("Hello PLayers Welcome to Stick Game!")
    player1 = input("Enter the name of Player 1:")
    player2 = input("Enter the name of Player 2:")
    sticknum = 16

    while sticknum > 0:
        p1_turn = int(input(f"{player1}! Enter the number of sticks you want to take ( 1,2 or 3): "))
        if p1_turn in range(1, 4):
            sticknum -= p1_turn
            print(f"You selected {p1_turn} number of sticks. \n Sticks Remaining: {sticknum}")
        else:
            print("Invalid number of Sticks!")
            print(f"Sticks Remaining: {sticknum}")
        if sticknum == 0:
            print(f"{player1}! you picked the last stick. You Lose! \n {player2} WINS!!!!")
            break

        p2_turn = int(input(f"{player2}! Enter the number of sticks you want to take ( 1,2 or 3): "))
        if p2_turn in range(1, 4):
            sticknum -= p2_turn
            print(f"You selected {p2_turn} number of sticks. \n Sticks Remaining: {sticknum}")
        else:
            print("Invalid number of Sticks!")
            print(f"Sticks Remaining: {sticknum}")
        if sticknum == 0:
            print(f"{player2}! you picked the last stick. You Lose! \n {player1} WINS!!!!")
            break

    print("Thank You for playing Stick Game!!")
