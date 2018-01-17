# -*- coding: UTF-8 -*-
file_name = input('请输入要打开的文件(record.txt):')
lines_org = input('请输入需要显示的行数【格式如13:21或:21或21:】:')
lines = list(lines_org)
f = open(file_name, encoding='UTF-8')
line_str = []
index = lines_org.find(':')
length = len(lines)
j = 0
print(index)
print(length)
for each_line in f:
    line_str.append(each_line)
    j += 1
if index == 0:
    if length == 1:
        print("文件%s的全文内容如下:" % file_name)
        for i in range(j):
            print(line_str[i])
    else:
        # 从首个字符开始计算到输入字符
        print("文件%s从开始到第%s行的内容如下:" % (file_name, ''.join(lines[1:])))
        for i in range(int(''.join(lines[1:]))):
            print(line_str[i])
elif index+1 == length:
    # 从输入字符计算到末位
    print("文件%s从第%s行到末尾的内容如下:" % (file_name, ''.join(lines[:(length-1)])))
    for i in range(int(''.join(lines[:(length-1)]))-1, j):
        print(line_str[i])


else:
    # 输入字符之间的字符
    print("文件%s从第%s行到第%s行的内容如下:" % (file_name, ''.join(lines[:index]), ''.join(lines[(index+1):j])))
    for i in range(int(''.join(lines[:index]))-1, int(''.join(lines[(index+1):j]))):
        print(line_str[i])

f.close()




