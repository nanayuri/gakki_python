def fibonacci(n):
    s = ''
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
        s += str(a)
    return s


def find_first_fibon(fib_n):
    str1 = fib_n
    isFind = False
    while not isFind:
        for i in range(len(str1)):
            fib_set = set(str1[i:i + 10])
            if len(fib_set) == 10:
                print(fib_set)
                print(str1)
                isFind = True



find_first_fibon(fibonacci(400))



