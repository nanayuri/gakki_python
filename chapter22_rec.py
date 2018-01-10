def rec(n):
    if n == 1:
        return 1
    else:
        return n * rec(n-1)
number = int(input("请输入一个正整数:"))
result = rec(number)
print("%d 的阶乘是 : %d" % (number,result))
