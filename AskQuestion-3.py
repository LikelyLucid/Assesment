import random
from checkscores1 import check_score
from PlayerInformation1 import playerInformation
global rounds
points = 1
rounds = 0
cheatermode = False
difficulty = "easy"
easymin, easymax = 0, 30
hardmin, hardmax = -20, 100
name, difficulty = playerInformation()
# check for interger
def integer_checker(question):
    error = "\nSorry, you must enter a number\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


def finish():
    global rounds
    print("your score was: ", points - 1)
    print(f"you lasted {rounds} rounds")
    exit()


def answerright(points):
    global rounds
    print("Correct answer!")
    points = points + 1 # add 1 to score
    print("your score is: ", points - 1)# minus 1 point because they start with 1 point, 
    rounds += 1
    return points                       # Easier than setting score to 0 and checking if score is -1


def answerwrong(points):
    global rounds
    print("answer wrong")
    print(f"The answer was {answer}")
    points = points - 1  # add 1 to score
    if not check_score(points): #check if score is 0
        finish() #if so call the end code
    print("your score is: ", points - 1) # wont run if the end code is called
    rounds += 1
    return points #return the points


while True:
    if difficulty == "Easy":
        # Set numbers to random a random number
        num1 = random.randint(easymin, easymax)
        num2 = random.randint(easymin, easymax)
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
        hardmin, hardmax = hardmin+(points * 5), hardmax+(points * 5)
        # Set numbers to random a random number
        num1 = random.randint(hardmin, hardmax)
        num2 = random.randint(hardmin, hardmax)
        # Make a choice between + or -
        choice = random.randint(1, 4)

        if choice == 1:
            # figure out the answer
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
            # ask for answer through interger checker
            ask = integer_checker("What does\n{} - {} = ".format(num1, num2))
            if ask == answer:
                points = answerright(points)

            else:
                points = answerwrong(points)

        elif choice == 4:
            # figure out the answer
            answer = num1 * num2
            # ask for answer through interger checker
            ask = integer_checker("What does\n{} * {} = ".format(num1, num2))
            if ask == answer:
                points = answerright(points)

            else:
                points = answerwrong(points)
