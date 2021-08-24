# check player scores
def check_score(player_score):
    # if score is more than 0 return true so that i can do "if check_score:"
    if player_score > 0:
        code = True
    #if not return False
    else:
        code = False
    return code

"""
Used for testing:

while True:
    if check_score(int(input("Waht is the player score:"))):
        print("Continue")
    else:
        print("Sorry, you have no lives left")
        print("{final summary}")"""

