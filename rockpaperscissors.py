from random import randint
import time

valid = 1
# List of possible answers computer picks from
Game = ["Rock", "Paper", "Scissors"]


def compare (x,y):
     # Convert all variables to lower case in case user input differs from specified
    if Game[y-1].lower() == x.lower():
        return("\nDraw!\nPlay again:")
    elif Game[y-1].lower() == "rock":
        if x.lower() == "scissors": 
            return("\nYou Lose!\nPlay again:")  
        elif x.lower() == "paper": 
            return("\nYou Win!\nPlay again:")
    elif Game[y-1].lower() == "paper":
        if x.lower() == "rock": 
            return("\nYou Lose!\nPlay again:")  
        elif x.lower() == "scissors": 
            return("\nYou Win!\nPlay again:")
    elif Game[y-1].lower() == "scissors":
        if x.lower() == "paper": 
            return("\nYou Lose!\nPlay again:")  
        elif x.lower() == "rock": 
            return("\nYou Win!\nPlay again:")

while valid == 1:
    # Check if player wants to play:
    z = input("Ready to play Rock, Paper Scissors?"+" ")
    # Convert all inputs to lower case in case user input differs from specified
    if z.lower() == "yes" or z.lower() == "yep" or z.lower() == "yeah" or z.lower() == "yh":
        valid = 1
    else:
        break

    # Loading Time 
    time.sleep(0.5)
    print("\n3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1\n")
    time.sleep(1)

    # Get input play from user
    user_input = input("Rock, Paper or Scissors?"+" ")

    if user_input.lower() in Game:
        # Computer picks at random
        computer_random = randint(0,3)

        # Prints game outcome
        print("\nI picked:", Game[computer_random-1])
        print(compare(user_input, computer_random))

    else:
        # Check if input valid
        print("\nInvalid input - try again!\n")


