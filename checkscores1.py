player_score = 0
code = ""


def check_score(player_score):

    if player_score > 0:
        code = True
    else:
        code = False
    return code

if check_score(int(input("Waht is the player score:"))):
    print("Continue")
else:
    print("Sorry, you have no lives left")
    print("{final summary}")
