def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return str(total)


total_str = ''
for num in range(1, 51):
    total_str += factorial(num)
len_str = len(total_str)
row_num = len_str // 40 + 1

for each_row in range(1, row_num + 1):
    str_final = total_str[40 * each_row - 40 :40 * each_row]
    print('(' + ('%2s' % str(each_row)) + ')' + str_final)

