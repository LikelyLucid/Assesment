global list 
list= []
def get_first_value(string):
    print(string.split("-")[0])
    return int(string.split("-")[0])


def emptyfile(file):
    open(file, "w").close #opens a file in write mode to delete all contents and closes it

def SortScores():
    # print(sorted(list, key=get_first_value))
    return sorted(list, key=get_first_value, reverse=True)

def printscores():
    with open("./Scores.txt", "r") as scores:
        for line in scores:
            print(line.replace("\n", ""))

def add_to_Scoreboard(string):
    with open("./Scores.txt", "r+") as scores: #open file in read and append mode
        for line in scores:
            list.append(line.replace("\n", "")) #replace \n in line with nothing
        list.append(string) 
    emptyfile("./Scores.txt")
    sortedlist = SortScores()
    
    with open("./Scores.txt", "a") as scores:
        for i in sortedlist:
            scores.write(i + "\n")
    printscores()





