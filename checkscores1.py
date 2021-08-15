player_score = 0
code = ""


def check_score(player_score):

    if player_score > 0:
        code = True
    else:
        code = False
    return code

if check_score(0):
    print("Continue")