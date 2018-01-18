# -*- coding: UTF-8 -*-
file_name = input('请输入文件名:')
file_word = input('请输入需要替换的单词或字符:')
file_new_word = input('请输入新的单词或字符:')
list_word = []
fr = open(file_name, encoding='UTF-8')
lines = fr.readlines()
num = 0
for i in lines:
    if i.find(file_word) != -1:
        num += 1
print('文件%s中共有%d个【%s】' %(file_name, num, file_word))
print('您确定要把所有的【%s】替换为【%s】吗?' %(file_word, file_new_word))
judge = input('【YES/NO】:\n')
if judge.lower() == 'yes':
    fw = open(file_name, 'w', encoding='UTF-8')
    for i in lines:
        fw.write(i.replace(file_word, file_new_word))
    fw.close()
fr.close()



