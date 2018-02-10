def dectobin(dec):
    temp = []
    result = ''
    while dec:
        yushu = dec % 2
        dec = dec // 2
        temp.append(yushu)


    while temp:
        result  += str(temp.pop())

    return result
