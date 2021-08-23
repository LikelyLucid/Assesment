list = []
def get_first_value(string):
    return string[0]

with open("./Scores.txt", "r") as scores:
    for line in scores:
        list.append(line)
print(list.sort(key = get_first_value(flist[])))