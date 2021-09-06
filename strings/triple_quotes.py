email = '''
Hi Manikandan,

This is an email for you,

Congratulations

'''

print(email)
print('End of printing email in triple quotes')

email = 'Helloworld helloworld helloworld helloworld'

print(email[17]) # access index of string variable is same as .chatAt() function in java
print(email[-1]) # prints the last character
print(email[-2]) # prints the second character from last and so-on...
print(email[3:6]) # returns character at index 3,4,5. start = inclusive and end = exclusive
print(email[3:]) # if end index is not provided, then 3 -> endIndex all chars are printed
print(email[:7]) # if start index is not provided, then it picks 0 by default, so here it prints 0,1,2,3,4,5,6 (excluding 7 remember above)
print(email[:]) # prints 0 -> endIndex all chars, same as print(email) statement

name = 'Jennifer'
print(name[1:-1]) # starts from 1st index and prints until end (excluding last index alone)




