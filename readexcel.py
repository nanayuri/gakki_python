# Project: Doha
# Written by: Huang Chao
# Date: 2018-02-13
# .svg image files auto generation

import openpyxl
import os

cur_dir = os.getcwd()
os.chdir(cur_dir)
# sta_list = ['RNST050', 'RSST010', 'RSST030', 'RSST040',	'RSST070', 'RNST010', 'RNST030', 'RNST040',	'RNST060', 'RNST070', 'RNST020', 'RNST090',	'RNST080', 'GSST010', 'RSST020', 'RSST050', 'RSST060', 'UCST000', 'REST020']
sta_list = []
file_path = cur_dir
file_name = 'image_autogen.xlsx'
sys_name_list = ['VHTS', 'BACS', 'PHE']
# sys_name = 'VHTS'
# sys_name = 'BACS'
# sys_name = 'PHE'

file_sour = file_path + '\\' + file_name
file_n_sour = file_sour.replace('.xlsx', '_update.xlsx')
station_name = ''
lines = []
long_str = ''
a = r'  <use mc:refType="symbol" mc:navigationId="" mc:layerName="'
b1 = r'" mc:navImageExtent="" transform="matrix(1 0 0 1 '
b2 = r')" mc:dbPath="'
c = r'" xlink:show="embed" xlink:type="simple" mc:navImageId="" mc:protoId="'
d = r'" mc:hvEntityId="'
e = r'" xlink:href="#'
f = r'" xlink:actuate="onLoad"/>'

image_cat = ['BACS', 'PHE', 'VHTS']
dict2 = {'BACS': 'Bacs', 'PHE': 'Phe', 'VHTS': 'VHTS'}
out_des = 'Z:\\git_depots\\cfg\\occ\\model\\metaconf\\proj\\ImageProject_ISCS\\svg-images\\DOHHK\\STA\\Bacs\\DOH\\STA\\'


def upd_col_h(x):
    # 更新h列
    try:
        if ws['H' + str(x - 1)].value[-2:-1] == '_':
            ws['H' + str(x)].value = ws['H' + str(x - 1)].value
        return ws['H' + str(x)].value
    except TypeError:
        print('第%d行有错' %x)


def add_col_h(x):
    # 增加一列，为了判断是否需要增加图
    z = 0
    s1 = ws['H' + str(x - 1)].value[-2:]
    if s1[0] == '_':
        z = int(s1[1]) + 1
    else:
        z = 1
    ws['H' + str(x)].value = ws['D' + str(x)].value[5:12] + '_' + str(z)
    return ws['H' + str(x)].value


for sys_name in sys_name_list:
    sta_list = []
    image_name = '_' + sys_name + '_Auto_gen'
    if not os.path.exists(cur_dir + '\\' + sys_name):
        os.mkdir(sys_name)

    wb = openpyxl.load_workbook(file_sour)
    ws = wb[sys_name]

    total_row = ws.max_row + 1

    ws['H1'].value = ws['D1'].value[5:12]

    for i in range(2, total_row):
        # 同一个车站，设备类型类相同
        if ws['A' + str(i)].value == ws['A' + str(i - 1)].value and ws['D' + str(i)].value[0:11] == ws['D' + str(
                i - 1)].value[0:11]:
            if ws['B' + str(i - 1)].value + 550 < 6821 and ws['C' + str(i - 1)].value < 2836:
                ws['B' + str(i)].value = ws['B' + str(i - 1)].value + 550
                ws['C' + str(i)].value = ws['C' + str(i - 1)].value
                ws['H' + str(i)].value = ws['D' + str(i)].value[5:12]
                ws['H' + str(i)].value = upd_col_h(i)

            elif ws['B' + str(i - 1)].value + 550 > 6821 and ws['C' + str(i - 1)].value < 2536:
                ws['B' + str(i)].value = 220
                ws['C' + str(i)].value = ws['C' + str(i - 1)].value + 300
                ws['H' + str(i)].value = ws['D' + str(i)].value[5:12]
                ws['H' + str(i)].value = upd_col_h(i)

            elif ws['B' + str(i - 1)].value + 550 < 6821 and ws['C' + str(i - 1)].value > 2834:
                ws['B' + str(i)].value = 220
                # ws['H' + str(i)].value = ws['D' + str(i)].value[5:12] + '_1'
                ws['H' + str(i)].value = add_col_h(i)
                ws['C' + str(i)].value = 735

            elif ws['B' + str(i - 1)].value + 550 > 6821 and ws['C' + str(i - 1)].value > 2834:
                ws['B' + str(i)].value = 220
                # ws['H' + str(i)].value = ws['D' + str(i)].value[5:12] + '_1'
                ws['H' + str(i)].value = add_col_h(i)
                ws['C' + str(i)].value = 735

        # 同一个车站，但设备类型不同
        elif ws['A' + str(i)].value != ws['A' + str(i - 1)].value and ws['D' + str(i)].value[0:11] == ws['D' + str(
                i - 1)].value[0:11]:
            if ws['C' + str(i - 1)].value < 2536:
                ws['B' + str(i)].value = 220
                ws['C' + str(i)].value = ws['C' + str(i - 1)].value + 300
                ws['H' + str(i)].value = ws['D' + str(i)].value[5:12]
                ws['H' + str(i)].value = upd_col_h(i)
            else:
                ws['B' + str(i)].value = 220
                ws['C' + str(i)].value = 735
                # ws['H' + str(i)].value = ws['D' + str(i)].value[5:12] + '_1'
                ws['H' + str(i)].value = add_col_h(i)

        # 不同车站
        elif ws['D' + str(i)].value[0:11] != ws['D' + str(i - 1)].value[0:11]:
            ws['B' + str(i)].value = 220
            ws['C' + str(i)].value = 735
            ws['H' + str(i)].value = ws['D' + str(i)].value[5:12]

        elif ws['C' + str(i - 1)].value > 2834:
            # ws['H' + str(i)].value = ws['D' + str(i)].value[5:12] + '_1'
            ws['H' + str(i)].value = add_col_h(i)
            ws['C' + str(i)].value = 735

        elif ws['A' + str(i)].value == '':
            ws['H' + str(i)].value = ws['H' + str(i - 1)].value

        if ws['H' + str(i)].value not in sta_list:
            sta_list.append(ws['H' + str(i)].value)

    os.chdir(cur_dir + '\\' + sys_name)

    for each_file in os.listdir(os.getcwd()):
        os.remove(each_file)

    for each_sta in sta_list:
        for each_rows in ws.rows:
            if each_rows[7].value == each_sta:
                long_str += a + each_rows[0].value + b1 + str(each_rows[1].value) + ' ' + str(each_rows[2].value) + b2 + each_rows[3].value + c + each_rows[4].value + d + each_rows[5].value + e + each_rows[6].value + r'" xlink:actuate="onLoad"/>' + '\n'

        with open(str(each_sta) + image_name + '.svg', 'w') as f:
            f.write(long_str)
        long_str = ''
    os.chdir(cur_dir)

wb.save(file_n_sour)
os.chdir(cur_dir)

if not os.path.exists(cur_dir + '\\' + 'output_files'):
    os.mkdir('output_files')
f_out_dir = cur_dir + '\\' + 'output_files'
os.chdir(f_out_dir)
for each_file in os.listdir(cur_dir + '\\' + 'output_files'):
    os.remove(each_file)

for each_cat in sys_name_list:
    sour_dir = cur_dir + '\\' + each_cat
    temp_file1 = cur_dir + '\\Template\\Summary_Background_template_' + each_cat + '_1.svg'
    temp_file2 = cur_dir + '\\Template\\Summary_Background_template_' + each_cat + '_2.svg'
    list1 = list(os.walk(sour_dir))[0][2]
    str_add = ''
    dict1 = {'RNST050': 'Al Qassar', 'RSST010': 'Al Doha Al Jadeeda', 'RSST030': 'Al Matar', 'RSST040': 'Oqba Ibn Nafie', 'RSST070': 'AL Wakra', 'RNST010': 'Al Bidda', 'RNST030': 'Corniche', 'RNST040': 'Doha Exhibition & Convention Centre', 'RNST060': 'Katara', 'RNST070': 'Legtaifiya', 'RNST020': 'West Bay', 'RNST090': 'Lusail', 'RNST080': 'Qatar University', 'GSST010': 'Al Mansoura', 'RSST020': 'Umm Ghuwailina', 	'RSST050': 'Economic Zone', 'RSST060': 'Ras Bu Fontas', 'UCST000': 'Msheireb', 'REST020': 'Hamad International Airport'}

    for each in list1:
        each = sour_dir + '\\' + each
        file_name = os.path.basename(each)
        if file_name.find('_1') is not -1:
            sta_code = file_name[0:9]
        else:
            sta_code = file_name[0:7]
        str_line = ''
        temp_vm_fn = '\\DOH_STA_Bacs_DOH_STA_' + sta_code + '_' + dict2[each_cat] + '_Summary.svg'
        temp_vm = out_des + sta_code + '\\' + dict2[each_cat] + temp_vm_fn
        with open(each) as f_sour:
            lines = f_sour.readlines()
            if lines[-1].find('dbPath=""') != -1:
                lines = lines[0:-1]

            for each_line in lines:
                str_line += each_line

            with open(temp_file1) as f_temp1, open(temp_file2) as f_temp2:
                os.chdir(cur_dir)

                # output to local
                with open(f_out_dir + '\\' + 'Summary_Background_' + sta_code+ '_' + each_cat + '.svg', 'w') as f_temp_final:
                # output to VM cfg repository
                # with open (temp_vm, 'w') as f_temp_final:

                    content1 = f_temp1.read()
                    content1 = content1.replace('Hamad International Airport', dict1[sta_code[0:7]])
                    content1 = content1.replace('REST020', sta_code[0:7])
                    content2 = f_temp2.read()
                    f_temp_final.write(content1 + str_line + content2)
                    os.chdir(cur_dir)
