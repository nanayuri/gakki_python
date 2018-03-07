class C:
    def __new__(cls, *args):
        s = 0
        str1 = ''
        for e in args:
            s += 1
            str1 += str(e) + ' '
        if s == 0:
            print('并没有传入参数')
        else:
            print('传入了%d个参数，分别是：' % s, str1)


class Word(str):
    def __init__(self, arg=''):
        if isinstance(arg, str):
            self.wlen = 0
            if arg.find(' ') != -1:
                print('value contains space')
                arg = arg[0:self.find(' ')]
            for each in arg:
                self.wlen += 1
        else:
            print('参数错误')

    def __lt__(self, other):
        return int.__lt__(self.wlen, other.wlen)
