def findstr(x,y):
    lens = len(x)
    times = 0
    for i in range(0,lens-1):
        if x[i:i+2] == y:
            times += 1
    print("子字符串在目标字符串中共出现 "+str(times)+" 次")

tgtstr = input("请输入目标字符串:")
fndstr = input("请输入子字符串(两个字符)：")
findstr(tgtstr,fndstr)
