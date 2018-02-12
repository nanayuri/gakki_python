import openpyxl
import os

cur_dir = os.getcwd()
os.chdir(cur_dir)
# sta_list = ['RNST050', 'RSST010', 'RSST030', 'RSST040',	'RSST070', 'RNST010', 'RNST030', 'RNST040',	'RNST060', 'RNST070', 'RNST020', 'RNST090',	'RNST080', 'GSST010', 'RSST020', 'RSST050', 'RSST060', 'UCST000', 'REST020']
sta_list = []
file_path = cur_dir
file_name = 'station_code.xlsx'
sys_name = 'PHE'
image_name = '_' + sys_name + '_Auto_gen'
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


if not os.path.exists(cur_dir + '\\' + sys_name):
    os.mkdir(sys_name)

wb = openpyxl.load_workbook(file_sour)
ws = wb['csv']

total_row = ws.max_row + 1

for i in range(2, total_row):
    # 同一个车站，设备类型类相同
    if ws['A' + str(i)].value == ws['A' + str(i - 1)].value and ws['D'+ str(i)].value[0:11] == ws['D' + str(i - 1)].value[0:11]:
        if ws['B' + str(i - 1)].value + 550 < 6821 and ws['C' + str(i - 1)].value < 2836:
            ws['B' + str(i)].value = ws['B' + str(i - 1)].value + 550
            ws['C' + str(i)].value = ws['C' + str(i - 1)].value
            ws['H' + str(i)].value = ws['D' + str(i)].value[5:12]

        elif ws['B' + str(i - 1)].value + 550 > 6821 and ws['C' + str(i - 1)].value < 2536:
            ws['B' + str(i)].value = 220
            ws['C' + str(i)].value = ws['C' + str(i - 1)].value + 300
            ws['H' + str(i)].value = ws['D' + str(i)].value[5:12]

        elif ws['B' + str(i - 1)].value + 550 < 6821 and ws['C' + str(i - 1)].value > 2834:
            ws['B' + str(i)].value = 220
            ws['H' + str(i)].value = ws['D' + str(i)].value[5:12] + '_1'
            ws['C' + str(i)].value = 735

        elif ws['B' + str(i - 1)].value + 550 > 6821 and ws['C' + str(i - 1)].value > 2834:
            ws['B' + str(i)].value = 220
            ws['H' + str(i)].value = ws['D' + str(i)].value[5:12] + '_1'
            ws['C' + str(i)].value = 735

    # 同一个车站，但设备类型不同
    elif ws['A' + str(i)].value != ws['A' + str(i - 1)].value and ws['D' + str(i)].value[0:11] == ws['D' + str(i - 1)].value[0:11]:
        if ws['C' + str(i - 1)].value < 2536:
            ws['B' + str(i)].value = 220
            ws['C' + str(i)].value = ws['C' + str(i - 1)].value + 300
            ws['H' + str(i)].value = ws['D' + str(i)].value[5:12]
        else:
            ws['B' + str(i)].value = 220
            ws['C' + str(i)].value = 735
            ws['H' + str(i)].value = ws['D' + str(i)].value[5:12] + '_1'

    # 不同车站
    elif ws['D' + str(i)].value[0:11] != ws['D' + str(i - 1)].value[0:11]:
        ws['B' + str(i)].value = 220
        ws['C' + str(i)].value = 735
        ws['H' + str(i)].value = ws['D' + str(i)].value[5:12]

    elif ws['C' + str(i - 1)].value > 2834:
        ws['H' + str(i)].value = ws['D' + str(i)].value[5:12] + '_1'
        ws['C' + str(i)].value = 735

    elif ws['A' + str(i)].value == '':
        ws['H' + str(i)].value = ws['H' + str(i - 1)].value

ws['H1'].value = ws['D1'].value[5:12]


for j in range(2, total_row):
    try:
        if (ws['H' + str(j - 1)].value[7:10] == '_1') and (ws['H' + str(j)].value == ws['H' + str(j - 1)].value[0:7]):
            ws['H' + str(j)].value = ws['H' + str(j - 1)].value
    except TypeError:
        print('在第%d行出现问题' %j)
        pass
    if ws['H' + str(j)].value not in sta_list:
        sta_list.append(ws['H' + str(j)].value)

os.chdir(cur_dir + '\\' + sys_name)

for each_file in os.getcwd():
    os.remove(each_file)

for each_sta in sta_list:
    for each_rows in ws.rows:
        if each_rows[7].value == each_sta:
            long_str += a + each_rows[0].value + b1 + str(each_rows[1].value) + ' ' + str(each_rows[2].value) + b2 + each_rows[3].value + c + each_rows[4].value + d + each_rows[5].value + e + each_rows[6].value + r'" xlink:actuate="onLoad"/>' + '\n'

    with open(str(each_sta) + image_name + '.svg', 'w') as f:
        f.write(long_str)
    long_str = ''


wb.save(file_n_sour)





