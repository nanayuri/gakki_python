import random

times = 3#定义用户输入的次数

secret = random.randint(1,10)

print('猜数字游戏')

number = 0

print('请输入数字：',end='')

while (number != secret) and (times > 0):
    
    temp = input()
    
    number = int(temp)
    
    times = times - 1#用户没输入一次就减少一次
    
    if number == secret:
        print('真厉害，')
        print('猜中了！')
    else:
        if number >secret:
            print('猜错了，大了，')
        else:
            print('猜错了，小了，')
        if times > 0:
            print('再试一次吧：',end='')
        else:
            print('机会用光了')
print('游戏结束。')

