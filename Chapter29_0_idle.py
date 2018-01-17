file_name = input('请输入文件名:')
content = input("请输入内容【单独输入':w'保存退出】:")
file_name_all = file_name + '.txt'
f = open(file_name_all, 'w')
content_str = []
for each_line in content:
    if each_line != ':w':
        content_str.append(each_line)
    else:
        f.close()
