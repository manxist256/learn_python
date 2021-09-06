# problem 1
temperature = 30

if temperature > 25:
    print("Hot day")
elif temperature == 0:
    print("Its zero degree!")
elif temperature < 15:
    print("Cold day")
elif temperature >= 15:
    print("Moderate day")


if temperature != 30:
    print("Temperature is not 30 today")

# problem 2
name = "India"

if len(name) < 3:
    print("Name can't be less than 3 characters")
elif len(name) > 50:
    print("Name cannot exceed 50 characters")
else:
    print("Good name!")