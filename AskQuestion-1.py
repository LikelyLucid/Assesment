import random

difficulty = "hard"
easymin, easymax = 0, 30
hardmin, hardmax = -20, 100
points = 0


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
    print("your score is: ", points)
    exit()


def answerright():
    print("answer right")
    points = + 1
    print("your score is: ", points)


def answerwrong():
    print("answer wrong")
    print("The answer was {}".format(answer))
    if points == 0:
        finish()

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
            if answer < 0:
                num1, num2 = num2, num1
                answer = num1 + num2
            # ask for answer and check if it is an integer
            ask = integer_checker("What does\n{} + {} = ".format(num1, num2))
            if ask == answer:
                answerright()

            else:
                answerwrong()

        elif choice == 2:
            # figure out the answer
            answer = num1 - num2
            if answer < 0:
                num1, num2 = num2, num1
                answer = num1 - num2
            # ask for answer through interger checker
            ask = integer_checker("What does\n{} - {} = ".format(num1, num2))
            if ask == answer:
                answerright()

            else:
                answerwrong()

    if difficulty == "hard":
        hardmin, hardmax =+ (points * 5) 
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
                answerright()

            else:
                answerwrong()

        elif choice == 2:
            # figure out the answer
            answer = num1 - num2
            # ask for answer through interger checker
            ask = integer_checker("What does\n{} - {} = ".format(num1, num2))
            if ask == answer:
                answerright()

            else:
                answerwrong()

        elif choice == 2:
            # figure out the answer
            answer = num1 / num2
            # ask for answer through interger checker
            ask = integer_checker("What does\n{} / {} = ".format(num1, num2))
            if ask == answer:
                answerright()

            else:
                answerwrong()

        elif choice == 4:
            # figure out the answer
            answer = num1 * num2
            # ask for answer through interger checker
            ask = integer_checker("What does\n{} * {} = ".format(num1, num2))
            if ask == answer:
                answerright()

            else:
                answerwrong()
