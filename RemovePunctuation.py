from cleantext import clean
def cleaninput(text):
    return clean(text, all=True)

print(cleaninput("!@##%$&^*^(^)&)(|}{]\[?><1234567890qwertyuiopasdfghjklzxcvbnm,./"))
