def get_digits(x):
    lens = len(str(x))
    a = x // 10
    b = x % 10
    global list1
    if a == 0:
        list1.append(b)
    else:
        get_digits(a)
        list1.append(b)
        
    return list1
list1 = []
number = int(input("请输入一个数字："))
print(get_digits(number))
