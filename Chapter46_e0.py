class Test:
    x = MyDes(10, 'x')

class MyDes:
    def __init__(self, value, attr):
        self.val = value
        self.attr = attr

    def __get__(self, instance, owner):
        print('正在获取变量: ' + self.attr)
        return self.val

    def __set__(self, instance, value):
        print('正在修改变量: ' + self.attr)
        self.val = value
        return self.val

    def __delete__(self, instance):
        print('正在删除变量: ' + self.attr)
        print('噢，这个变量没法删除~')
