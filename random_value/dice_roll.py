import random


def roll():
    a = random.randint(1, 6)
    b = random.randint(1, 6)

    # by default below returns a type, parenthesis is not mandatory
    return a, b


print(roll())
