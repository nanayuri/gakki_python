import openpyxl
import time


Class_list_dict = {}
Class_list_dict['isAComment'] = 1
Class_list_dict['Class name'] = 4
Class_list_dict['SIL Level'] = 11
Instance_list_dict = {}
Instance_list_dict['isAComment'] = 1
Instance_list_dict['Description'] = 5
Instance_list_dict['Location'] = 6
Instance_list_dict['Sublocation'] = 7
Instance_list_dict['Class name'] = 8
Instance_list_dict['Equipment name'] = 9
Instance_list_dict['RTU name'] = 10
Instance_list_dict['Short name'] = 20
Instance_list_dict['Unique ID code'] = 21
EV_dict = {}
EV_dict['Class name'] = 0
EV_dict['iopath'] = 1
EV_dict['vetype'] = 2
EV_dict['ve_base'] = 3
EV_dict['description'] = 4
EV_dict['address'] = 5
EV_dict['evgroup'] = 6
EV_dict['deadband'] = 7
EV_dict['length'] = 11

type_dict = {
    'dci': 'dac',
    'aci': 'aac',
    'dio': 'dov',
    'aio': 'aio'
}

ev_type_dict = {
    'dci': 'dei',
    'aci': 'aei',
    'dio': 'deo',
    'aio': 'aeo'
}

sil_type_dict = {
    'SIL0': '_S0',
    'SIL2_Monitoring': '_S2M',
    'SIL2_Control': '_S2C'
}

ins_list = []
list_nom = [[], [], [], [], [], [], [], [], [], []]
ws_list = []
row_list = []
ws_par_list = []
link_list = []
ev_gen_list = []


def save_to_excel(data, i):
    wb_new = openpyxl.Workbook()
    wb_new.guess_types = True
    ws_new = wb_new.active
    ws_new.append(['nom_instance', 'ID', 'ELEMENT_NAME', '__PROTOTYPE__', '__AGGREGATE__', 'link_object_is_from_object_type', 'reference_import', 'label', 'shortname', 'hvid'])
    for each in data:
        ws_new.append(each)
    file_n = str(i) + "-equipment.csv"
    wb_new.save(file_n)
    wb_new.close()


def save_link_to_excel(data):
    wb_new = openpyxl.Workbook()
    wb_new.guess_types = True
    ws_new = wb_new.active
    ws_new.append(['nom_instance', 'ID', 'ELEMENT_NAME', 'lk0', 'lk1'])
    for each in data:
        ws_new.append(each)
    file_n = "lk_gen.csv"
    wb_new.save(file_n)
    wb_new.close()


def save_ev_to_excel(data):
    wb_new = openpyxl.Workbook()
    wb_new.guess_types = True
    ws_new = wb_new.active
    ws_new.append(['ID', 'nom_instance', 'reference_import', 'address', 'deadband', 'label', 'length', 'name', 'type', 'ELEMENT_NAME', 'varInvalid1', 'varInvalid2', 'varInvalid3', 'functCheck', 'functTrans'])
    for each in data:
        ws_new.append(each)
    file_n = "ev_gen.csv"
    wb_new.save(file_n)
    wb_new.close()


def add_parent_path(row_id):
    row_id = row_id[5:]
    id_list = row_id.split(':')
    instance = ':R:A'
    for each_ins in id_list:
        instance += (':' + each_ins)
        if instance not in ins_list:
            ins_list.append(instance)

    return ins_list


def split_parent(ins_list):
    for each_ins in ins_list:
        num = each_ins.count(':')
        if each_ins not in list_nom[num - 1]:
            list_nom[num - 1].append(each_ins)
    return list_nom


def judge_str_null(s):
    if s.strip() == '':
        pass
    else:
        return s


def judge_proto(s_eq, eq):
    if s_eq == '':
        return 'Qatar:QatarAlmSynthe'
    else:
        return eq


def judge_label(s_eq, s_nom):
    if s_eq == '':
        return 'Synthesis class ' + s_nom
    else:
        return 'LusHK:Lus'


def open_excel(file_name):

    wb = openpyxl.load_workbook(file_name)
    ws_1 = wb['1-Class List']
    ws_2 = wb['2-Instance List']
    ws_3 = wb['3-Class Mapping']
    ws_4 = wb['4-External Variables']


def split_parent_node(data):
    par_list = []
    ws_par_list = []
    for each_list in data:
        par_id = each_list
        par_proto = 'Qatar:QatarAlmSynthe'
        par_nom_ins = par_id.split(':')[-1]
        par_elename = ''
        par_aggreg = ''
        par_linkob = ''
        par_refimp = ''
        par_label = 'Synthesis class ' + par_nom_ins
        par_shtnam = '&' + par_nom_ins
        par_hvid = 'STA_' + par_nom_ins
        for each in [par_nom_ins, par_id, par_elename, par_proto, par_aggreg, par_linkob, par_refimp, par_label,
                     par_shtnam, par_hvid]:
            par_list.append(each)
        ws_par_list.append(par_list)
    return ws_par_list


def equipment_csv():
    file_name = 'LRT-QSTT-XX-ICD-SCC-GEN00-371058_-B2.1_ICD_SCADA-TVS_Appendix_C_ATT1 SW input.xlsx'
    wb = openpyxl.load_workbook(file_name, data_only=True)
    list_par = []
    ws_1 = wb['1-Class List']
    ws_2 = wb['2-Instance List']
    ws_3 = wb['3-Class Mapping']
    ws_4 = wb['4-External Variables']

    for each_row in ws_3.rows:
        class_map_dict = {}
        if each_row[0].value != 'Class name':
            class_map_dict[each_row[0].value] = each_row[1].value
    print(class_map_dict)

    for each_row in ws_2.rows:
        row_list = []
        print(each_row[Instance_list_dict['isAComment']].value)
        if each_row[Instance_list_dict['isAComment']].value == 'N':
            row_id = ':R:A:' + judge_str_null(each_row[Instance_list_dict['Location']].value) + ':' + judge_str_null(
                each_row[Instance_list_dict['Sublocation']].value) + ':' + judge_str_null(each_row[Instance_list_dict['Equipment name']].value)
            row_par = ':R:A:' + judge_str_null(each_row[Instance_list_dict['Location']].value) + ':' + judge_str_null(
                each_row[Instance_list_dict['Sublocation']].value)

            try:
                row_proto = class_map_dict[judge_proto(each_row[Instance_list_dict['Equipment name']].value, each_row[Instance_list_dict['Class name']].value)]
            except KeyError:
                row_proto = 'not defined'
            row_nom_ins = row_id.split(':')[-1]
            row_elename = ''
            row_aggreg = ''
            row_linkob = ''
            row_refimp = ''
            row_label = each_row[Instance_list_dict['Description']].value
            row_shtnam = each_row[Instance_list_dict['Short name']].value
            row_hvid = each_row[Instance_list_dict['Unique ID code']].value
            list_par = split_parent(add_parent_path(row_par))
            print(row_id)
            for each in [row_nom_ins, row_id, row_elename, row_proto, row_aggreg, row_linkob, row_refimp, row_label, row_shtnam, row_hvid]:
                row_list.append(each)
            ws_list.append(row_list)

    save_to_excel(ws_list, 'all')
    i = 1
    for each_list in list_par:
        ws_par_list = []
        if each_list:
            for each_data in each_list:
                par_list = []
                par_id = each_data
                par_proto = 'Qatar:QatarAlmSynthe'
                par_nom_ins = par_id.split(':')[-1]
                par_elename = ''
                par_aggreg = ''
                par_linkob = ''
                par_refimp = ''
                par_label = 'Synthesis class ' + par_nom_ins
                par_shtnam = '&' + par_nom_ins
                par_hvid = 'STA_' + par_nom_ins
                for each in [par_nom_ins, par_id, par_elename, par_proto, par_aggreg, par_linkob, par_refimp, par_label,
                             par_shtnam, par_hvid]:
                    par_list.append(each)
                ws_par_list.append(par_list)
            save_to_excel(ws_par_list, i)
            i += 1


def ev():
    ws_ev_list = []
    class_list = []
    ev_gp_list = []
    file_name = 'LRT-QSTT-XX-ICD-SCC-GEN00-371058_-B2.1_ICD_SCADA-TVS_Appendix_C_ATT1 SW input.xlsx'
    wb = openpyxl.load_workbook(file_name, data_only=True)
    list_par = []
    ws_1 = wb['1-Class List']
    ws_2 = wb['2-Instance List']
    ws_3 = wb['3-Class Mapping']
    ws_4 = wb['4-External Variables']
    for each_row in ws_1.rows:

        Class_list_dict['isAComment'] = 1
        Class_list_dict['Class name'] = 4
        Class_list_dict['SIL Level'] = 11
        Class_list_dict['Code'] = 63
        row_list = []
        if each_row[Class_list_dict['isAComment']].value == 'N':
            row_class = each_row[Class_list_dict['Class name']].value
            row_sil_level = each_row[Class_list_dict['SIL Level']].value
            row_code = each_row[Class_list_dict['Code']].value

            for each in [row_class,row_code, row_sil_level]:
                row_list.append(each)
            class_list.append(row_list)

    for each_row in ws_2.rows:
        row_list = []
        if each_row[Instance_list_dict['isAComment']].value == 'N':
            row_id = ':R:A:' + judge_str_null(each_row[Instance_list_dict['Location']].value) + ':' + judge_str_null(
                each_row[Instance_list_dict['Sublocation']].value) + ':' + judge_str_null(each_row[Instance_list_dict['Equipment name']].value)

            row_class = each_row[Instance_list_dict['Class name']].value
            row_rtu_name = each_row[Instance_list_dict['RTU name']].value

            for each in [row_id, row_class, row_rtu_name]:
                row_list.append(each)
            ws_ev_list.append(row_list)

    for each_row in ws_4.rows:
        ev_class = each_row[EV_dict['Class name']].value
        ev_address = each_row[EV_dict['address']].value
        ev_deadband = each_row[EV_dict['deadband']].value
        ev_label = each_row[EV_dict['description']].value
        ev_length = each_row[EV_dict['length']].value
        ev_type = each_row[EV_dict['vetype']].value
        ev_ptname = each_row[EV_dict['iopath']].value.replace(':dac', '')
        ev_group = each_row[EV_dict['evgroup']].value
        ev_list = []
        if each_row[EV_dict['Class name']].value != 'Class name':
            for each in [ev_class, ev_ptname, ev_address, ev_deadband, ev_label, ev_length, ev_type, ev_group]:
                ev_list.append(each)
            ev_gp_list.append(ev_list)

    for each in ws_ev_list:

        class_name = each[1]
        nom_instance = 'link_ve'
        for each_ele in ev_gp_list:
            each_link = []
            each_ev = []
            deadband = each_ele[3]
            label = each_ele[4]
            length = each_ele[5]
            ev_tp = each_ele[6]
            pt_type = each_ele[1][0:3]
            pt_ele_type = type_dict[pt_type] + '_type_link_ve'
            address = each_ele[2]
            if each_ele[0] == class_name:
                link_id = each[0] + ':' + each_ele[1] + ':' + type_dict[pt_type] + ':link_ve'
                for each_sil in class_list:
                    if each_sil[0] == each_ele[0] and each_sil[1] == str(each_ele[1]).split('-')[-1]:
                        sil_type = sil_type_dict[each_sil[2]]
                        lk0 = ':R:A:POLE:' + each[2] + sil_type + ':' + each_ele[7] + ':' + ev_type_dict[pt_type] + str(
                            each[0][5:]).replace(':', '') + str(each_ele[1]).split('-')[-1]
                print(link_id)
                each_link.append(nom_instance)
                each_link.append(link_id)
                each_link.append(pt_ele_type)
                each_link.append(lk0)
                each_ev.append(lk0)
                each_ev.append(str(lk0).split(':')[-1])
                each_ev.append('M-Conf ' + time.strftime("%d/%m/%y %H:%M"))
                each_ev.append(address)
                each_ev.append(deadband)
                each_ev.append(label)
                each_ev.append(length)
                each_ev.append(str(lk0).split(':')[-1])
                each_ev.append(ev_tp)
                each_ev.append('VE')
                link_list.append(each_link)
                ev_gen_list.append(each_ev)

    print(ws_ev_list)
    print(ev_gp_list)
    print(link_list)
    print(class_list)
    print(ev_gen_list)
    save_link_to_excel(link_list)
    save_ev_to_excel(ev_gen_list)


if __name__ == "__main__":
    # equipment_csv()
    ev()



