MyDict = {}
print("|---- 欢迎进入通讯录程序 ---|")
print("|---- 1 :查询联系人资料 ---|")
print("|---- 2 ：插入新的联系人 ---|")
print("|---- 3 ：删除已有联系人 ---|")
print("|---- 4 ：退出通讯录程序 ---|")

ipt = int(input("请输入相关的指令代码:"))
str2 = ''
def Book(x):
    global MyDict
    if x == 4:
        print("感谢使用通讯录程序!")
    elif x == 2:
        str2 = input("请输入联系人姓名:")
        if MyDict.get(str2,'noexist') != 'noexist':
            print("您输入的姓名在通讯录中已存在 -->>" + str2 + " : "+MyDict[str2])
            if input("是否修改用户资料(Yes/No):") == 'Yes':
                MyDict = {str2:input("请输入用户联系电话:")}
                print('\n')
                aa = int(input("请输入相关的指令代码:"))
                Book(aa)
            else:
                print('\n')
                aa = int(input("请输入相关的指令代码:"))
                Book(aa)
        else:
            MyDict[str2] = int(input("请输入用户联系电话:"))
            print('\n')
            aa = int(input("请输入相关的指令代码:"))
            Book(aa)
    elif x == 1:
        str1 = input("请输入联系人姓名:")
        if MyDict.get(str1,'noexist') == 'noexist':
            print("您查询的联系人不在通讯录中!")
            print('\n')
            aa = int(input("请输入相关的指令代码:"))
            Book(aa)
        else:
            print(str1 + " : " + str(MyDict[str1]))
            print('\n')
            aa = int(input("请输入相关的指令代码:"))
            Book(aa)
    elif x == 3:
        str3 = input("请输入需要删除的联系人姓名:")
        if MyDict.get(str3,'noexist') != 'noexist':
            MyDict.pop(str3)
            print("删除联系人成功!")
            print('\n')
            aa = int(input("请输入相关的指令代码:"))
            Book(aa)
        else:
            print("此联系人已不在通讯录中!")
            print('\n')
            aa = int(input("请输入相关的指令代码:"))
            Book(aa)
            
        
Book(ipt)
