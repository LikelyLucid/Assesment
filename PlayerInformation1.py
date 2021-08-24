
# Ask the user for their name and difficulty
from RemovePunctuation import cleaninput
import string
def playerInformation():
    name = input("What is your name? ")
    name = cleaninput(name)

    while name == "":
        name = input("Please enter a valid name: ")
        name = cleaninput(name)

    print("Hello, " + name.capitalize())
    print("Welcome to my maths quiz")
    print("Important information:")
    print("")


    difficulty = input("What difficulty would you like to play with?\nEasy or Hard: ").capitalize()


    # Check if the user has entered easy or hard. if not, ask them again.
    while True:
        if difficulty in ["Easy", "Hard"]:
            break
        difficulty = input("Please enter a difficulty\nEasy or Hard: ").capitalize()
    return name.capitalize(), difficulty




