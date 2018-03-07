class MyDescripter:
    def __get__(self, instance, owner):
        print("getting...", self, instance, owner)

    def __set__(self, instance, value):
        print("setting...", self, instance, value)

    def __delete__(self, instance):
        print("deleting...", self, instance)


class Test:
    x = MyDescripter()


class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)

