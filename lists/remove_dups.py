dups = [1, 3, 5, 1, 7, 7, 8, 9, 1, 10, 1, -1, 2, 2, 3, 10, 9, -1, -2, 0, 0, 20, 1, 12]

without_dups = []

for val in dups:
    if val not in without_dups:
        without_dups.append(val)

print(without_dups)