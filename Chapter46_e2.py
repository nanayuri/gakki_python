import os
import pickle


class MyDes:
    def __init__(self, name):
        self.name = name
        self.val = ''

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, value):
        self.val = value
        print(self.name)
        with open((str(self.name) + '.pickle'), 'wb') as f:
            pickle.dump(self.val, f)

    def __delete__(self, instance):
        os.remove(self.name + '.pickle')


class Test:
    x = MyDes('x')
    y = MyDes('y')

test = Test()
test.x = 123
test.y = "I love FishC.com"
print(test.x)
print(test.y)
del test.x
