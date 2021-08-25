import random
import string
from checkscores1 import check_score
from PlayerInformation2 import playerInformation
from Scoreboard import *
global rounds
points = 1
rounds = 0
cheatermode = False  # used for testing will give you the answer
easymin, easymax = 0, 30  # minimum and maximum numbers for equations
hardmin, hardmax = -20, 100

# set name and difficulty to the returned values
name, difficulty = playerInformation()
# check for interger


def integer_checker(question):
    error = "\nSorry, you must enter a number\n"
    number = ""

    while not number:
        try:
            number = input(question)
            if number == "exit":
                finish()
            number = int(number)
            return number
        except ValueError:
            print(error)


def finish():
    print(f"you lasted {rounds} rounds")
    add_to_Scoreboard(f"{rounds} - {difficulty} - {name} ")
    print("")
    exit()


def answerright(points):
    global rounds
    print("Correct answer!")
    points = points + 1  # add 1 to score
    # minus 1 point because they start with 1 point,
    print(f"you have {points} lives left")
    rounds += 1
    # Easier than setting score to 0 and checking if score is -1
    return points


def answerwrong(points):
    global rounds
    print("answer wrong")
    print(f"The answer was {answer}")
    points = points - 1  # add 1 to score
    if not check_score(points):  # check if score is 0
        finish()  # if so call the end code
    print(f"you have {points} lives left")  # wont run if the end code is called
    rounds += 1
    return points  # return the points


while True:
    if difficulty == "Easy":
        # Set numbers to random a random number
        num1 = random.randint(easymin, easymax + (rounds * 3))
        num2 = random.randint(easymin, easymax + (rounds * 3) )
        # Make a choice between + or -
        choice = random.randint(1, 2)

        if choice == 1:
            # figure out the answer
            answer = num1 + num2
            if cheatermode:
                print(answer)
            if answer < 0:
                num1, num2 = num2, num1
                answer = num1 + num2
            # ask for answer and check if it is an integer
            ask = integer_checker("What does\n{} + {} = ".format(num1, num2))
            if ask == answer:
                points = answerright(points)

            else:
                points = answerwrong(points)

        elif choice == 2:
            # figure out the answer
            answer = num1 - num2
            if cheatermode:
                print(answer)
            if answer < 0:
                num1, num2 = num2, num1
                answer = num1 - num2
            # ask for answer through interger checker
            ask = integer_checker("What does\n{} - {} = ".format(num1, num2))
            if ask == answer:
                points = answerright(points)

            else:
                points = answerwrong(points)

    elif difficulty == "Hard":
        hardmin, hardmax = hardmin+(rounds * 7), hardmax+(rounds * 7)
        # Set numbers to random a random number
        num1 = random.randint(hardmin, hardmax)
        num2 = random.randint(hardmin, hardmax)
        # Make a choice between + or - or *
        choice = random.randint(1, 3)

        if choice == 1:
            # figure out the answer
            answer = num1 + num2
            if cheatermode:
                print(answer)
            # ask for answer and check if it is an integer
            ask = integer_checker("What does\n{} + {} = ".format(num1, num2))
            if ask == answer:
                points = answerright(points)

            else:
                points = answerwrong(points)

        elif choice == 2:
            # figure out the answer
            answer = num1 - num2
            if cheatermode:
                print(answer)
            # ask for answer through interger checker
            ask = integer_checker("What does\n{} - {} = ".format(num1, num2))
            if ask == answer:
                points = answerright(points)

            else:
                points = answerwrong(points)


        else:
            # change the difficulty of the numbers because when testing they were to hard to solve,
            # mostly because you had to times and divide in the hundreds
            max = 1 + rounds * 3
            num1 = random.randint(1, max)
            num2 = random.randint(1, max)
            # figure out the answer
            answer = num1 * num2
            if cheatermode:
                print(answer)
            # ask for answer through interger checker
            ask = integer_checker("What does\n{} * {} = ".format(num1, num2))
            if ask == answer:
                points = answerright(points)

            else:
                points = answerwrong(points)
