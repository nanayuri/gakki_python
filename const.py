import sys


class Const:
    class ConstError(TypeError) :
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("不能修改常量")
        if not str(name).isupper():
            raise self.ConstError("常量名必须由大写字母组成!")

        self.__dict__[name] = value


sys.modules[__name__] = Const()


def test():
    const = Const()
    const.NAME = "FishC"
    print(const.NAME)

    try:
        # 尝试修改常量
        const.NAME = "FishC.com"
    except TypeError as Err:
        print(Err)

    try:
        # 变量名需要大写
        const.name = "FishC"
    except TypeError as Err:
        print(Err)


if __name__ == '__main__':
    test()


