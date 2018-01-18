import os
tar_dir = input('请输入待查找的初始目录:')
tar_file = input('请输入需要查找的目标文件:')
list1 = list(os.walk(tar_dir))
length = len(list1)
for i in range(length):
    list_file = list1[i][2]
    list_dir = list1[i][0]
    for each in list_file:
        if each == tar_file:
            print(os.path.realpath(list_dir) + '\\' + tar_file)
