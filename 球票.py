def calc_queue(m, n):
    if n == 0:
        queue = 1
    elif n > m:
        queue = 0
    else:
        queue = calc_queue(m, n-1) + calc_queue(m-1, n)
    return queue


a = calc_queue(500, 400)
print(a)