import os
image_cat = ['BACS', 'PHE', 'VHTS']
dict2 = {'BACS': 'Bacs', 'PHE': 'Phe', 'VHTS': 'VHTS'}
out_des = 'Z:\\git_depots\\cfg\\occ\\model\\metaconf\\proj\\ImageProject_ISCS\\svg-images\\DOHHK\\STA\\Bacs\\DOH\\STA\\'
for each_cat in image_cat:
    sour_dir = 'D:\\Doha\\From HK\\20180208\\New_SummaryScript\\' + each_cat
    temp_file1 = 'D:\\Doha\\From HK\\20180208\\New_SummaryScript\\Summary_Background_template_' + each_cat + '_1.svg'
    temp_file2 = 'D:\\Doha\\From HK\\20180208\\New_SummaryScript\\Summary_Background_template_' + each_cat + '_2.svg'
    list1 = list(os.walk(sour_dir))[0][2]
    str_add = ''
    dict1 = {'RNST050': 'Al Qassar', 'RSST010': 'Al Doha Al Jadeeda', 'RSST030': 'Al Matar', 'RSST040': 'Oqba Ibn Nafie', 'RSST070': 'AL Wakra', 'RNST010': 'Al Bidda', 'RNST030': 'Corniche', 'RNST040': 'Doha Exhibition & Convention Centre', 'RNST060': 'Katara', 'RNST070': 'Legtaifiya', 'RNST020': 'West Bay', 'RNST090': 'Lusail', 'RNST080': 'Qatar University', 'GSST010': 'Al Mansoura', 'RSST020': 'Umm Ghuwailina', 	'RSST050': 'Economic Zone', 'RSST060': 'Ras Bu Fontas', 'UCST000': 'Msheireb', 'REST020': 'Hamad International Airport'}

    for each in list1:
        each = sour_dir + '\\' + each
        file_name = os.path.basename(each)
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
            f_temp1 = open(temp_file1)
            f_temp2 = open(temp_file2)
            # output to local
            f_temp_final = open(temp_file1.replace('template_' + each_cat + '_1', sta_code + '_' + each_cat), 'w')
            # output to VM cfg repository

            f_temp_final = open(temp_vm, 'w')
            content1 = f_temp1.read()
            content1 = content1.replace('Hamad International Airport', dict1[sta_code])
            content1 = content1.replace('REST020', sta_code)
            content2 = f_temp2.read()
            f_temp_final.write(content1 + str_line + content2)
            f_temp_final.close()
            f_temp1.close()
            f_temp2.close()
