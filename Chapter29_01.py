# -*- coding: UTF-8 -*-
file_name = input('请输入文件名:')
print("请输入内容【单独输入':w'保存退出】:")
file_content = input()
file_name_all = file_name + '.txt'
f = open(file_name_all, 'w')
content_1 = []
while file_content != ':w':
    file_content += '\n'
    content_1.append(file_content)
    file_content = input()

f.writelines(content_1)
f.close()

