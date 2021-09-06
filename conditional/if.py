# change below 2 values to modify if evaluation
# If both is true,  is_hot is evaluated first as per business usecase
is_hot = True
is_cold = True

if is_hot:
    print("It's hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's cold day")
    print("Wear warm clothers")
else:
    print("It's a lovely day")
