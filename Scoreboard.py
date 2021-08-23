list = []
def get_first_value(string):
    print(string[0])
    return string[0]

def SortList():
    list = []
    with open("./Scores.txt", "w") as scores:
        for line in scores:
            list.append(line)
    print(sorted(list, key=get_first_value))
    
SortList()