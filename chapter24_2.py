'''
def guess(x):
    global old
    if x == 1:
        None

    else:
        old = guess(x-1) + 2
        
    return old
old = 10
print(guess(5))
'''
def guess(n):
    if n == 1:
        return 10
    else:
        return guess(n-1) + 2
print(guess(5))
