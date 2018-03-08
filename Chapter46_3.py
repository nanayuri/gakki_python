class MyDes:
    def __init__(self, value = None):
        self.val = value

    def __get__(self, instance, owner):
        return self.val - 20

    def __set__(self, instance, value):
        self.val = value + 10
        print(self.val)


class C:
    x = MyDes()


if __name__ == '__main__':  # 该模块被执行的话，执行下边语句。
    c = C()
    c.x = 10
    print(c.x)