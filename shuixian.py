for i in range(100,100000000):
    a = list(str(i))
    c = 0
    for d in range(len(a)):
        c += int(a[d])**len(a)
    if c == i:
        print(i)
