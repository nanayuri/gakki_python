def zhishu(x):
    result = True
    for i in range(2, x):
        if x % i == 0:
            result = False
            break
    return result


if __name__ == "__main__":
    for num in range(2, 100):
        dec = num // 10
        car = divmod(num, 10)[1]
        if zhishu(num) is True and zhishu(dec) is True and zhishu(car) is True:
            print(num)
