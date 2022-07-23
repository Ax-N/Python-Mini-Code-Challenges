# Rock, Paper, and Scissors By me
# 0 > 2
# 2 > 1
# 1 > 0
import random
import os

playerWins = 0
playerLoses = 0
Draws = 0
def game():
    global playerWins
    global playerLoses
    global Draws
    os.system('cls') # Clears the Terminal

    print("Rock, Paper, Scissors.... SHOOT \n")

    print("0: Rcok")
    print("1: Paper")
    print("2: Scissors")
    print("3: History")
    print("4: Exit")

    player = int(input()) # Player input in the form of an integer beween 0 and 4
    while not int(player) in range(0,5):
        player = int(input("Please enter an Integer between 0-4: "))
    
    if player == 4: # Exits the terminal
        exit()

    if player == 3: # Displays Game History
        os.system('cls')
        print("Wins: ", playerWins)
        print("Loses: ", playerLoses)
        print("Draws: ", Draws)
        pause()
        game()

    comP = random.randrange(0,3) # number from 0-2 for the computers move
    c = ["Rock", "Paper", "Scissors"] # list for the words

    # States the Player's Choice and the Computer's Choice
    os.system('cls')
    print("The Computer chose " + c[comP])
    print("You chose " + c[player])

    # Compares the Players Choice and the Computer's Choice to determine the victor
    if comP == player:
        print("It's a Draw")
        Draws += 1

    elif comP == 0 and player == 2:
        print("You Lost")
        playerLoses += 1

    elif comP == 2 and player == 0:
        print("You Won")
        playerWins  += 1

    elif comP > player:
        print("You Lost")
        playerLoses += 1

    elif comP < player:
        print("You Won")
        playerWins  += 1

    pause()
    game() # Creates a recursive loop

def pause(massage = 'press any key to continue'):  # this function will pause the script with a default massage or a custome one.
    print(massage)
    os.system('pause >NULL')  # this will pause untill any key is pressed.
    return 0

game()