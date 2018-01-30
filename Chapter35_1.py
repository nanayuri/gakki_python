import easygui as g

msg = "【*真实姓名】为必填项\n【*手机号码】为必填项\n【*E-mail】为必填项"
title = "账号中心"
fieldNames = ["*用户名", "*真实姓名", "固定电话", "*手机号码", "QQ", "*Email"]
fieldValues = []
filedValues = g.multenterbox(msg, title, fieldNames)
print(fieldValues)
while True:
    if fieldValues is None:
        break
    errmsg = ""
    try:
        for i in range(len(fieldNames)):
            option = fieldNames[i].strip()
            # print(fieldValues)
            if fieldValues[i].strip() == "" and option[0] == "*":
                errmsg += ("【%s】为必填项   " %fieldNames[i])
            if errmsg == "":
                break
            fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
    except IndexError:
        pass
g.msgbox("您填写的资料如下:%s" %str(fieldValues))