listx = [1, 2, 3, 6, 9, 1, 1, 2, 1]

# append adds to the end of the list
listx.append(20)
print(listx)

# insert adds an element to a specific index position, moving all the subsequent items one position right
listx.insert(0, 23)
print(listx)

# remove - removes the first occurence of a given element
listx.remove(1)
print(listx)

# pops the elements from the list with provided index
listx.pop(2)
print(listx)

# returns the index of the first occurence of the element 9 in the listx
print(listx.index(9)) # output -> 4
#gives error if the element is not present in the list
# another way of finding an element in the list
print(50 in listx) # -> returns True / False

# counts the number of occurences of a given item
print(listx.count(1))

#sort
print(listx.sort())
print(listx)
listx.reverse() # reverses the entire list | irrespective of sorting
print(listx)

# clears all the elements from the list
listx.clear()
print(listx)

