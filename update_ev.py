import re
import os


def updt_pow_db():
    for each_file in file_list:
        each_file_path = tar_dir + '\\' + each_file
        with open(each_file_path, 'r') as f1:
            content = f1.readlines()
            pow_list = []
            for each in content:
                try:
                    cont = each.split(';')
                    if len(cont) > 1:
                        cont = cont[1]
                        a = re.match(r' aeiGZ[0-9]{3}PSCADAJL[J|K][1|3|5|6][0-9]{4}-U[A|B|C][A|B|C]', cont)

                        if a is not None:
                            deadband_org = each.split(';')[5]
                            each = each.replace(';' + deadband_org + ';', '; 0.1;')
                            print(each)
                        pow_list.append(each)
                    else:
                        pow_list.append(each)
                except TypeError:
                    pass
            print(pow_list)
        with open(each_file_path, 'w') as f2:
            f2.writelines(pow_list)


def updt_bas_db():
    for each_file in file_list:
        each_file_path = tar_dir + '\\' + each_file
        with open(each_file_path, 'r') as f1:
            content = f1.readlines()
            pow_list = []
            # pt_list = ['CWOWTEMP',	'CWIWTEMP',	'CTMPSET',	'EVOUTMP',	'EVINTMP',	'ENVTMP',	'CMEXTMP1',	'CWOWTEMP',	'CWIWTEMP',	'CTMPSET',	'EVOUTMP',	'EVINTMP',	'ENVTMP',	'CMEXTMP1',	'CMEXTMP2']
            # eqt_list = ['WCC1', 'WCC2']
            pt_list = ['MOCUR', 'MOFRE', 'CMEXPRE1', 'CMEVPRE1', 'CMRNCUR1', 'CMEXHOD1', 'CMXPPR1', 'CMCAP1', 'CMRCAP1',
                       'EXPOPEN', 'CMRNTIM1', 'CMSTRTM1', 'EXPOPEN1', 'CMEXPRE2', 'CMEVPRE2', 'CMRNCUR2', 'CMEXHOD2',
                       'CMXPPR2', 'CMCAP2', 'CMRCAP2', 'EXPOPEN2', 'CMRNTIM2', 'CMSTRTM2', 'OPFEDBAC', 'PRESB', 'FLOW',
                       'RUNTIME', 'FLTTIME', 'STRTIME', 'CO2CONC', 'INVOLT', 'FLTVOLT', 'OUTVOLT', 'LDPCNT', 'INFRQ',
                       'BTVOLT', 'UPSTEMP', 'MNVOLTA', 'MNVOLTB', 'MNVOLTC', 'INBVOLTA', 'INBVOLTB', 'INBVOLTC',
                       'EPSCURA', 'EPSCURB', 'EPSCURC', 'CHGVOLT', 'CHGCUR']
            eqt_list = ['TEF_', 'HPF_', 'AHU1', 'CHWP', 'WCC1', 'WCC2', 'MOV_', 'P___', 'DP__', 'F___', 'ESC1', 'ESC2',
                        'CO2_', 'UPS1', 'EPS1']
            for each in content:
                try:
                    cont = each.split(';')
                    if len(cont) > 1:
                        cont = cont[1]
                        for each_eqpt in eqt_list:
                            for each_pt in pt_list:
                                a = re.match(r' aeiGZ[0-9]{3}BAS' + each_eqpt + r'[0-9]{4}-' + each_pt, cont)
                                if a is not None:
                                    break
                            if a is not None:
                                break
                        if a is not None:
                            deadband_org = each.split(';')[5]
                            each = each.replace(';' + deadband_org + ';', '; 1;')
                            print(each)
                        pow_list.append(each)
                    else:
                        pow_list.append(each)
                except TypeError:
                    pass
            print(pow_list)
        with open(each_file_path, 'w') as f2:
            f2.writelines(pow_list)


if __name__ == '__main__':
    cur_dir = os.getcwd()
    tar_dir = cur_dir + '\\' + 'GZL7'
    file_list = os.listdir(tar_dir)
    # updt_pow_db()
    updt_bas_db()
