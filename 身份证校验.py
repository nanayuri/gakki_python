# -*- coding: gbk -*-
import pickle
import datetime
import ���֤������


def borderline(str1, ch='*'):
    # ����Ŀ����Ϊһ�л�����ַ�������һ���߿򣬸����۵������*Ϊȱʡ�߿��ַ�
    strLen = 0
    for each in str1.splitlines():  # �ҳ��ַ����һ�е��ַ���
        if strLen < len(each.encode('gb2312')): strLen = len(each.encode('gb2312'))
        # ����encode('gb2312')��ʹÿ�����ּ�Ϊ2���ַ�����
    str2 = ch * (strLen + 6) + '\n'
    str2 = str2 + ch + ' ' * (strLen + 4) + ch + '\n'
    for each in str1.splitlines():
        str2 = str2 + ch + '  ' + each + ' ' * (strLen - len(each.encode('gb2312')) + 2) + ch + '\n'
    str2 = str2 + ch + ' ' * (strLen + 4) + ch + '\n'
    str2 = str2 + ch * (strLen + 6)
    return str2


def checkDate(str1):
    # ������������Ƿ�Ϸ�
    try:
        global birthday
        birthday = datetime.date(int(str1[6:10]), int(str1[10:12]), int(str1[12:14]))
        check = True
    except:
        check = False
    return check


def checkByte(str1):
    # ����У��λ
    w = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    s = 0
    for i in range(17):
        s = s + int(str1[i]) * w[i]
    check = (1 - s) % 11  # ����s%11�ٲ��õ�У��λ�����ݹ���ֱ�Ӽ���ó�
    if check == 10: check = 'X'
    check = str(check)
    return check


def sex(str1):
    # �鿴�Ա�
    if int(str1[-2]) % 2 == 0:
        return 'Ů'
    else:
        return '��'


titleStr = '''���֤��������ʶ��'''
f = open('f1.pkl', 'rb')  # �򿪹��������ݿ�
idData = pickle.load(f)#��ȡ���ݿ�
f.close()
url = 'http://www.tcmap.com.cn/list/daima_list.html'
html = ���֤������.open_url(url)
#idData = ���֤������.find_data(html)

# ��ȡ���ݿ�
# f.close()
print(borderline(titleStr))
week = ('����һ', '���ڶ�', '������', '������', '������', '������', '������')
while True:
    code = input('������15λ��18λ���֤���룬���롰q���˳���')
    if code.upper() == 'Q':
        break
    if len(code) != 15 and len(code) != 18:
        print('����λ���������������롣')
        continue
    if len(code) == 15:
        code = code[:6] + '19' + code[6:] + 'M'
        # 15λ���֤��19xx�꿼�ǣ���תΪ18λ��У��λ��δ��M�����������������жϺͼ���
    if not (code[:17].isdigit() and (code[-1].isdigit() or code[-1] == 'M' or code[-1].upper() == 'X')):
        print('����15λ���֤Ҫ��ȫΪ���֣�18λ���֤ǰ17λΪ���֣���18λΪ���ֻ���ĸ��X�������������롣')
        continue
    if idData.get(code[:6]) == None:
        print('�����ǰ6λ�ǹ����ش��룬������Ĺ����ز鲻�������������롣', )
        continue
    if checkDate(code) == False:
        print('15λ���֤��7~12λΪ���ڣ�18λ���֤7~14λΪ���ڣ�����������������������롣', )
        continue
    last = checkByte(code)  # ����У��λ
    if code[-1] == 'M':
        code = code[:17] + last
        print('15λת18λ���֤���ǣ�', code)
    elif code[-1] != last:
        code = code[:17] + last
        print('18λ���֤У�������ȷ�ĺ�������ǣ�', code)
    else:
        print('18λ���֤У����ȷ��')
    print('���֤�����أ�', idData[code[:6]])
    print('���գ�', birthday, week[birthday.weekday()])
    print('���䣺', datetime.datetime.now().year - int(code[6:10]))
    print('�Ա�', sex(code))
