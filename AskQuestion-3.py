import random
from checkscores1 import check_score
points = 1

difficulty = "easy"
easymin, easymax = 0, 30
hardmin, hardmax = -20, 100

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
    print("your score was: ", points - 1)
    exit()


def answerright(points):
    print("Correct answer!")
    points = points + 1 # add 1 to score
    print("your score is: ", points - 1)
    return points


def answerwrong(points):
    print("answer wrong")
    print(f"The answer was {answer}")
    points = points - 1  # add 1 to score
    if check_score(points): #check if score is 0
        finish() #if so 
    print("your score is: ", points - 1)
    return points


while True:
    if difficulty == "easy":
        # Set numbers to random a random number
        num1 = random.randint(easymin, easymax)
        num2 = random.randint(easymin, easymax)
        # Make a choice between + or -
        choice = random.randint(1, 2)

        if choice == 1:
            # figure out the answer
            answer = num1 + num2
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

    elif difficulty == "hard":
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
