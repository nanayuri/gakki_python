usertxt = input("请输入一句话:")
def hwl(x):
    lens = len(x)
    count = lens // 2
    i = 0
    cal = 0
    for i in range(0,count):
        if x[i] != x[lens-1-i]:
            cal += 1

    if cal == 0:
        print("是回文联!")
    else:
        print("不是回文联!")

hwl(usertxt)
        
    
    
