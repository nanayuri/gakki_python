class C:
    def __getattr__(self, name):
        print(1)

    def __getattribute__(self, name):
        print(2)

    def __setattr__(self, name, value):
        print(3)

    def __delattr__(self, name):
        print(4)


c = C()
c.x = 1
print(c.x)