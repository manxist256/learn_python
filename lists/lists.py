list1 = ["a1", "a2", "a3", "a4", "a5"]

# access array elements directly using indexes
print(list1[1])

# prints last element in list
print(list1[-1])

# prints second last element in the list
print(list1[-2])

# prints from start to destination index excluding destination index
print(list1[1:3])

# since start not provided, defaults to 0
print(list1[:3])

# since end not provided, defaults to last
print(list1[1:])

# since both not provided, defaults from 0 to lastIndex (inclusive)
print(list1[:])

# modify the value (of an index) of the list
list1[0] = "ax"
print(list1)