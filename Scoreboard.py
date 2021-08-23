list = []
def get_first_value(string):
    

with open("./Scores.txt", "r") as scores:
    for line in scores:
        list.append(line)
print(list)