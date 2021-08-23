list = []
def get_first_value(e)
with open("./Scores.txt", "r") as scores:
    for line in scores:
        list.append(line)
print(list)