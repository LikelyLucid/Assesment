list = []
def get_first_value(string):
    print(string[0])
    return string[0]

def SortScores():
    list = []
    with open("./Scores.txt", "r") as scores:
        for line in scores:
            list.append(line)
    # print(sorted(list, key=get_first_value))
    return sorted(list, key=get_first_value)

#print(SortScores())
string = "100 - Michael"
print(string.split("-"))
