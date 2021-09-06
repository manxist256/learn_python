lix = [1, 2, 3, 10, 2, -1, 1, 9, 20, 3, 1]

# 1. traditional way
maximum = -1000

for x in lix:
    if maximum < x:
        maximum = x

print(maximum)


# 2. build in function way
print(max(lix))