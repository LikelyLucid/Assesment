list = []
def get_first_value(string):
    print(string[0])
    return string[0]
def 
with open("./Scores.txt", "r") as scores:
    for line in scores:
        list.append(line)
print(sorted(list, key=get_first_value))