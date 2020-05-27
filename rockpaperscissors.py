from random import randint
import math
import time

valid = 1

while valid == 1:
    # Check if player wants to play:
    z = input("Ready to play Rock, Paper Scissors?"+" ")
    # Convert all inputs to lower case in case user input differs from specified
    if z.lower() == "yes":
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
    x = input("Rock, Paper or Scissors?"+" ")

    # Computer picks at random
    y = randint(0,3)

    # List of possible answers computer picks from
    Game = ["Rock", "Paper", "Scissors"]

    # Prints game outcome
    print("\nI picked:", Game[y-1])

    # Convert all variables to lower case in case user input differs from specified
    if Game[y-1].lower() == x.lower():
        print("\nDraw!\n")
    elif Game[y-1].lower() == "rock":
        if x.lower() == "scissors": 
            print("\nYou Lose!\n")  
        elif x.lower() == "paper": 
            print("\nYou Win!\n")
    elif Game[y-1].lower() == "paper":
        if x.lower() == "rock": 
            print("\nYou Lose!\n")  
        elif x.lower() == "scissors": 
            print("\nYou Win!\n")
    elif Game[y-1].lower() == "scissors":
        if x.lower() == "paper": 
            print("\nYou Lose!\n")  
        elif x.lower() == "rock": 
            print("\nYou Win!\n")

