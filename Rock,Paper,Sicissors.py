import random

choice= ['rock','paper','scissor']
comp_point = 0
user_point = 0

while True:
    user_choice = input("Choose one (rock,paper,scissor).(quit to exit)")
    comp_choice = random.choice(choice)
    print(f"Computer choose {comp_choice}\n"
              f"You choose {user_choice}")

    if user_choice=="quit":
        break
    elif user_choice not in choice:
        print("Invalid choice,Try again")
        continue

    elif(comp_choice=="rock" and user_choice=="paper" or 
         comp_choice=="scissor" and user_choice=="rock" or
         comp_choice=="paper" and user_choice=="scissor"):
         print("You won!")
         user_point += 1
    elif user_choice==comp_choice:
        print("Its a Tie!")
    else:
        comp_point+=1
        print("You Lose!,Try again")

print(f"Final score\n You={user_point}\tComputer={comp_point}")

