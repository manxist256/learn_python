year_of_dob = input('Enter year of birth: ')  # whatever input you provide, it's type is always String in python input() function
print(type(year_of_dob)) # returns string

diff = 2021 - int(year_of_dob)
# use int(arg) function to cast arg from string to integer
# float(arg) is used to cast to float, bool(arg) to boolean

print(type(year_of_dob)) # returns string only since we haven't updated the type of "year_of_dob" variable

year_of_dob = int(year_of_dob)
print(type(year_of_dob)) # returns int now :P

print(diff)
