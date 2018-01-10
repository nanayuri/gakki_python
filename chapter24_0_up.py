
def tobin(n,w):
    global str1
    a = n // w
    b = n % w
    if a == 0:
        str1 += str(b)
    else:
        
        str1 += str(b)
        tobin(a,w)
    return str1[::-1]
str1 = ''               
numb = int(input("请输入需要转化为二进制的十进制数:"))
numb1 = int(input("请输入需要转化为多少进制进制数:"))
print(tobin(numb,numb1))
