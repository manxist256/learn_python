secret=9

chances = 3
guessed = False

while chances > 0:
    guess = int(input())
    if guess == secret:
        guessed = True
        break
    chances = chances - 1
if guessed:
    print("Correct")
else:
    print("Chances are Over!")
