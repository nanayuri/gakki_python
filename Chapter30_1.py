import os
cur_dir = os.getcwd()
list1 = list(os.listdir(cur_dir))
print(list1)
for each in list1:
    if os.path.isfile(each):
        file_size = os.path.getsize(each)
        print('%s【%sBytes】' % (each, file_size))

