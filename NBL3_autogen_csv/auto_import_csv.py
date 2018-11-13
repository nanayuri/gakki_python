import os
import wmi
from win32com.client import GetObject, Dispatch


def auto_import_class(file_path):
    files_list = os.listdir(file_path)
    Cfg_Folder_Path = 'Z:\\'
    Cfg_Inter_File = Cfg_Folder_Path + 'CfgInterface_csv.bat'
    i = 1
    file_dict = {}
    for each_file in files_list:
        print(i + '.' + each_file)
        file_dict[i] = each_file
    str1 = str(input('请输入需要导入的csv文件, 多个文件间用逗号隔开,0为所有文件:'))
    ved = input('请输入wds名称:\n')
    list1 = []
    if str1 == '0':
        initVal = 1
        listLen = len(file_dict)
        list1 = [i for i in range(1, listLen + 1)]
    else:
        for each in str1.split(','):
            list1.append(int(each))
    for each in list1:
        each_file = file_dict[each]
        cmd_commend = 'I.ImportCSV(' + ved + ',' + each_file + ')'


def sys_version(ipaddress, user, password):
    conn = wmi.WMI(computer=ipaddress, user=user, password=password)
    for sys in conn.Win32_OperatingSystem():
        print("Version:%s" % sys.Caption.encode("UTF8"), "Vernum:%s" % sys.BuildNumber)  # 系统信息
        print(sys.OSArchitecture.encode("UTF8"))  # 系统的位数
        print(sys.NumberOfProcesses)  # 系统的进程数
    try:
        filename = r"C:\softs\Configurator\ISCS_NB_11\client\script\CfgInterface_csv.bat"  # 此文件在远程服务器上
        cmd_callbat = r"cmd /c call %s" % filename
        conn.Win32_Process.Create(CommandLine=cmd_callbat)  # 执行bat文件   Win32_Process.Create
    except Exception as e:
        print(e)


if __name__ == '__main__':
    sys_version(ipaddress="192.168.1.200", user="xia", password="thales")