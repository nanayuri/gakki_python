def mysum(*args):
    sum = 0
    str1 = ''
    for each in args:
        sum += each
        if each >= 0:
            str1 += '+' + str(each)
        else:
            str1 += str(each)
    if str1[0] == '+':
        str1 = str1[1:len(str1)]
    return sum,str1


p = mysum(-1,2,3,-2,5,0)
print(p[1] + '=' + str(p[0]))

