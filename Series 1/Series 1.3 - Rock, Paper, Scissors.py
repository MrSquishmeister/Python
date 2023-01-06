import random
#imports random so it can be used
import sys

def game():
    action = ("rock", "paper", "scissors")
#sets list of actions

    cchoice = (random.choice(action))
#randomly selects from list
    print("-----------------------------------------------------")
    choice = input("Enter rock, paper or scissors: ")
#takes users choice
    print(("You: ") + (choice))
#displays what user entered
    print(("Opponent: ") + (cchoice))
#displays random choice

    if choice == "rock" and cchoice == "rock":
        print("Result: Draw")
        after()
    elif choice == "rock" and cchoice == "paper":
        print("Result: Loss")
        after()
    elif choice == "rock" and cchoice == "scissors":
        print("Result: Win")
        after()
    elif choice == "paper" and cchoice == "rock":
        print("Result: Win")
        after()
    elif choice == "paper" and cchoice == "paper":
        print("Result: Draw")
        after()
    elif choice == "paper" and cchoice == "scissors":
        print("Result: Loss")
        after()
    elif choice == "scissors" and cchoice == "rock":
        print("Result: Loss")
        after()
    elif choice == "scissors" and cchoice == "paper":
        print("Result: Win")
        after()
    elif choice == "scissors" and cchoice == "scissors":
        print("Result: Draw")
        after()
    else:
        print("Try again")
        game()

def after():
    print("-----------------------------------------------------")
    print("""Choices:
    1. Play Again
    2. Exit""")
    answer = str(input("Choice: "))
    if answer == "1":
        game()
    elif answer == "2":
        print("--------------------------Exit-----------------------")
        sys.exit(99)
    else:
        print("Error. Try again")
        after()
    

print("---------------Rock Paper Scissors Game--------------")
game()


