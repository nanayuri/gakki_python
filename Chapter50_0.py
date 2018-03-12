import sys

sys.modules[__name__] = Const()


class Const:
    class ConstError(TypeError) :
        pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError("不能修改常量")
        self.__dict__[name] = value




