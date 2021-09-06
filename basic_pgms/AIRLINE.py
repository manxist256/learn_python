t = int(input())
while t > 0:
    inputs = input().split(' ')
    a = int(inputs[0])
    b = int(inputs[1])
    c = int(inputs[2])
    d = int(inputs[3])
    e = int(inputs[4])
    if (a+b <= d and c <= e) or (a+c <= d and b <= e) or (b+c <= d and a <= e):
        print("YES")
    else:
        print("NO")
    t = t - 1
