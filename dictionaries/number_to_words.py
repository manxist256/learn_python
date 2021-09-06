dict = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "😁" # ctrl + cmd + space
}

print(dict["1"])
print(dict.get("1"))

ph_num = input()

words = ""

for x in ph_num:
    words = words + dict.get(x, "!").lower() + " "

print(words)

