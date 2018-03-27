# -*- coding: gbk -*-
import pickle
import datetime
import 身份证归属地


def borderline(str1, ch='*'):
    # 函数目的是为一行或多行字符串加上一个边框，更美观的输出，*为缺省边框字符
    strLen = 0
    for each in str1.splitlines():  # 找出字符串最长一行的字符数
        if strLen < len(each.encode('gb2312')): strLen = len(each.encode('gb2312'))
        # 加上encode('gb2312')是使每个汉字记为2个字符长度
    str2 = ch * (strLen + 6) + '\n'
    str2 = str2 + ch + ' ' * (strLen + 4) + ch + '\n'
    for each in str1.splitlines():
        str2 = str2 + ch + '  ' + each + ' ' * (strLen - len(each.encode('gb2312')) + 2) + ch + '\n'
    str2 = str2 + ch + ' ' * (strLen + 4) + ch + '\n'
    str2 = str2 + ch * (strLen + 6)
    return str2


def checkDate(str1):
    # 检查日期数据是否合法
    try:
        global birthday
        birthday = datetime.date(int(str1[6:10]), int(str1[10:12]), int(str1[12:14]))
        check = True
    except:
        check = False
    return check


def checkByte(str1):
    # 计算校验位
    w = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    s = 0
    for i in range(17):
        s = s + int(str1[i]) * w[i]
    check = (1 - s) % 11  # 可以s%11再查表得到校验位，根据规律直接计算得出
    if check == 10: check = 'X'
    check = str(check)
    return check


def sex(str1):
    # 查看性别
    if int(str1[-2]) % 2 == 0:
        return '女'
    else:
        return '男'


titleStr = '''身份证号码内容识别'''
f = open('f1.pkl', 'rb')  # 打开归属地数据库
idData = pickle.load(f)#读取数据库
f.close()
url = 'http://www.tcmap.com.cn/list/daima_list.html'
html = 身份证归属地.open_url(url)
#idData = 身份证归属地.find_data(html)

# 读取数据库
# f.close()
print(borderline(titleStr))
week = ('星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日')
while True:
    code = input('请输入15位或18位身份证号码，输入“q”退出：')
    if code.upper() == 'Q':
        break
    if len(code) != 15 and len(code) != 18:
        print('输入位数有误，请重新输入。')
        continue
    if len(code) == 15:
        code = code[:6] + '19' + code[6:] + 'M'
        # 15位身份证按19xx年考虑，先转为18位，校验位暂未‘M’，这样方便后面的判断和计算
    if not (code[:17].isdigit() and (code[-1].isdigit() or code[-1] == 'M' or code[-1].upper() == 'X')):
        print('输入15位身份证要求全为数字，18位身份证前17位为数字，第18位为数字或字母“X”，请重新输入。')
        continue
    if idData.get(code[:6]) == None:
        print('输入的前6位是归属地代码，你输入的归属地查不到，请重新输入。', )
        continue
    if checkDate(code) == False:
        print('15位身份证的7~12位为日期，18位身份证7~14位为日期，输入的日期有误，请重新输入。', )
        continue
    last = checkByte(code)  # 计算校验位
    if code[-1] == 'M':
        code = code[:17] + last
        print('15位转18位身份证号是：', code)
    elif code[-1] != last:
        code = code[:17] + last
        print('18位身份证校验错误，正确的号码可能是：', code)
    else:
        print('18位身份证校验正确。')
    print('身份证归属地：', idData[code[:6]])
    print('生日：', birthday, week[birthday.weekday()])
    print('年龄：', datetime.datetime.now().year - int(code[6:10]))
    print('性别：', sex(code))
