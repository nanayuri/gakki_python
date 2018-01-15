###用户登录程序###
dict1 = {}
def pt():
    print("|--- 新建用户:N/n ---|")
    print("|--- 登录账号:E/e ---|")
    print("|--- 退出程序:Q/q ---|")

def usernameck(x):
    #global dict1
    if x not in dict1:
        pswd = input("请输入密码:")
        dict1[x] = pswd
        print("注册成功，赶紧试试登录吧^_^"+"\n")
        return dict1
    else:
        username1 = input("此用户名已经被使用，请重新输入:")
        usernameck(username1)

def loginck(x):
    #global dict1
    if x not in dict1:
        k = input("您输入的用户名不存在，请重新输入:")
        loginck(k)
    else:
        pw = input("请输入密码:")
        if pw == dict1[x]:
            print("欢迎进入系统，请点击右上角的x结束程序!")
        else:
            j = input("密码错误，请重新输入用户名：")
            loginck(j)


def login(x):
    if x.lower() == 'n':
        username = input("请输入用户名:")
        usernameck(username)
        pt()
        iptin = input("|--- 请输入指令代码:")
        login(iptin)

    if x.lower() == 'e':
        ipte = input("请输入用户名:")
        loginck(ipte)

    if x.lower() == 'q':
        print("已退出程序!")
    
pt()       
ipt = input("|--- 请输入指令代码:")
login(ipt)


      
    
    
    
    
