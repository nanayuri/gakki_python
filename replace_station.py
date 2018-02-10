import os
import sys

dict1 = {'RSST070': 'AL One A'}
print(dict1['RSST070'])
tar_path = 'D:\\Doha_svg'
list1 = list(os.walk(tar_path))[0][2]
print(list1)

for each in list1:

    each = tar_path + '\\' + each
    print(each)
    file_svg = open(each, encoding='UTF-8')
    lines = file_svg.read()
    lines = lines.replace('AIRPORT', dict1['RSST070'])
    file_svg_w = open(each, 'w', encoding='UTF-8')
    file_svg_w.write(lines)
    file_svg_w.close()
    file_svg.close()


