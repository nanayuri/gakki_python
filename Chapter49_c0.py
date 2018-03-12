def myRev(x):
    x_len = len(x)
    while x_len:
        yield x[x_len-1]
        x_len -= 1


for i in myRev("FishC"):
    print(i, end='')
