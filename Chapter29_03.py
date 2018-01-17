# -*- coding: UTF-8 -*-
file_name = input('请输入要打开的文件(record.txt):')
number = int(input('请输入需要显示该文件的前几行:'))
line_str = []
f = open(file_name, encoding='UTF-8')
for each_line in f:
    line_str.append(each_line)

print("文件%s的前%d的内容如下:" % (file_name, number))

for i in range(number):
    print(line_str[i])
