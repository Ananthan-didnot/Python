"""
Author:Ananthakrishnan KV
Date:3/1/2024
Stick game
Version 1.0
"""

print("*RULE*"
      "\nThere are total 16 sticks"
      "\nEach player can pick 1,2 or 3 stick in one try")

def stick_game():
    player1=input("Enter name of 1st player: ")
    player2=input("Enter name of 2nd player: ")
    p1=0
    p2=0
    sticks=16

    while sticks>0:
        print("Remaining sticks: ", sticks)
        pick1=int(input(f"{player1},pick 1 , 2 or 3 sticks: "))
        if pick1==1 or pick1==2 or pick1==3:
            sticks-=pick1
            p1=sticks
        else:
            print("Invalid input,You can only choose 1 , 2 or 3")
        print("Remaining sticks: ", sticks)
        pick2 = int(input(f"{player2},pick 1 , 2 or 3 sticks: "))
        if pick2==1 or pick2==2 or pick2==3:
             sticks-=pick2
             p2=sticks
        else:
            print("Invalid input,You can only choose 1 , 2 or 3")


    if p1==0:
        print(f"{player1}, choose the last stick.He lose the game.")
    elif p2==0:
        print(f"{player2}, choose the last stick.He lose the game.")


print(stick_game())

