class Point:

    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # self is like this keyword in java. In python you are forced to use the self keyword for referencing current object
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
print(point1.x)
print(point1.y)

# changing value of x only
point1.x = 30

print(point1.x)
print(point1.y)





