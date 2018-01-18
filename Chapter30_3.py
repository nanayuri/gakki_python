import os
tar_dir = input('请输入待查找的目录:')
tar_file = input('请输入需要查找的目标文件类型:')
list1 = list(os.walk(tar_dir))
length = len(list1)
file_pt_list = []
for i in range(length):
    list_file = list1[i][2]
    list_dir = list1[i][0]
    for each in list_file:
        if len(each.split('.')) != 2:
            continue

        (file_name, file_type) = each.split('.')
        if file_type == tar_file:
            file_pt_list.append(os.path.realpath(list_dir) + '\\' + each + '\n')

fr = open('typeList.txt', 'w', encoding='UTF-8')
fr.writelines(file_pt_list)
fr.close()
