global list
list = []


def get_first_value(string):
    # print(string.split("-")[0])  #for testing to see the output
    return int(string.split("-")[0])


def emptyfile(file):
    # opens a file in write mode to delete all contents and closes it
    open(file, "w").close


def SortScores():
    # print(sorted(list, key=get_first_value))
    return sorted(list, key=get_first_value, reverse=True)


def printscores():
    print("Score board:")
    # open Scores.txt in read mode so it doesn't change the value on accident
    with open("./Scores.txt", "r") as scores:
        for line in scores:
            print(line.replace("\n", ""))  # remove \n and print it


def add_to_Scoreboard(string):
    with open("./Scores.txt",
              "r+") as scores:  # open file in read and append mode
        for line in scores:
            # replace \n in line with nothing
            list.append(line.replace("\n", ""))
        list.append(string)
    emptyfile("./Scores.txt")
    sortedlist = SortScores()

    with open("./Scores.txt", "a") as scores:
        for i in sortedlist:
            # add the line and a \n to make the next item on another line
            scores.write(i + "\n")
    printscores()
