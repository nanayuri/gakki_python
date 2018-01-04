import string
def count(*x):
    digit = string.digits
    chara = string.ascii_letters
    i = 0
    for i in range(0,len(x)):
        spa = 0
        dig = 0
        cha = 0
        other = 0
        for each in x[i]:
            if each == ' ':
                spa += 1
            elif each in digit:
                dig += 1
            elif each in chara:
                cha += 1
            else:
                other += 1
        print("第"+str(i+1)+"个字符串共有：英文字母 "+str(cha)+" 个，数字 "+str(dig)+" 个，空格 "+str(spa)+" 个，其他字符 "+str(other)+" 个。")     
        i += 1


        
    
    
