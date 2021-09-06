first = 'John'
last = 'Smith'
message = first + ' [' + last + ']' + ' is a play boy'
# You can see the problem that the above format is complex in nature and affects readability
# So, there is a better approach
# It is same as String.format("%s [%s] is a play boy", first, last)
print(message)

# Let's see the same in python
message = f'{first} [{last}] is a play boy'
print(message)
