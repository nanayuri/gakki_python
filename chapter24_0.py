
def tobin(n):
    global str1
    a = n // 2
    b = n % 2
    if a == 0:
        str1 += str(b)
    else:
        
        str1 += str(b)
        tobin(a)
    return str1[::-1]
str1 = ''               
numb = int(input("请输入需要转化为二进制的十进制数:"))
print(tobin(numb))
