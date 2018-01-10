def dd(x):
    list1 = []
    if x == 1:
        result = 1
    elif x == 2:
        result = 1
    else:
        list1 = [1,1]
        for i in range(3,x+1):
            result = list1[i-3] + list1[i-2]
            list1.append(result)
    return result
def dg(x):
    if x == 1:
        result = 1
    elif x == 2:
        result =1
    else:
        result = dg(x-2)+dg(x-1)
    return result

number = int(input("请输入斐波那契数列的数字:"))
print(dd(number))
print(dg(number))
