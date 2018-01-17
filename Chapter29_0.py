# -*- coding: UTF-8 -*-
import sys
file_name = input('请输入文件名:')
print("请输入内容【单独输入':w'保存退出】:")
file_content = sys.stdin
file_name_all = file_name + '.txt'
f = open(file_name_all, 'w')
content_1 = []
for each_line in file_content:
    if each_line != ':w\n':
        content_1.append(each_line)
        print(content_1)
    else:
        f.writelines(content_1)
        f.close()



