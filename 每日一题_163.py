class Nint(int):
    def __init__(self, x):
        self.x = x

    def __truediv__(self, other):
        self.div = int.__truediv__(self, other)
        if self.div == int(self.div):
            return int(self.div)
        else:
            return self.div

    def __rtruediv__(self, other):
        self.div = int.__rtruediv__(self, other)
        if self.div == int(self.div):
            return int(self.div)
        else:
            return self.div


a = Nint(9)
b = Nint(8)
c = Nint(4)
print(a/c)
print(b/c)
print(12/c)
print(13/c)
print(a/3)
print(a/5)