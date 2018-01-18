import os
cur_dir = os.getcwd()
list1 = list(os.walk(cur_dir))
list_file_pix = []
list_file_num = []
num = 0
for each in list1[0][2]:
    pix = each.split('.')[1]
    if pix not in list_file_pix:
        list_file_pix.append(pix)

for each in list_file_pix:
    for each_pix in list1[0][2]:
        if each_pix.split('.')[1] == each:
            num += 1
    list_file_num.append(num)
    num = 0
num_folder = 0
for each in list1[0][1]:
    num_folder += 1
list_file_num.append(num_folder)
i = 0
list_file_pix.append('文件夹')
for each in list_file_pix:
    print('该文件夹下共有类型【%s】的文件%s个' %(list_file_pix[i], list_file_num[i]))
    i += 1

