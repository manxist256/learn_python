t = int(input())
while t > 0:
    inputs = input().split(' ')
    a = int(inputs[0])
    b = int(inputs[1])
    c = int(inputs[2])
    binarys = input()
    cnt = 0
    for x in binarys:
        if x == '0':
            cnt += b
        else:
            cnt += c
    print(cnt)
    t = t - 1
