import random

# random() function randomly returns a value between 0 and 1. Eg., value = 0.12421...
print(random.random())

# to generate integer random values (and) to give a range within which we want to generate random values
print(random.randint(b=20, a=10))


# to randomly select from a list or set etc...
listx = [1, 10, 96, 123, 89, 90, 123]
print(random.choice(listx))

