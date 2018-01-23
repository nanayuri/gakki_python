import random

secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
right_num = 1
num1 = 1


def guess_num(x):
    guess = int(x)
    while guess != secret:
        x = input("哎呀，猜错了，请重新输入吧：")
        guess = int(x)
        if guess == secret:
            print("我草，你是小甲鱼心里的蛔虫吗？！")
            print("哼，猜中了也没有奖励！")
        else:
            if guess > secret:
                print("哥，大了大了~~~")
            else:
                print("嘿，小了，小了~~~")
    print("游戏结束，不玩啦^_^")


while right_num == 1:
    try:
        if num1 == 1:
            temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
        else:
            temp = input('必须输入一个整数，小数无效，请重新输入:')
        guess_num(temp)
        right_num = 0
    except ValueError:
        temp = input('必须输入一个整数，小数无效，请重新输入:')
        right_num = 1
        num1 = 0
    except EOFError:
        print('结束程序')
        right_num = 0
    except KeyboardInterrupt:
        print('结束程序')
        right_num = 0
