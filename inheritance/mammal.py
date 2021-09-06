class Mammal:
    def walk(self):
        print("Walking!")


# Just by passing the reference of Mammal inside the parenthesis, Dog inherits Mammal class
# Python doesn't allow empty classes or empty methods, hence to add a dummy statement, we add 'pass'
class Dog(Mammal):
    pass

    def walk(self):
        print("Walking!")


# Just by passing the reference of Mammal inside the parenthesis, Cat inherits Mammal class
class Cat(Mammal):
    def __init__(self):
        print("Constructor of Cat class")
