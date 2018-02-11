import os
import sys

dict1 = {'RNST050': 'Al Qassar', 'RSST010': 'Al Doha Al Jadeeda', 'RSST030': 'Al Matar', 'RSST040': 'Oqba Ibn Nafie', 'RSST070': 'AL Wakra', 'RNST010': 'Al Bidda', 'RNST030': 'Corniche', 'RNST040': 'Doha Exhibition & Convention Centre', 'RNST060': 'Katara', 'RNST070': 'Legtaifiya', 'RNST020': 'West Bay', 'RNST090': 'Lusail', 'RNST080': 'Qatar University', 'GSST010': 'Al Mansoura', 'RSST020': 'Umm Ghuwailina', 	'RSST050': 'Economic Zone', 'RSST060': 'Ras Bu Fontas', 'UCST000': 'Msheireb', 'REST020': 'Hamad International Airport'}
print(dict1['RSST070'])
tar_path = 'C:\\Users\\zhaichunmei\\Documents\\GitHub\\gakki_python\\Doha'
list1 = list(os.walk(tar_path))[0][2]
print(list1)

for each in list1:

    each = tar_path + '\\' + each
    file_name = os.path.basename(each)
    sta_code = file_name[19:26]
    file_svg = open(each, encoding='UTF-8')
    lines = file_svg.read()
    lines = lines.replace('Hamad International Airport', dict1[sta_code])
    lines = lines.replace('REST020', sta_code)
    file_svg_w = open(each.replace('.svg', '_Bacs.svg'), 'w')
    file_svg_w.write(lines)
    file_svg_w.close()
    file_svg.close()


