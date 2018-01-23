# -*- coding: UTF-8 -*-
import os
key_word = input('请输入关键字:')
file_con = input('请问是否需要打印关键字【%s】在文件中的具体位置:' % key_word)
if file_con.lower() == 'yes':
    list1 = list(os.walk(os.getcwd()))
    length = len(list1)
    list_index = []
    for i in range(length):
        list_file = list1[i][2]
        list_dir = list1[i][0]

        for each in list_file:
            if len(each.split('.')) != 2:
                continue
            (file_name, file_type) = each.split('.')
            # print(file_type)
            if file_type == 'txt':
                file_name = list_dir + '\\' + each
                fr = open(file_name, encoding='UTF-8')
                # print(file_name)
                lines = fr.readlines()
                # print(lines)
                lin_num = 1
                for each_line in lines:
                    # print(each_line)
                    if key_word in each_line:
                        print('在文件%s中找到关键字%s:' % (file_name, key_word))
                        break

                for j in lines:
                    # print(each_line1)

                    if j.find(key_word) != -1:
                        # print('111111')
                        list_index.append(j.find(key_word)+1)

                    if len(list_index) != 0:
                        print('关键字出现在第%d行，第%s个位置' % (lin_num, list_index))
                    list_index = []
                    lin_num += 1
                fr.close()





