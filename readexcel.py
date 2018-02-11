import openpyxl
sta_list = ['RNST050', 'RSST010', 'RSST030', 'RSST040',	'RSST070', 'RNST010', 'RNST030', 'RNST040',	'RNST060', 'RNST070', 'RNST020', 'RNST090',	'RNST080', 'GSST010', 'RSST020', 'RSST050', 'RSST060', 'UCST000', 'REST020']
wb = openpyxl.load_workbook(r"C:\Users\zhaichunmei\Documents\GitHub\gakki_python\station_code.xlsx")
ws = wb.get_sheet_by_name('csv')
station_name = ''
lines = []
long_str = ''
a = r'  <use mc:refType="symbol" mc:navigationId="" mc:layerName="'
b1 = r'" mc:navImageExtent="" transform="matrix(1 0 0 1 '
b2 = r')" mc:dbPath="'
c = r'" xlink:show="embed" xlink:type="simple" mc:navImageId="" mc:protoId="'
d = r'" mc:hvEntityId="'
e = r'" xlink:href="'
f = r'" xlink:actuate="onLoad"/>'

legal_x = [220, 6821]
legal_y = [735, 2836]


class Cord:
    def __init__(self):
        self.x = legal_x[0]
        self.y = legal_y[0]

    def add_svg(self):
        new_x = self.x + 550
        if new_x < legal_x[1]:
            self.x = new_x
        return self.x

    def add_class(self):
        new_y = self.y + 300
        if new_y < legal_y[1]:
            self.y = new_y
        return self.y

for i in range(2,200):
    if ws['A' + str(i)].value == ws['A' + str(i - 1)].value and ws['D'+ str(i)].value[0:11] == ws['D' + str(i - 1)].value[0:11]:
        if ws['B' + str(i - 1)].value + 550 < 6821 and ws['C' + str(i)].value < 2836:
            ws['B' + str(i)].value = ws['B' + str(i - 1)].value + 550
            ws['C' + str(i)].value = ws['C' + str(i - 1)].value

        elif ws['B' + str(i - 1)].value + 550 > 6821 and ws['C' + str(i)].value < 2836 and ws['A' + str(i)].value != ws['A' + str(i - 1)].value and ws['D' + str(i)].value[0:11] == ws['D' + str(i - 1)].value[0:11]:
            ws['B' + str(i)].value = 220
            ws['C' + str(i)].value = ws['C' + str(i - 1)].value + 300

        elif ws['A' + str(i)].value != ws['A' + str(i - 1)].value and ws['B' + str(i - 1)].value + 550 < 6821:
            ws['B' + str(i)].value = ws['B' + str(i - 1)].value + 550
            ws['C' + str(i)].value = ws['C' + str(i - 1)].value + 300

        elif ws['D' + str(i)].value[0:11] != ws['D' + str(i - 1)].value[0:11]:
            ws['B' + str(i)].value = 220
            ws['C' + str(i)].value = 735


for each_sta in sta_list:
    for each_rows in ws.rows:
        if each_rows[3].value[5:12] == each_sta:
            long_str += a + each_rows[0].value + b1 + ' ' + b2 + each_rows[3].value + each_rows[4].value + d + each_rows[5].value + e + each_rows[6].value + r'" xlink:actuate="onLoad"/>' + '\n'

    with open(each_sta + '.svg', 'w') as f:
        f.write(long_str)
    long_str = ''








