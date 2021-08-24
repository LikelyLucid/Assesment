import random


easy_questions = ["How many days are there in a week: ",
                  "How many letters are there in the English alphabet: ",
                  "How many sides are in a Triangle: ",
                  "How many months do we have in a year: ",
                  "What is the biggest animal in the world: ",
                  "What is the tallest animal in the world: ",
                  "How many sides does a square have: ",
                  "What is a baby dog called: ",
                  "What is the Maori number for 1: ",
                  "How many days in February in a non-leap year: "]
# Aligning answers corresponding positions to questions
easy_answers = ["7", "26", "3", "12", "blue whale",
                "giraffe", "4", "puppy", "tahi", "28"]


hard_questions = ["Na is chemical symbol for what element: ",
                  "What is the capital of Spain: ",
                  "Whats the worlds largest ocean: ",
                  "What language has the most words: ",
                  "What is the largest bone in the body: ",
                  "what year was the first moon landing: ",
                  "Which animal has the largest eye: ",
                  "Where would you find the Sea of Tranquility: ",
                  "What is the name of the greek god of the sky: ",
                  "What animal has the most species: "]
# Aligning answers corresponding positions to questions
hard_answers = ["sodium", "madrid", "pacific", "english", "femur",
                "1969", "giant squid", "the moon", "zeus", "ants"]


def easy_quiz():
    total_correct = 0
    while len(easy_questions) > 0:
        ask_question = random.randint(0, (len(easy_questions) - 1))
        easy_input = input(easy_questions[ask_question]).lower()
        easy_compare = easy_answers[ask_question]
        easy_questions.pop(ask_question)
        easy_answers.pop(ask_question)
        # Keeping both answer and question in
        # unison remove question and answer from same position based on
        # how many are left in the question picker
        if easy_input == easy_compare:
            print("Correct!")
            total_correct += 1
        else:
            print("Incorrect")
            print()
    return total_correct


def hard_quiz():
    total_correct = 0
    while len(hard_questions) > 0:
        ask_question = random.randint(0, (len(hard_questions) - 1))
        hard_input = input(hard_questions[ask_question]).lower()
        hard_compare = hard_answers[ask_question]
        hard_questions.pop(ask_question)
        hard_answers.pop(ask_question)  # Keeping both answer and question in
        # unison remove question and answer from same position based on
        # how many are left in the question picker
        if hard_input == hard_compare:
            print("Correct!")
            total_correct += 1
        else:
            print("Incorrect")
    return total_correct


def integer_checker(question):
    error = "\nSorry, you must enter a positive integer:"
    number = ""
    while not number:
        try:
            number = int(input(question))
            if number < 0:
                print(error)
                number = ""
            else:
                return number
        except ValueError:
            print(error)


# Function to not allow a blank 'name' or any digits
def check_blank():
    global person_name
    while not str.isalpha(person_name):  # Boolean expression to return false
        # if any digits or left blank
        person_name = input("Please do not leave blank "
                            "and/or do not include "
                            "digits or symbols: ").capitalize()


# Main Routine
person_name = input("What is your name: ").capitalize()
# .capitalize automatically capitalizes the first letter in the string
check_blank()
person_age = integer_checker("Please enter your age: ")
print("\nHello {} welcome to my quiz!".format(person_name))

if 11 >= person_age >= 0:
    amount_correct = easy_quiz()

elif person_age >= 12:
    amount_correct = hard_quiz()
print("******* Summaries! *******")
if amount_correct == 0:
    print("Better luck next time\nYou got 0 correct.")
elif amount_correct == 10:
    print("Wow, Good Job! \nYou got all of them Correct!")
else:
    print("Good try, you got {} Correct.".format(amount_correct))
