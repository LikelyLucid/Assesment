global list 
list= []
def get_first_value(string):
    print(string.split("-")[0])
    return int(string.split("-")[0])

def SortScores():
    # print(sorted(list, key=get_first_value))
    return sorted(list, key=get_first_value, reverse=True)

def add_to_Scoreboard(string):
    with open("./Scores.txt", "a+") as scores:
        for line in scores:
            list.append(line)
        print(line)

        scores.seek(0)
add_to_Scoreboard("23 - Michael")
scores = SortScores()
print(scores)


