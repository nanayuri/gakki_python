file1 = input('请输入需要比较的头一个文件名:')
file2 = input('请输入需要比较的第二个文件名:')

f1 = open(file1)
f2 = open(file2)

file_word1 = []
file_word2 = []

for each_line in f1:
    file_word1.append(each_line)

for each_line in f2:
    file_word2.append(each_line)

if len(file_word1) > len(file_word2):
    for i in range(len(file_word2)):
        if file_word1[i] != file_word2[i]:
            print('第' + str(i+1) + '行不一样')

        i += 1
    for i in range(len(file_word2)+1, len(file_word1)+1):
        print('第' + str(i) + '行不一样')
elif len(file_word1) < len(file_word2):
    for i in range(len(file_word1)):
        if file_word2[i] != file_word1[i]:
            print('第' + str(i+1) + '行不一样')

        i += 1
    for i in range(len(file_word1) + 1, len(file_word2)+1):
        print('第' + str(i) + '行不一样')
else:
    for i in range(len(file_word1)):
        if file_word2[i] != file_word1[i]:
            print('第' + str(i+1) + '行不一样')

        i += 1
f1.close()
f2.close()
