t = int(input())
while t > 0:
    N = int(input())
    inputs = input().split(' ')
    even = N // 2
    odd = N // 2
    if N % 2 == 1:
        odd = odd + 1
    ceven = 0
    codd = 0
    for i in inputs:
        if int(i) % 2 == 0:
            ceven = ceven + 1
        else:
            codd = codd +1
    print(min(ceven, odd) + min(codd, even))
    t = t - 1
