intipt = input("请输入一个整数（输入Q结束程序):")
while 1:
    if intipt.isdigit():
        dhex = '%#x' %int(intipt)
        doct = '%#o' %int(intipt)
        dbin =  bin(int(intipt))
        print("十进制 -> 十六进制:"+str(intipt)+"->"+str(dhex))
        print("十进制 -> 八进制:"+str(intipt)+"->"+str(doct))
        print("十进制 -> 二进制:"+str(intipt)+"->"+str(dbin))
        print('十进制 -> 十六进制: %d -> 0x%x' %(int(intipt),int(intipt)))
        print('十进制 -> 八进制: %d -> 0o%o' %(int(intipt),int(intipt)))
        print('十进制 -> 二进制: %d -> ' %int(intipt),bin(int(intipt)))
        break
    elif intipt == 'Q':
        break

        
    

    
