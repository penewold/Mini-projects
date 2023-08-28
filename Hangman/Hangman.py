import random

words = ["equation", "shadow", "resource", "basket", "knowledge", "handicap", "skin", "know", "bank", "sympathetic", "roof", "chart", "comment", "terrace", "joint", "positive", "disappear", "reproduction", "kneel", "serve"]
guesses = 0
word = random.choice(words)
running = True

print("The program is gonna pick a random word from a list of words. You have to guess it. You have 7 guesses. Each time you guess wrong you get closer to losing")

def hangman(stage):
    if stage == 1:
        return '''
         ____
        |    |
        |    
        |
        |
        |
        |___
'''
    if stage == 2:
        return '''
         ____
        |    |
        |    O
        |
        |
        |   
        |___
'''
    if stage == 3:
        return '''
         ____
        |    |
        |    O
        |    |
        |
        |   
        |___
'''
    if stage == 4:
        return '''
         ____
        |    |
        |    O
        |   /|
        |
        |   
        |___
'''
    if stage == 5:
        return '''
         ____
        |    |
        |    O
        |   /|v
        |
        |   
        |___
'''
    if stage == 6:
        return '''
         ____
        |    |
        |    O
        |   /|v
        |   /
        |   
        |___
'''
    if stage == 7:
        return '''
         ____
        |    |
        |    O
        |   /|v
        |   /(
        |   
        |___
'''
while running == True:
    for i in range(8):
        print(hangman(i))
    running = False