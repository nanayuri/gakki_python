import os
import re


def read_csv_file(*args):
    cur_dir = os.getcwd()
    tem_dir = cur_dir + '\\template'
    dci24 = ['dciPOW-CurProt', 'dciPOW-IoProtI', 'dciPOW-ITrip', 'dciPOW-LocUrgent']
    dci25 = ['dciPOW-PowIscs']
    dci26 = ['dciPOW-LVProt', 'dciPOW-OverCur']
    if args[0] == 'dci':
        class_file = tem_dir + '\\dci.xml'
        out_dir = cur_dir + '\\out'
        exist_dir = out_dir + '\\existed_point'
        exist_list = os.listdir(exist_dir)
        file_name = args[4] + '.xml'
        if args[4] in dci24:
            temp_file = tem_dir + '\\dci_temp24.xml'
        elif args[4] in dci25:
            temp_file = tem_dir + '\\dci_temp25.xml'
        elif args[4] in dci26:
            temp_file = tem_dir + '\\dci_temp26.xml'
        else:
            temp_file = tem_dir + '\\dci_temp.xml'
        if file_name in exist_list:
            class_file = exist_dir + '\\' + args[4] + '.xml'
            with open(class_file) as f_class1:
                content_class = f_class1.read()
        else:
            with open(class_file) as f_class:
                content_class = f_class.read()
                content_class = content_class.replace('file_name', args[4])
                content_class = content_class.replace('file_label', args[2])
        with open(temp_file) as f:
            content = f.read()
            # print(content.find('dci_alias'))
            # print(content)
            content = content.replace('dci_alias', args[1])
            content = content.replace('dci_label', args[2])
            content = content.replace('dci_pointname', args[3])
    elif args[0] == 'dac':
        temp_file = tem_dir + '\\dac_temp.xml'
        class_file = tem_dir + '\\dac.xml'
        with open(temp_file) as f:
            content = f.read()
            # print(content.find('dac_alias'))
            # print(content)
            content = content.replace('dac_alias', args[1])
            content = content.replace('ve_alias', args[2])
        with open(class_file) as f_class:
            content_class = f_class.read()
            content_class = content_class.replace('file_name', args[3])
    elif args[0] == 'dal':
        temp_file = tem_dir + '\\dal_temp.xml'
        class_file = tem_dir + '\\dal.xml'
        out_dir = cur_dir + '\\out'
        exist_dir = out_dir + '\\existed_point'
        exist_list = os.listdir(exist_dir)
        file_name = args[23] + '.xml'
        if file_name in exist_list:
            temp1_file = exist_dir + '\\' + args[23] + 'Instances.xml'
            class_file = exist_dir + '\\' + args[23] + '.xml'
            # class_file1 = tem_dir + '\\dal.xml'
            with open(class_file) as f_class:
                cont = f_class.readlines()[2]
                matchObj = re.match(r'(.*) numInstances="(.*?)" numPeriod_MT(.*)', cont, re.M)
                ins_num = int(matchObj.group(2))
                cont1 = cont.replace('num_ins', str(ins_num))
            with open(class_file) as f_class1:
                content_class = f_class1.read()
                content_class = content_class.replace(cont, cont1)
            with open(temp_file) as f:
                content = f.read()
                # print(content.find('dal_alias'))
                # print(content)
                cont_temp = re.findall(r'\bStructFieldValue.*StructFieldValue\b', content, re.DOTALL)
                content = content.replace('dal_alias', args[1])
                content = content.replace('ala_type', args[2])
                # print(cont_temp)
                str1 = ''
                for each in cont_temp:
                    str1 += each + '\n'

            with open(class_file) as f1:
                cot1 = f1.read()
                cont_org = re.findall(r'\bStructFieldDefaultValue.*StructFieldDefaultValue\b', cot1, re.DOTALL)
                # print(cont_org)
                str2 = ''
                for each in cont_org:
                    str2 += each + '\n'
            #print(str1, str2)
            #print(content.find(str1))

            content = content.replace(cont_temp[0], cont_org[0].replace('Default', '').replace('default', '').replace('Value=', 'value='))


        else:
            with open(class_file) as f_class:
                content_class = f_class.read()
                content_class = content_class.replace('file_name', args[23])
                content_class = content_class.replace('file_alclass', args[2])
                content_class = content_class.replace('bit0_value', args[3])
                content_class = content_class.replace('bit0_label', args[4])
                content_class = content_class.replace('bit0_state', args[5])
                content_class = content_class.replace('bit0_severity', args[6])
                content_class = content_class.replace('bit1_value', args[7])
                content_class = content_class.replace('bit1_label', args[8])
                content_class = content_class.replace('bit1_state', args[9])
                content_class = content_class.replace('bit1_severity', args[10])
                content_class = content_class.replace('bit2_value', args[11])
                content_class = content_class.replace('bit2_label', args[12])
                content_class = content_class.replace('bit2_state', args[13])
                content_class = content_class.replace('bit2_severity', args[14])
                content_class = content_class.replace('bit3_value', args[15])
                content_class = content_class.replace('bit3_label', args[16])
                content_class = content_class.replace('bit3_state', args[17])
                content_class = content_class.replace('bit3_severity', args[18])
                content_class = content_class.replace('bit4_value', args[19])
                content_class = content_class.replace('bit5_value', args[20])
                content_class = content_class.replace('bit6_value', args[21])
                content_class = content_class.replace('bit7_value', args[22])
            with open(temp_file) as f:
                content = f.read()
                # print(content.find('dal_alias'))
                # print(content)
                content = content.replace('dal_alias', args[1])
                content = content.replace('ala_type', args[2])
                content = content.replace('bit0_value', args[3])
                content = content.replace('bit0_label', args[4])
                content = content.replace('bit0_state', args[5])
                content = content.replace('bit0_severity', args[6])
                content = content.replace('bit1_value', args[7])
                content = content.replace('bit1_label', args[8])
                content = content.replace('bit1_state', args[9])
                content = content.replace('bit1_severity', args[10])
                content = content.replace('bit2_value', args[11])
                content = content.replace('bit2_label', args[12])
                content = content.replace('bit2_state', args[13])
                content = content.replace('bit2_severity', args[14])
                content = content.replace('bit3_value', args[15])
                content = content.replace('bit3_label', args[16])
                content = content.replace('bit3_state', args[17])
                content = content.replace('bit3_severity', args[18])
                content = content.replace('bit4_value', args[19])
                content = content.replace('bit5_value', args[20])
                content = content.replace('bit6_value', args[21])
                content = content.replace('bit7_value', args[22])

    elif args[0] == 'dfo':
        temp_file = tem_dir + '\\dfo_temp.xml'
        class_file = tem_dir + '\\dfo.xml'
        with open(temp_file) as f:
            content = f.read()
            print(content.find('dfo_alias'))
            # print(content)
            content = content.replace('dfo_alias', args[1])
        with open(class_file) as f_class:
            content_class = f_class.read()
            content_class = content_class.replace('file_name', args[2])

    elif args[0] == 'aci':
        temp_file = tem_dir + '\\aci_temp.xml'
        class_file = tem_dir + '\\aci.xml'
        with open(temp_file) as f:
            content = f.read()
            print(content.find('aci_alias'))
            # print(content)
            content = content.replace('aci_alias', args[1])
            content = content.replace('aci_label', args[2])
            content = content.replace('aci_pointname', args[3])
            content = content.replace('aci_unit', args[4])
        with open(class_file) as f_class:
            content_class = f_class.read()
            content_class = content_class.replace('file_name', args[5])
            content_class = content_class.replace('file_label', args[2])
            content_class = content_class.replace('file_unit', args[4])
    elif args[0] == 'aal':
        temp_file = tem_dir + '\\aal_temp.xml'
        class_file = tem_dir + '\\aal.xml'
        with open(temp_file) as f:
            content = f.read()
            print(content.find('aal_alias'))
            # print(content)
            content = content.replace('aal_alias', args[1])
        with open(class_file) as f_class:
            content_class = f_class.read()
            content_class = content_class.replace('file_name', args[2])
    elif args[0] == 'aac':
        temp_file = tem_dir + '\\aac_temp.xml'
        class_file = tem_dir + '\\aac.xml'
        with open(temp_file) as f:
            content = f.read()
            print(content.find('aac_alias'))
            # print(content)
            content = content.replace('aac_alias', args[1])
            content = content.replace('ve_alias', args[2])
            content = content.replace('num_ins', args[3])
        with open(class_file) as f_class:
            content_class = f_class.read()
            content_class = content_class.replace('file_name', args[3])
    elif args[0] == 'afo':
        temp_file = tem_dir + '\\afo_temp.xml'
        class_file = tem_dir + '\\afo.xml'
        with open(temp_file) as f:
            content = f.read()
            print(content.find('afo_alias'))
            # print(content)
            content = content.replace('afo_alias', args[1])
        with open(class_file) as f_class:
            content_class = f_class.read()
            content_class = content_class.replace('file_name', args[2])

    elif args[0] == 'eq':
        temp_file = tem_dir + '\\eq_temp.xml'
        class_file = tem_dir + '\\eq.xml'
        with open(temp_file) as f:
            content = f.read()
            print(content.find('eq_alias'))
            # print(content)
            content = content.replace('eq_alias', args[1])
            content = content.replace('eq_label', args[2])
            content = content.replace('eq_geo', args[3])
            content = content.replace('eq_name', args[4])
            content = content.replace('eq_shortlabel', args[5])
            content = content.replace('eq_mmi', args[6])
        with open(class_file) as f_class:
            content_class = f_class.read()
            content_class = content_class.replace('file_name', args[7])
            content_class = content_class.replace('file_eqname', args[4])
            content_class = content_class.replace('file_label', args[5])
    elif args[0] == 'dio':
        temp_file = tem_dir + '\\dio_temp.xml'
        class_file = tem_dir + '\\dio.xml'
        with open(temp_file) as f:
            content = f.read()
            print(content.find('dio_alias'))
            # print(content)
            content = content.replace('dio_alias', args[1])
            content = content.replace('dio_label', args[2])
            content = content.replace('bit_val0', args[3])
            content = content.replace('bit_lbl0', args[4])
            content = content.replace('bit_sta0', args[5])
            content = content.replace('dov_name0', args[6])
            content = content.replace('bit_val1', args[7])
            content = content.replace('bit_lbl1', args[8])
            content = content.replace('bit_sta1', args[9])
            content = content.replace('dov_name1', args[10])
        with open(class_file) as f_class:
            content_class = f_class.read()
            content_class = content_class.replace('file_name', args[11])
            content_class = content_class.replace('file_label', args[2])
            content_class = content_class.replace('bit_val0', args[3])
            content_class = content_class.replace('bit_lbl0', args[4])
            content_class = content_class.replace('bit_sta0', args[5])
            content_class = content_class.replace('dov_name0', args[6])
            content_class = content_class.replace('bit_val1', args[7])
            content_class = content_class.replace('bit_lbl1', args[8])
            content_class = content_class.replace('bit_sta1', args[9])
            content_class = content_class.replace('dov_name1', args[10])
    elif args[0] == 'dov':
        temp_file = tem_dir + '\\dov_temp.xml'
        class_file = tem_dir + '\\dov.xml'
        with open(temp_file) as f:
            content = f.read()
            print(content.find('dov_alias'))
            # print(content)
            content = content.replace('dov_alias', args[1])
            content = content.replace('dov_rc_ce', args[2])
            content = content.replace('dov_rc_to', args[3])
            content = content.replace('ev_name', args[4])
            content = content.replace('ev_value', args[5])
        with open(class_file) as f_class:
            content_class = f_class.read()
            content_class = content_class.replace('file_name', args[6])
    elif args[0] == 'sio':
        temp_file = tem_dir + '\\sio_temp.xml'
        class_file = tem_dir + '\\sio.xml'
        with open(temp_file) as f:
            content = f.read()
            print(content.find('sio_alias'))
            # print(content)
            content = content.replace('sio_alias', args[1])
            content = content.replace('sio_label', args[2])
            content = content.replace('sio_ev', args[3])
        with open(class_file) as f_class:
            content_class = f_class.read()
            content_class = content_class.replace('file_name', args[4])
            content_class = content_class.replace('file_label', args[2])
    return content, content_class


def write_point_xml(content, point_name):
    cur_dir = os.getcwd()
    out_dir = cur_dir + '\\out'
    exist_dir = out_dir + '\\existed_point'
    exist_list = os.listdir(exist_dir)
    file_name = point_name + 'Instances.xml'
    if file_name in exist_list:
        out_temp_file = exist_dir + '\\' + point_name + 'Instances.xml'
        out_file = out_dir + '\\' + point_name + 'Instances.xml'
        with open(out_temp_file) as f:
            cont = f.readlines()
            cont_new = cont[0:-1]
            for each in content:
                cont_new += each
                if each != content[-1]:
                    cont_new += '\n'
        cont_new += '\n' + cont[-1]
        with open(out_file, 'w') as f:
            f.writelines(cont_new)

    else:
        out_temp_file = out_dir + '\\point_template.xml'
        out_file = out_dir + '\\' + point_name + 'Instances.xml'
        with open(out_temp_file) as f:
            cont = f.readlines()
            cont_new = cont[0:-1]
            cont_new[2] = cont_new[2].replace('point_temp', point_name)
            for each in content:
                cont_new += each
                if each != content[-1]:
                    cont_new += '\n'
        cont_new += '\n' + cont[-1]
        with open(out_file, 'w') as f:
            f.writelines(cont_new)
    '''
    if point_name[0:3] != 'dfo' and point_name[0:3] != 'afo':
        out_temp_file = out_dir + '\\point_template.xml'
        out_file = out_dir + '\\' + point_name + 'Instances.xml'
        with open(out_temp_file) as f:
            cont = f.readlines()
            cont_new = cont[0:-1]
            cont_new[2] = cont_new[2].replace('point_temp', point_name)
            for each in content:
                cont_new += each
                if each != content[-1]:
                    cont_new += '\n'
        cont_new += '\n' + cont[-1]
        with open(out_file, 'w') as f:
            f.writelines(cont_new)
    elif point_name[0:3] == 'afo':
        out_file = out_dir + '\\afoInstances.xml'
        out_temp_file = out_dir + '\\afoInstances_temp.xml'
        with open(out_temp_file) as f:
            cont = f.readlines()
            cont_new = cont[0:-1]
            for each in content:
                cont_new += each
                if each != content[-1]:
                    cont_new += '\n'
        cont_new += '\n' + cont[-1]
        with open(out_file, 'w') as f:
            f.writelines(cont_new)
    else:
        out_file = out_dir + '\\dfoInstances.xml'
        out_temp_file = out_dir + '\\dfoInstances_temp.xml'
        with open(out_temp_file) as f:
            cont = f.readlines()
            cont_new = cont[0:-1]
            for each in content:
                cont_new += each
                if each != content[-1]:
                    cont_new += '\n'
        cont_new += '\n' + cont[-1]
        with open(out_file, 'w') as f:
            f.writelines(cont_new)
    '''


def write_class_xml(content, point_name, number):
    cur_dir = os.getcwd()
    out_dir = cur_dir + '\\out'
    exist_dir = out_dir + '\\existed_point'
    exist_list = os.listdir(exist_dir)
    file_name = point_name + '.xml'
    if file_name in exist_list:
        out_temp_file = exist_dir + '\\' + point_name + '.xml'
        out_file = out_dir + '\\' + point_name + '.xml'
        with open(out_temp_file) as f:
            cont = f.readlines()[2]
            # print(cont)
            matchObj = re.match(r'(.*) numInstances="(.*?)" numPeriod_MT(.*)', cont, re.M)
            print(matchObj.group(2), number, point_name)
            ins_num = int(matchObj.group(2)) + number
            str_org = 'numInstances="' + str(int(matchObj.group(2))) + '"'
            str_org1 = 'numInstances="num_ins"'
            str_new = 'numInstances="' + str(ins_num) + '"'
        print(content[0].find(str_org))
        content = content[0].replace(str_org, str_new).replace(str_org1, str_new)
        with open(out_file, 'w') as f:
            f.writelines(content)

    else:
        out_file = out_dir + '\\' + point_name + '.xml'
        # print(content)
        content = content[0].replace('num_ins', str(number))
        with open(out_file, 'w') as f:
            f.writelines(content)


def gen_xml_file():
    tgt_file = []
    dict_out = {}
    dict_num = {}
    dict_class = {}
    dict_path = {}
    cur_dir = os.getcwd()
    csv_dir = cur_dir + '\\csv'
    dict_path['dci_file'] = csv_dir + '\\dci.csv'
    dict_path['dac_file'] = csv_dir + '\\dac.csv'
    dict_path['dal_file'] = csv_dir + '\\dal.csv'
    dict_path['dfo_file'] = csv_dir + '\\dfo.csv'
    dict_path['aci_file'] = csv_dir + '\\aci.csv'
    dict_path['aac_file'] = csv_dir + '\\aac.csv'
    dict_path['aal_file'] = csv_dir + '\\aal.csv'
    dict_path['afo_file'] = csv_dir + '\\afo.csv'
    dict_path['sio_file'] = csv_dir + '\\sio.csv'
    dict_path['eq_file'] = csv_dir + '\\eq.csv'
    dict_path['dio_file'] = csv_dir + '\\dio.csv'
    dict_path['dov_file'] = csv_dir + '\\dov.csv'
    dict_type = {1: 'dci_file',
                 2: 'dac_file',
                 3: 'dal_file',
                 4: 'dfo_file',
                 5: 'aci_file',
                 6: 'aac_file',
                 7: 'aal_file',
                 8: 'afo_file',
                 9: 'sio_file',
                 10: 'eq_file',
                 11: 'dio_file',
                 12: 'dov_file',
                 0: 'all'}
    # 这里输入选择需要生成的点的类型
    for i in range(len(dict_type)):
        print(str(i) + ':' + dict_type[i])
    choice = input('请输入需要生成的点的类型(输入Q离开)：(如大于一个请用逗号隔开))').split(',')

    print(choice[0])
    if choice[0] != '0':
        for each in choice:
            tgt_file.append(dict_type[int(each)])
    else:
        for i in range(1, len(dict_type)):
            tgt_file.append(dict_type[i])
        print(tgt_file)
    # 根据输入，读取相应类型的点的内容
    for each in tgt_file:
        with open(dict_path[each]) as f:
            point_list = []
            csv_content = f.readlines()
            for each_line in csv_content:
                each_line = each_line.replace('\n', '')
                if each.split('_')[0] == 'dci':
                    alias, label, point_name, file_name = each_line.split(',')[0], each_line.split(',')[1], each_line.split(',')[2], each_line.split(',')[3]
                    print(alias, label, point_name)
                    content, content_class = read_csv_file(each.split('_')[0], alias, label, point_name, file_name)
                    if file_name not in point_list:
                        point_list.append(file_name)
                        dict_out[file_name] = [content]
                        dict_class[file_name] = [content_class]
                        dict_num[file_name] = 1
                    else:
                        dict_out[file_name].append(content)
                        dict_class[file_name].append(content_class)
                        dict_num[file_name] += 1
                elif each.split('_')[0] == 'dac':
                    alias, ve_alias, file_name = each_line.split(',')[0], each_line.split(',')[1], each_line.split(',')[2]
                    content, content_class = read_csv_file(each.split('_')[0], alias, ve_alias, file_name)
                    if file_name not in point_list:
                        point_list.append(file_name)
                        dict_out[file_name] = [content]
                        dict_class[file_name] = [content_class]
                        dict_num[file_name] = 1
                    else:
                        dict_out[file_name].append(content)
                        dict_class[file_name].append(content_class)
                        dict_num[file_name] += 1
                elif each.split('_')[0] == 'dal':
                    alias, ala_type, bit0_value, bit0_label, bit0_state, bit0_severity, bit1_value, bit1_label, bit1_state, bit1_severity,  bit2_value, bit2_label, bit2_state, bit2_severity, bit3_value, bit3_label, bit3_state, bit3_severity, bit4_value, bit5_value, bit6_value, bit7_value, file_name = each_line.split(',')[0], each_line.split(',')[1], each_line.split(',')[2], each_line.split(',')[3], each_line.split(',')[4], each_line.split(',')[5], each_line.split(',')[6], each_line.split(',')[7], each_line.split(',')[8], each_line.split(',')[9], each_line.split(',')[10], each_line.split(',')[11], each_line.split(',')[12], each_line.split(',')[13], each_line.split(',')[14], each_line.split(',')[15], each_line.split(',')[16], each_line.split(',')[17], each_line.split(',')[18], each_line.split(',')[19], each_line.split(',')[20], each_line.split(',')[21], each_line.split(',')[22]
                    content, content_class = read_csv_file(each.split('_')[0], alias, ala_type, bit0_value, bit0_label, bit0_state, bit0_severity, bit1_value, bit1_label, bit1_state, bit1_severity,  bit2_value, bit2_label, bit2_state, bit2_severity, bit3_value, bit3_label, bit3_state, bit3_severity, bit4_value, bit5_value, bit6_value, bit7_value, file_name)
                    # print(content)
                    if file_name not in point_list:
                        point_list.append(file_name)
                        dict_out[file_name] = [content]
                        dict_class[file_name] = [content_class]
                        dict_num[file_name] = 1
                    else:
                        dict_out[file_name].append(content)
                        dict_class[file_name].append(content_class)
                        dict_num[file_name] += 1
                elif each.split('_')[0] == 'dfo':
                    alias, file_name = each_line.split(',')[0], each_line.split(',')[1]
                    content, content_class = read_csv_file(each.split('_')[0], alias, file_name)
                    if file_name not in point_list:
                        point_list.append(file_name)
                        dict_out[file_name] = [content]
                        dict_class[file_name] = [content_class]
                        dict_num[file_name] = 1
                    else:
                        dict_out[file_name].append(content)
                        dict_class[file_name].append(content_class)
                        dict_num[file_name] += 1
                elif each.split('_')[0] == 'aci':
                    alias, label, point_name, unit, file_name = each_line.split(',')[0], each_line.split(',')[1], each_line.split(',')[2], each_line.split(',')[3], each_line.split(',')[4]
                    print(alias, label, point_name)
                    content, content_class = read_csv_file(each.split('_')[0], alias, label, point_name, unit, file_name)
                    if file_name not in point_list:
                        point_list.append(file_name)
                        dict_out[file_name] = [content]
                        dict_class[file_name] = [content_class]
                        dict_num[file_name] = 1
                    else:
                        dict_out[file_name].append(content)
                        dict_class[file_name].append(content_class)
                        dict_num[file_name] += 1
                elif each.split('_')[0] == 'aal':
                    alias, file_name = each_line.split(',')[0], each_line.split(',')[1]
                    content, content_class = read_csv_file(each.split('_')[0], alias,  file_name)
                    if file_name not in point_list:
                        point_list.append(file_name)
                        dict_out[file_name] = [content]
                        dict_class[file_name] = [content_class]
                        dict_num[file_name] = 1
                    else:
                        dict_out[file_name].append(content)
                        dict_class[file_name].append(content_class)
                        dict_num[file_name] += 1
                elif each.split('_')[0] == 'aac':
                    alias, ve_alias, file_name = each_line.split(',')[0], each_line.split(',')[1], each_line.split(',')[2]
                    content, content_class = read_csv_file(each.split('_')[0], alias, ve_alias, file_name)
                    if file_name not in point_list:
                        point_list.append(file_name)
                        dict_out[file_name] = [content]
                        dict_class[file_name] = [content_class]
                        dict_num[file_name] = 1
                    else:
                        dict_out[file_name].append(content)
                        dict_class[file_name].append(content_class)
                        dict_num[file_name] += 1
                elif each.split('_')[0] == 'afo':
                    alias, file_name = each_line.split(',')[0], each_line.split(',')[1]
                    content, content_class = read_csv_file(each.split('_')[0], alias, file_name)
                    if file_name not in point_list:
                        point_list.append(file_name)
                        dict_out[file_name] = [content]
                        dict_class[file_name] = [content_class]
                        dict_num[file_name] = 1
                    else:
                        dict_out[file_name].append(content)
                        dict_class[file_name].append(content_class)
                        dict_num[file_name] += 1
                elif each.split('_')[0] == 'sio':
                    alias, label, ev, file_name = each_line.split(',')[0], each_line.split(',')[1], each_line.split(',')[2], each_line.split(',')[3]
                    content, content_class = read_csv_file(each.split('_')[0], alias, label, ev, file_name)
                    if file_name not in point_list:
                        point_list.append(file_name)
                        dict_out[file_name] = [content]
                        dict_class[file_name] = [content_class]
                        dict_num[file_name] = 1
                    else:
                        dict_out[file_name].append(content)
                        dict_class[file_name].append(content_class)
                        dict_num[file_name] += 1
                elif each.split('_')[0] == 'eq':
                    alias, label, geo_cat, name, shortLabel, mmiSchematic, file_name = each_line.split(',')[0], each_line.split(',')[1], each_line.split(',')[2], each_line.split(',')[3], each_line.split(',')[4], each_line.split(',')[5], each_line.split(',')[6]
                    content, content_class = read_csv_file(each.split('_')[0], alias, label, geo_cat, name, shortLabel, mmiSchematic, file_name)
                    if file_name not in point_list:
                        point_list.append(file_name)
                        dict_out[file_name] = [content]
                        dict_class[file_name] = [content_class]
                        dict_num[file_name] = 1
                    else:
                        dict_out[file_name].append(content)
                        dict_class[file_name].append(content_class)
                        dict_num[file_name] += 1
                elif each.split('_')[0] == 'dio':
                    alias, label, bit_val0, bit_lbl0, bit_sta0, dov_name0, bit_val1, bit_lbl1, bit_sta1, dov_name1, file_name = each_line.split(',')[0], each_line.split(',')[1], each_line.split(',')[2], each_line.split(',')[3], each_line.split(',')[4], each_line.split(',')[5], each_line.split(',')[6], each_line.split(',')[7], each_line.split(',')[8], each_line.split(',')[9], each_line.split(',')[10]
                    content, content_class = read_csv_file(each.split('_')[0], alias, label, bit_val0, bit_lbl0, bit_sta0, dov_name0, bit_val1, bit_lbl1, bit_sta1, dov_name1, file_name)
                    if file_name not in point_list:
                        point_list.append(file_name)
                        dict_out[file_name] = [content]
                        dict_class[file_name] = [content_class]
                        dict_num[file_name] = 1
                    else:
                        dict_out[file_name].append(content)
                        dict_class[file_name].append(content_class)
                        dict_num[file_name] += 1
                elif each.split('_')[0] == 'dov':
                    alias, ce, dov_rc_to, ev, ev_value, file_name = each_line.split(',')[0], each_line.split(',')[1], each_line.split(',')[2], each_line.split(',')[3], each_line.split(',')[4], each_line.split(',')[5]
                    content, content_class = read_csv_file(each.split('_')[0], alias, ce, dov_rc_to, ev, ev_value, file_name)
                    if file_name not in point_list:
                        point_list.append(file_name)
                        dict_out[file_name] = [content]
                        dict_class[file_name] = [content_class]
                        dict_num[file_name] = 1
                    else:
                        dict_out[file_name].append(content)
                        dict_class[file_name].append(content_class)
                        dict_num[file_name] += 1
        # 把读取出的内容加入到源文件中
        # print(dict_num)
        for each_item in dict_out:
            write_point_xml(dict_out[each_item], each_item)
        for each_item in dict_class:
            write_class_xml(dict_class[each_item], each_item, dict_num[each_item])


def gen_root_hier():
    content = '<HierarchyItem alias="root_alias" name="root_name">'
    content1 = '<HierarchyItem alias="root_alias" name="root_name"/>'
    cur_dir = os.getcwd()
    out_dir = cur_dir + '\\out\\rootHier_add.xml'
    csv_dir = cur_dir + '\\csv'
    file_dir = csv_dir + '\\root.csv'

    root_list = []
    sta_list = []
    with open(file_dir) as f:
        read_cont = f.readlines()
    org_alias = read_cont[0].split(',')[0]
    for each_line in read_cont:
        each_line = each_line.strip()
        cont_new = content.replace('root_alias', each_line.split(',')[0]).replace('root_name', each_line.split(',')[1])
        cont_new3 = content1.replace('root_alias', each_line.split(',')[0]).replace('root_name', each_line.split(',')[1])
        # print(type(each_line.split(',')[2]))

        if each_line.split(',')[2] == '1':
            if each_line.split(',')[0] != org_alias:
                sta_list.append('    </HierarchyItem>' + '\n')
                sta_list.append('   </HierarchyItem>' + '\n')
                sta_list.append('   ' + cont_new + '\n')
                org_alias = each_line.split(',')[0]
            else:
                sta_list.append('   ' + cont_new + '\n')
            pt_type = '1'
            dt_type = each_line.split(',')[0][0:3]
            print(dt_type)
        elif each_line.split(',')[2] == '2':
            if pt_type != '1':
                if each_line.split(',')[0][0:3] != 'sio':
                    if dt_type != 'sio':
                        sta_list.append('    </HierarchyItem>' + '\n')
                    if dt_type == 'sio':
                        sta_list.append('    ' + cont_new + '\n')
                    else:
                        sta_list.append('    ' + cont_new + '\n')
                else:
                    if pt_type == '3':
                        sta_list.append('    </HierarchyItem>' + '\n')
                    sta_list.append('    ' + cont_new3 + '\n')

            else:
                sta_list.append('    ' + cont_new + '\n')
            pt_type = '2'
            dt_type = each_line.split(',')[0][0:3]
            print(dt_type)
        elif each_line.split(',')[2] == '3':
            sta_list.append('     ' + cont_new3 + '\n')
            pt_type = '3'
            dt_type = each_line.split(',')[0][0:3]
            print(dt_type)
        if each_line == read_cont[-1]:
            sta_list.append('    </HierarchyItem>' + '\n')
            sta_list.append('   </HierarchyItem>' + '\n')
    sta_list.append('   </HierarchyItem>')
    sta_list.append('\n')
    sta_list.append('  </HierarchyItem>')
    with open(out_dir, 'w') as f:
        f.writelines(sta_list)


def find_exist_file(path):
    exist_list = os.listdir(path)
    for each in exist_list:
        if each.find('.') == -1:
            exist_list.remove(each)
    return exist_list


def copy_exist_file():
    cur_dir = os.getcwd()
    out_dir = cur_dir + '\\out'
    target_dir = cur_dir + '\\copy_exist'
    path = out_dir + '\\existed_point'
    # os.remove(path + '\\AZM_xml')
    exist_list = []
    exist_list = find_exist_file(path)
    station_xml_path = 'X:\\DB\\BJ_CFG\\ZCI_xml'
    station_xml_list = find_exist_file(station_xml_path)
    target_exist_path = target_dir + '\\ZCI_xml\\'
    os.mkdir(target_dir + '\\ZCI_xml')
    for each_file_name in exist_list:
        print(target_exist_path + each_file_name)
        with open(station_xml_path + '\\' + each_file_name) as f1:
            content = f1.read()
        with open(target_exist_path + each_file_name, 'w') as f2:
            f2.write(content)


if __name__ == '__main__':
    print('请选择需要的操作,输入Q退出：')
    print('1. 生成存在的xml文件.\n2. 生成需要的xml文件.\n3. 生成root_hier.xml增加文件')
    choice = input()
    while choice != 'Q':
        if choice == '1':
            copy_exist_file()
            print('请选择需要的操作,输入Q退出：')
            print('1. 生成存在的xml文件.\n2. 生成需要的xml文件.\n3. 生成root_hier.xml增加文件')
            choice = input()
        elif choice == '2':
            gen_xml_file()
            print('请选择需要的操作,输入Q退出：')
            print('1. 生成存在的xml文件.\n2. 生成需要的xml文件.\n3. 生成root_hier.xml增加文件')
            choice = input()
        elif choice == '3':
            gen_root_hier()
            print('请选择需要的操作,输入Q退出：')
            print('1. 生成存在的xml文件.\n2. 生成需要的xml文件.\n3. 生成root_hier.xml增加文件')
            choice = input()
        else:
            print('输入有误，请重新输入')
            choice = input('请选择需要的操作,输入Q退出：')

