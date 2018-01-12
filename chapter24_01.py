
def tobin(n):
    str1 = ''
    a = n // 2
    b = n % 2
    if n:
        
       
        str1 = tobin(a)
        return str1 + str(b)
    else :
        return str1
              
numb = int(input("请输入需要转化为二进制的十进制数:"))
print(tobin(numb))
