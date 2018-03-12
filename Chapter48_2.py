class MyRev():
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        return reversed(self.x)

    def __next__(self):
        return next(self)

