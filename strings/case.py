# Case
mixed = 'Python for Beginners'
uppercase = mixed.upper()
print(mixed) # existing mixed doesnt change since strings are immutable
print(uppercase)
lowercase = mixed.lower()
print(lowercase)

# Find
print(mixed.find('y')) # finds and returns the index of the first occurence of the character passed. In this case, it returns 1
print(mixed.find('Begin')) # returns 11

# Replace
text = 'Helloworld for beginners' # Jelloworld for beginners
replaced = text.replace('H', 'J')
print(replaced)
replace_v2 = text.replace('Hello', 'Hi') # Hiworld for beginners
print(replace_v2)

# Contains (or) in operator
checker_text = 'Helloworld'
print(checker_text.__contains__('Hello'))
print('Hello' in checker_text)
