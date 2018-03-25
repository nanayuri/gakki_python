num1 = 0
num2 = 0

for i in range(3):
    str1 = ''
    if i == 1:
        num1 = 1
    if i == 2:
        num2 = 2
        str1 = str(num2) + '/' + str(num1)

    else:
        str1 += '+'
        num = num1 + num2
        num1 = num2
        num2 = num
        str1 += str(num2) + '/' + str(num1)
print(str1)
