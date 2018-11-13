#coding=utf-8
import os
import difflib
import datetime
import sys

occ_dict = {
    'PSCADA': 'OCC',
    'AFC': 'OCC',
    'MPSCADA': 'OCC',
    'SIG': 'OCC',
    'PSD': 'OCC',
    'AFC': 'OCC',
    'BAS': 'OCCB',
    'UPS': 'OCCB',
    'FG': 'OCCB',
    'DTS': 'OCCB',
    'ASD': 'OCCB',
    'FAS': 'OCCC',
    'ALM': 'OCCC',
    'ACS': 'OCCC',
    'PA': 'OCCC',
    'PIS': 'OCCC',
    'CCTV': 'OCCC'
}
starttime = datetime.datetime.now()
def compare_file(file1, file2):
    f1 = file(file1)
    text1_lines = f1.readlines()
    f2 = file(file2)
    text2_lines = f2.readlines()
    d = difflib.Differ()
    diff = d.compare(text1_lines, text2_lines)
    out_list = []
    for each_line in list(diff):
        if each_line[0] == '+' and each_line[2] == '-':
            print each_line
            out_list.append(each_line)
    return out_list


def test_io_with_event(line1, line2):
    # line1 is from IO list, line2 is generated from eventlist
    error_list = []
    alias_el = '<alias>' + str(line2.split('"')[1].replace(':', ''))
    alias_io = str(line1.split(',')[0])
    pt_el = str(line2.split('"')[5].split('|')[13].split(':')[-1])
    pt_io = str(line1.split(',')[1])
    eqpt_shn_el = str(line2.split('"')[5].split('|')[3])
    eqpt_shn_io = str(line1.split(',')[7])
    eqpt_lbl_el = str(line2.split('"')[5].split('|')[2])
    eqpt_lbl_io = str(line1.split(',')[8])
    pt_lbl_el = str(line2.split('"')[5].split('|')[4])
    pt_lbl_io = str(line1.split(',')[9])
    bit_lbl_el = str(line2.split('"')[5].split('|')[5])
    bit_lbl_io = str(line1.split(',')[10])
    bit_sev_el = str(line2.split('"')[4].split(' ')[3])
    bit_ser_io = str(line1.split(',')[12])
    print(str(line2.split('"')[4]))
    if alias_el != alias_io:
        error_list.append(alias_el + 'is not same as event list' + '\n')
    else:
        if pt_el != pt_io:
            error_list.append(pt_el + 'is not same as event list' + '\n')
        else:
            if eqpt_shn_el != eqpt_shn_io:
                error_list.append(alias_io + ':' + pt_io + '  ' + eqpt_shn_io + ' 设备描述 is not same as event list' + '\n')
            else:
                if eqpt_lbl_el != eqpt_lbl_io:
                    error_list.append(alias_io + ':' + pt_io + '  ' + eqpt_lbl_io + ' 设备标签 is not same as event list' + '\n')
                else:
                    if pt_lbl_el != pt_lbl_io:
                        error_list.append(alias_io + ':' + pt_io + '  ' + pt_lbl_io + ' 属性描述 is not same as event list' + '\n')
                    else:
                        if bit_lbl_el != bit_lbl_io:
                            error_list.append(alias_io + ':' + pt_io + '  ' + bit_lbl_io + ' 比特标签 is not same as event list' + '\n')
                        else:
                            if bit_sev_el != bit_ser_io:
                                error_list.append(alias_io + ':' + pt_io + '  ' + bit_ser_io + ' 比特严重度 is not same as event list' + '\n')
                            else:
                                error_list.append(alias_io + ':' + pt_io + ' has passed the test!' + '\n')
    return error_list



if __name__ == "__main__":
    choose = str(sys.argv[1])
    local_dir = os.getcwd()
    os.system('rm -rf test_result.txt')
    for i in os.listdir("."):
        if os.path.splitext(i)[-1] == ".txt" and os.path.splitext(i)[0][0:4] == 'NBL3':
            file_temp = str(i)
            occ_name = file_temp.split(' ')[4]
            # file_temp = 'NBL3 NF IO List AFC ZXN(中兴大桥南站) V1.5 (20180914).xlsx'

            # command = 'cd /export/home/nbl2/OCC_A1TEMP2_181023/log/unit_test; ./abc.py'
            # run_script(command)
            # 首先set 通讯状态点
            file_gen = file_temp
            final_list = []
            with open(file_gen, 'r') as f1:
                io_cont = f1.readlines()
            station_name = io_cont[0].split(',')[3]
            sys_name = io_cont[0].split(',')[4]
            com_file_template = 'set_com.sh_template'
            com_file = 'set_com.sh'
            with open(com_file_template, 'r') as f_com:
                com_cont = f_com.read()
            with open(com_file, 'w') as f_com_new:
                f_com_new.write(str(com_cont).replace('station_name', station_name).replace('sys_name', sys_name).replace('occ_name', occ_dict[occ_name]))
            os.system('./add_right.sh')
            os.system('./set_com.sh')
            if choose == '1':
                for each_line in io_cont:
                    # Step 4. 保存eventlist到old_event.txt
                    # command1 = 'cd ' + ut_dir + ';rm old_event.txt'
                    # run_script(command1)
                    os.system('./save_old.sh')
                    print ('-----Original status for eventlist has been saved successfully! -----')

                    # Step 5. 执行tcl去模拟值的变化
                    each_list = each_line.split(',')
                    target_pt = each_list[0][7:] + ':' + each_list[1]
                    target_value = each_list[-3]
                    # 生成对应.sh文件
                    sh_file = 'set_pt.sh_template'
                    tar_sh_file = 'set_pt.sh'
                    with open(sh_file, 'r') as f2:
                        sh_cont = f2.read()
                    with open(tar_sh_file, 'w') as f3:
                        f3.write(str(sh_cont).replace('replace_pt_alias', target_pt).replace('replace_value', target_value))
                    os.system('./add_right.sh')
                    os.system('./set_pt.sh')
                    # Step 6. 模拟点的值
                    # print('-----The point' + str(sh_cont).replace('replace_pt_alias', target_pt) + ' successfully! -----')
                    # Step 7. 保存eventlist到new_event.txt
                    os.system('./save_new.sh')
                    print ('-----New status for eventlist has been saved successfully! -----')
                    # Step 8. 上传old_event.txt和new_event.txt

                    # Step 9. 比较前后两份eventlist
                    compare_list = compare_file('old_event.txt', 'new_event.txt')
                    # Step 10. 比较模拟的结果和io中的信息
                    # 首先处理compare_list
                    final_list.append(compare_list)

                    if len(compare_list) != 0:
                        main_list = compare_list[0].split('"')[5]
                        alias_new = '<alias>' + str(main_list[13]).replace(':', '')
                        alias_old = str(each_line[0]) + str(each_line[1])
            elif choose == '2':
                os.system('rm -rf *_event.txt')
                os.system('./save_old.sh')
                for each_line in io_cont:
                    # Step 4. 保存eventlist到old_event.txt
                    # command1 = 'cd ' + ut_dir + ';rm old_event.txt'
                    # run_script(command1)

                    print('-----Original status for eventlist has been saved successfully! -----')

                    # Step 5. 执行tcl去模拟值的变化
                    each_list = each_line.split(',')
                    target_pt = each_list[0][7:] + ':' + each_list[1]
                    target_value = each_list[-3]
                    # 生成对应.sh文件
                    sh_file = 'set_pt.sh_template'
                    tar_sh_file = 'set_pt.sh'
                    with open(sh_file, 'r') as f2:
                        sh_cont = f2.read()
                    with open(tar_sh_file, 'w') as f3:
                        f3.write(str(sh_cont).replace('replace_pt_alias', target_pt).replace('replace_value', target_value).replace('replace_occ', occ_dict[occ_name]))
                    os.system('./add_right.sh')
                    os.system('./set_pt.sh')
                os.system('./save_new.sh')
                compare_list = compare_file('old_event.txt', 'new_event.txt')
                final_list.append(compare_list)
                if len(compare_list) != 0:
                     main_list = compare_list[0].split('"')[5]
                     alias_new = '<alias>' + str(main_list[13]).replace(':', '')
                     alias_old = str(each_line[0]) + str(each_line[1])
            with open('out.txt', 'w') as f_out:
                for each_line in final_list:
                    f_out.writelines(each_line)
            if choose == '1':
                pass
            elif choose == '2':
                with open('out.txt', 'r') as f_out:
                    evl_list = f_out.readlines()
                for each_line in evl_list:
                    b = each_line.split('|')[13]
                    if str(b.split(':')[1] + b.split(':')[2]) != str(station_name) + str(sys_name) or str(b.split(':')[3][0:3]) == 'STA':
                        evl_list.remove(each_line)


                final_error_list = []
                io_len = len(io_cont)
                el_len = len(evl_list)
                print(io_len, el_len)
                if io_len != el_len:
                    print('different points number between in io list and event list, please check it again.')
                else:
                    for i in range(io_len):
                        line1 = io_cont[i]
                        line2 = evl_list[i]
                        error_list = test_io_with_event(line1, line2)
                        final_error_list.append(error_list)
                    with open('test_result.txt', 'a') as f_out:
                        for each_line in final_error_list:
                            f_out.writelines(each_line)
            endtime = datetime.datetime.now()
    print('程序总用时' + str((endtime - starttime).seconds) + '秒')