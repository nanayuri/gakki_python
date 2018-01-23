try:
    f = open('我为什么是一个文件.txt', 'w')
    f.write('我存在了')
    sum1 = 1 + '1'


except OSError as reason:
    print('文件出错啦\n错误的原因是：' + str(reason))
except TypeError as reason:
    print('类型出错啦\n错误的原因是：' + str(reason))
finally:
    f.close()