# Ask the user for their name and difficulty

from RemovePunctuation import cleaninput


def playerInformation():
    name = input("What is your first name? ")
    name = cleaninput(name)

    while name == "":
        name = input("Please enter a valid name: ")
        name = cleaninput(name)

    print("\nHello, " + name.capitalize())
    print("Welcome to my maths quiz")

    print("\nImportant information:\n")

    print("\tYour score goes up everytime you get a correct answer")
    print("\tand goes down everytime you get a incorrect answer")
    print("\tif your score gets to 0 the game will end")
    print("\tThe questions will get harder as you play.")
    print("\tIf you have to leave the quiz just enter 'exit' into a question")

    difficulty = input(
        "\nWhat difficulty would you like to play with?\n"
        "Easy or Hard: ").capitalize()

    # Check if the user has entered easy or hard. if not, ask them again.
    while True:
        if difficulty in ["Easy", "Hard"]:
            break
        difficulty = input(
            "Please enter a difficulty\nEasy or Hard: ").capitalize()
    return name.capitalize(), difficulty
