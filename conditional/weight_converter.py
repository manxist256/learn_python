weight = int(input())
type = input("(L)bs or (K)g: ")
if type.upper() == "L":
    print(f"You are {0.453592 * weight} kgs")
else:
    print(f"You are {2.20462 * weight} pounds")