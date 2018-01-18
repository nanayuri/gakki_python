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

        for line_num, each in enumerate(list_file):
            if len(each.split('.')) != 2:
                continue
            (file_name, file_type) = each.split('.')
            if file_type == 'txt':
                file_name = list_dir + '\\' + each
                fr = open(file_name, encoding='UTF-8')
                print(file_name)
                lines = fr.readlines()
                # print(lines)
                for each_line in fr:
                    if key_word in each_line:
                        print('在文件%s中找到关键字%s:' % (file_name, key_word))

                for j in lines:
                    if j.find(key_word) != -1:
                        list_index.append(j.find(key_word)+1)
                if len(list_index) != 0:
                    print('关键字出现在第%d行，第%s个位置' %(line_num+1, list_index))
                list_index = []
                line_num = 0
fr.close()



