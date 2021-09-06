# fn. returns a value
def find_square(num):
    return num * num


print(find_square(5))


# if fn. doesn't returns a value, then python adds a return statement by itself.
# statement added by python = "return None". None is same as Null in other programmingdd languages
def return_nothing(num):
    print(num * num)


print(return_nothing(5)) # prints "None"

