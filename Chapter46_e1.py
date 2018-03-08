import time


class Record:
    def __init__(self, value, attr):
        self.val = value
        self.attr = attr

    def __get__(self, instance, owner):
        content = self.attr + '变量于北京时间 ' + time.strftime("%a %b %d %H:%M:%S %G") + '被读取, ' + self.attr + ' = ' + str(self.val) + '\n'
        with open('record.txt', 'a', encoding='Utf-8') as f:
            f.write(content)

    def __set__(self, instance, value):
        self.val = value
        content = self.attr + '变量于北京时间 ' + time.strftime(
            "%a %b %d %H:%M:%S %G") + '被修改, ' + self.attr + ' = ' + str(self.val) + '\n'
        with open('record.txt', 'a', encoding='Utf-8') as f:
            f.write(content)


class Test:
    x = Record(10, 'x')
    y = Record(8.8, 'y')


test = Test()
test.x
test.y
test.x = 123
test.x = 1.23
test.y = "I love FishC.com"