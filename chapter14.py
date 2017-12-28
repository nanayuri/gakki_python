import string
pswd = input("请输入需要检查的密码组合:")
lowsec = "您的密码安全级别评定为：低"
highsec = "您的密码安全级别评定为：高"
midsec = "您的密码安全级别评定为：中"
hint = "请按以下方式提升您的密码安全级别:\n\t1.密码必须由数字,字母及特殊字符三种组合\n\t2.密码只能由字母开头\n\t3.密码长度不能低于16位"
str1 = string.ascii_letters
num1 = string.digits
char1 = string.punctuation
length = len(pswd)
flag_con = 0

if length < 8:
    flag_len = 1
elif 8 < length < 16:
    flag_len = 2
else:
    flag_len = 3

for each in pswd:
    if each in char1:
        flag_con +=1
        break

for each in pswd:
    if each in num1:
        flag_con +=1
        break

for each in pswd:
    if each in str1:
        flag_con +=1
        break
while 1:
    if flag_len ==1 or flag_con ==1:
        print(lowsec)
    elif flag_len ==3 and flag_con ==3 and (pswd[0].isalpha() == True):
        print(highsec)
        break
    else:
        print(midsec)
    print(hint)




 
